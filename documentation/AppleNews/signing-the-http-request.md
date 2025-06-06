# Signing the HTTP Request

**Framework**: Apple News

Sign the canonical request and send the custom authorization header to the Apple News API.

#### Overview

When communicating using HTTP protocol, the server validates the identity of the client and provides authorization for specific actions. By signing the HTTP request, the Apple News API authenticates the client and authorizes your news channel. See [`About the Apple News Security Model`](about-the-apple-news-security-model.md).

- Create a canonical request.
- Sign the canonical request.
- Create a custom authorization header.
- Send the header and the request to the Apple News API.

##### Copy This Code

Open any text editor to copy this code. Save the file as `read_channel.py`.

```python
import base64
import hmac
import requests
import sys
from datetime import datetime
import hashlib 

class PublisherAPI:
    channel_id = ""
    current_action = ""
    key_id = ""
    key_secret = ""
    url = ""

    def send_request(self, method, url, content_type=None):
        date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        canonical_request = method + url + date
        canonical_request = canonical_request.encode()
        signature = self.create_signature(canonical_request)
        authorization = "HHMAC; key=%s; signature=%s; date=%s" % (
            self.key_id, signature, date)
        headers = {"Authorization": authorization}
        return requests.request(method, url, headers=headers)

    def create_signature(self, canonical_request):
        key_bytes = base64.b64decode(self.key_secret)
        message = canonical_request
        secret = self.key_secret.encode("utf-8")

        signature = base64.b64encode(
            hmac.new(key_bytes, message,digestmod=hashlib.sha256).digest()).decode("utf-8")
        return signature

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
    if not len(sys.argv) > 4:
        print ('no or missing arguments')
        exit()

    publisherAPI = PublisherAPI()
    publisherAPI.url = sys.argv[1] + "/channels/"
    publisherAPI.channel_id = sys.argv[2]
    publisherAPI.key_id = sys.argv[3]
    publisherAPI.key_secret = sys.argv[4]
    publisherAPI.current_action = "readChannel"

    response = publisherAPI.main()

    print(response.status_code)
    print(response.text)
```

##### Run the Script

Start the command prompt and change to the directory containing `read_channel.py`. Run this script to make a properly authenticated [`Read Channel Information`](https://developer.apple.com/documentation/applenewsapi/get-channels-_channelid_) request to the Apple News API. This script takes four arguments: API URL `(https://news-api.apple.com`), Channel ID, Key ID, and the Secret.

```swift
python read_channel.py https://news-api.apple.com channel_id key_id key_secret
```

##### Result

The server returns a  successful response. The response includes information about the channel, as shown here. See [`Channel`](https://developer.apple.com/documentation/applenewsapi/channel) and [`ChannelLinks`](https://developer.apple.com/documentation/applenewsapi/channellinks).

```json
{
    "data": {
        "createdAt": "2016-06-13T00:25:43Z",
        "modifiedAt": "2016-06-13T23:30:05Z",
        "id": "42424242-4242-4242-4242-424242424242",
        "type": "channel",
        "shareUrl": "https://apple.news/Taaaaaaaaaaaaaaaaaaaaaa",
        "links": {
            "defaultSection": "https://news-api.apple.com/sections/42424242-4242-4242-4242-424242424242",
            "self": "https://news-api.apple.com/channels/42424242-4242-4242-4242-424242424242"
        },
        "name": "My Channel",
        "website": "http://mychannel.com"
    }
}
```

##### How It Works

The canonical request combines the method, the URL, and the current date, as shown here:

```python
date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
canonical_request = method + url + date
```

The date is formatted as shown here:

`{Year with century as a decimal number}-{Month as a zero-padded decimal number}-{Day of the month as a zero-padded decimal number}T{Hour (24-hour clock) as a zero-padded decimal number}:{Minute as a zero-padded decimal number}:{Second as a zero-padded decimal number}Z`

The date format looks like this:

```other
2018-08-10T23:55:11Z
```

The canonical request looks like this:

```other
GEThttps://news-api.apple.com/channels/{channel-id}2018-08-10T23:57:00Z
```

You create a custom authorization header by combining the Key ID, the signed canonical request, and the formatted current date, as shown here:

`{'HHMAC; key={Key ID}; signature={Signed Canonical Request}; date={Formatted Current Date'}`

The header looks like this:

```other
{'Authorization': 'HHMAC; key={Key ID}; signature=1rBvQKZeQ6M3/dVMtv95Dc51V+QViaqUB0bF6exzYtw
```

Finally, you send the header and the request to the Apple News API. The request looks like this:

```python
return requests.request(method, url, headers=headers)
```

## See Also

- [Making an HTTP Request to the Apple News API](making-an-http-request-to-the-apple-news-api.md)
  Create the URL, set the method, and send the request.
- [Publishing an Article](publishing-an-article.md)
  Build a URL and article body for the publish-article request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/signing-the-http-request)*