from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://blog.csdn.net/haoel/article/details/2872'
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()

def extract(url, fn):
  driver.get(URL)
  driver.implicitly_wait(1)
  old_source = page_source = driver.page_source
  
  # Send the Page Down key
  body = driver.find_element(By.TAG_NAME, "body")
  body.send_keys(Keys.PAGE_DOWN)
  
  new_source =  driver.page_source
  while old_source != new_source:
    old_source = new_source
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_DOWN)
    new_source = driver.page_source
  
  with open(fn, 'w') as f:
    f.write(page_source)


urls = [x.split(' ')[0].strip().replace('"', '') for x in open('blog.url.txt').readlines()]
for url in urls:
  fn = url[ ( 1 + url.rfind('/')) :] + '.html'
  print("extract:", url, fn)
  extract(url, fn)
  
driver.quit()


