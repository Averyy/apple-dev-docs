# countOfBytesSent

**Framework**: Foundation  
**Kind**: property

The number of bytes that the task has sent to the server in the request body.

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
var countOfBytesSent: Int64 { get }
```

#### Discussion

This byte count includes  the length of the request body itself, not the request headers.

To be notified when this value changes, implement the [`urlSession(_:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:)`](urlsessiontaskdelegate/urlsession(_:task:didsendbodydata:totalbytessent:totalbytesexpectedtosend:).md) delegate method.

## See Also

- [var progress: Progress](urlsessiontask/progress.md)
  A representation of the overall task progress.
- [var countOfBytesExpectedToReceive: Int64](urlsessiontask/countofbytesexpectedtoreceive.md)
  The number of bytes that the task expects to receive in the response body.
- [var countOfBytesReceived: Int64](urlsessiontask/countofbytesreceived.md)
  The number of bytes that the task has received from the server in the response body.
- [var countOfBytesExpectedToSend: Int64](urlsessiontask/countofbytesexpectedtosend.md)
  The number of bytes that the task expects to send in the request body.
- [let NSURLSessionTransferSizeUnknown: Int64](nsurlsessiontransfersizeunknown.md)
  The total size of the transfer cannot be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytessent)*