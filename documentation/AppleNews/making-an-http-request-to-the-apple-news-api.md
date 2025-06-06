# Making an HTTP Request to the Apple News API

**Framework**: Apple News

Create the URL, set the method, and send the request.

#### Overview

You make an HTTP request to send or receive data from a server. On this page, you’ll make the HTTP request to the Apple News API to get details about the channel, including the name, corresponding website, and default section. See [`Read Channel Information`](https://developer.apple.com/documentation/applenewsapi/get-channels-_channelid_).

- Create the URL `https://news-api.apple.com/channels/{channel-id}`.
- Set the method to `GET`.
- Send the request.

##### Copy This Code

Open any text editor to copy this code.  Save the file as `make_an_http_request.py`.

```python
import sys
import requests

class PublisherAPI:
    channel_id = ""
    current_action = ""
    url = ""

    def send_request(self, method, url):
        return requests.request(method, url)
    
    def read_channel(self):
        method = "GET"
        url = self.url + "%s" % self.channel_id
        return self.send_request(method, url)

    def main(self):
        if self.current_action == "readChannel":
            response = self.read_channel()
        else:
            response = {
                "status_code": 400,
                "response": "{\"errors\":[{\"code\":\"UNKNOWN_COMMAND\"}]}"
            }
        return response

    if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('no arguments')
        exit()

  publisherAPI = PublisherAPI()
  publisherAPI.url = sys.argv[1] + "/channels/"
  publisherAPI.channel_id = sys.argv[2]
  publisherAPI.current_action = "readChannel"

  response = publisherAPI.main()

  print(response.status_code)
  print(response.text)
```

##### Run the Script

Start the command prompt and change to the directory containing `make_an_http_request.py` file. Run this script to make an HTTP request to the Apple News API. This script takes Channel ID as an argument.

```python
$ python make_an_http_request.py channel_id
```

##### Result

The script returns this error:

`{"errors":[{"code":"UNAUTHORIZED"}]}`

The error indicates that the HTTP request didn’t include the authorization header.

## See Also

- [Signing the HTTP Request](signing-the-http-request.md)
  Sign the canonical request and send the custom authorization header to the Apple News API.
- [Publishing an Article](publishing-an-article.md)
  Build a URL and article body for the publish-article request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/making-an-http-request-to-the-apple-news-api)*