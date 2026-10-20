# progress

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A representation of the overall task progress.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var progress: Progress { get }
```

```objc
@property (strong, readonly) NSProgress * progress;
```

## Mentions

- [Downloading files from websites](../downloading-files-from-websites.md)

## See Also

### Obtaining task progress
- [var countOfBytesExpectedToReceive: Int64](./countofbytesexpectedtoreceive.md)
  The number of bytes that the task expects to receive in the response body.
- [var countOfBytesReceived: Int64](./countofbytesreceived.md)
  The number of bytes that the task has received from the server in the response body.
- [var countOfBytesExpectedToSend: Int64](./countofbytesexpectedtosend.md)
  The number of bytes that the task expects to send in the request body.
- [var countOfBytesSent: Int64](./countofbytessent.md)
  The number of bytes that the task has sent to the server in the request body.
- [let NSURLSessionTransferSizeUnknown: Int64](../nsurlsessiontransfersizeunknown.md)
  The total size of the transfer cannot be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/progress)*