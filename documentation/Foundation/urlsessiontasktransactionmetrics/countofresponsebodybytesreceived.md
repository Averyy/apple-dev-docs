# countOfResponseBodyBytesReceived

**Framework**: Foundation  
**Kind**: property

The number of bytes transferred for the response body.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var countOfResponseBodyBytesReceived: Int64 { get }
```

#### Discussion

This value includes protocol-specific framing, transfer encoding, and content encoding.

## See Also

- [var countOfRequestBodyBytesBeforeEncoding: Int64](urlsessiontasktransactionmetrics/countofrequestbodybytesbeforeencoding.md)
  The size of the upload body data, file, or stream, in bytes.
- [var countOfRequestBodyBytesSent: Int64](urlsessiontasktransactionmetrics/countofrequestbodybytessent.md)
  The number of bytes transferred for the request body.
- [var countOfRequestHeaderBytesSent: Int64](urlsessiontasktransactionmetrics/countofrequestheaderbytessent.md)
  The number of bytes transferred for the request header.
- [var countOfResponseBodyBytesAfterDecoding: Int64](urlsessiontasktransactionmetrics/countofresponsebodybytesafterdecoding.md)
  The size of data delivered to your delegate or completion handler.
- [var countOfResponseHeaderBytesReceived: Int64](urlsessiontasktransactionmetrics/countofresponseheaderbytesreceived.md)
  The number of bytes transferred for the response header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesreceived)*