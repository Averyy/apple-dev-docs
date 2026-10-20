# countOfResponseBodyBytesAfterDecoding

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The size of data delivered to your delegate or completion handler.

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
var countOfResponseBodyBytesAfterDecoding: Int64 { get }
```

```objc
@property (readonly) int64_t countOfResponseBodyBytesAfterDecoding;
```

## See Also

### Accessing data transfer metrics
- [var countOfRequestBodyBytesBeforeEncoding: Int64](./countofrequestbodybytesbeforeencoding.md)
  The size of the upload body data, file, or stream, in bytes.
- [var countOfRequestBodyBytesSent: Int64](./countofrequestbodybytessent.md)
  The number of bytes transferred for the request body.
- [var countOfRequestHeaderBytesSent: Int64](./countofrequestheaderbytessent.md)
  The number of bytes transferred for the request header.
- [var countOfResponseBodyBytesReceived: Int64](./countofresponsebodybytesreceived.md)
  The number of bytes transferred for the response body.
- [var countOfResponseHeaderBytesReceived: Int64](./countofresponseheaderbytesreceived.md)
  The number of bytes transferred for the response header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesafterdecoding)*