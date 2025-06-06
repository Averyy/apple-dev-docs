# rawData

**Framework**: MailKit  
**Kind**: property

The raw RFC 2822 header and body content of the message.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var rawData: Data? { get }
```

#### Discussion

The content is available after MailKit downloads the message. MailKit provides the content as unprocessed data. For details about the format of the data, see [`RFC 2822`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2822).

> **Note**:  This property includes the full content of the message, and contains both the headers and the message body. If you only need the headers in the message, use [`headers`](memessage/headers.md) instead.

 This property includes the full content of the message, and contains both the headers and the message body. If you only need the headers in the message, use [`headers`](memessage/headers.md) instead.

## See Also

- [var headers: [String : [String]]?](memessage/headers.md)
  A dictionary that contains the message’s header values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessage/rawdata)*