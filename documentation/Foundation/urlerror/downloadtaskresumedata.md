# downloadTaskResumeData

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An opaque data object used to resume a failed download task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var downloadTaskResumeData: Data? { get }
```

## Discussion

Pass this object to [`downloadTask(withResumeData:)`](../urlsession/downloadtask%28withresumedata%29.md) or [`downloadTask(withResumeData:completionHandler:)`](../urlsession/downloadtask%28withresumedata,completionhandler%29.md) to create a new download task that can attempt to resume the failed download.

## See Also

### Error details
- [var failingURL: URL?](./failingurl.md)
  The URL which caused a load to fail.
- [var failureURLPeerTrust: SecTrust?](./failureurlpeertrust.md)
  The state of a failed SSL handshake.
- [var failureURLString: String?](./failureurlstring.md)
  The string for the URL which caused a load to fail.
- [var backgroundTaskCancelledReason: URLError.BackgroundTaskCancelledReason?](./backgroundtaskcancelledreason-swift.property.md)
  The reason for canceling a background task.
- [URLError.BackgroundTaskCancelledReason](./backgroundtaskcancelledreason-swift.enum.md)
  An enumeration of reasons used to explain the cancellation of a background task.
- [var networkUnavailableReason: URLError.NetworkUnavailableReason?](./networkunavailablereason-swift.property.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](./networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/downloadtaskresumedata)*