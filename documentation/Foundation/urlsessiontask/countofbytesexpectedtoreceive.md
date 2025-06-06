# countOfBytesExpectedToReceive

**Framework**: Foundation  
**Kind**: property

The number of bytes that the task expects to receive in the response body.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var countOfBytesExpectedToReceive: Int64 { get }
```

#### Discussion

This value is determined based on the `Content-Length` header received from the server. If that header is absent, the value is [`NSURLSessionTransferSizeUnknown`](nsurlsessiontransfersizeunknown.md).

## See Also

- [var progress: Progress](urlsessiontask/progress.md)
  A representation of the overall task progress.
- [var countOfBytesReceived: Int64](urlsessiontask/countofbytesreceived.md)
  The number of bytes that the task has received from the server in the response body.
- [var countOfBytesExpectedToSend: Int64](urlsessiontask/countofbytesexpectedtosend.md)
  The number of bytes that the task expects to send in the request body.
- [var countOfBytesSent: Int64](urlsessiontask/countofbytessent.md)
  The number of bytes that the task has sent to the server in the request body.
- [let NSURLSessionTransferSizeUnknown: Int64](nsurlsessiontransfersizeunknown.md)
  The total size of the transfer cannot be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytesexpectedtoreceive)*