# failureURLString

**Framework**: Foundation  
**Kind**: property

The string for the URL which caused a load to fail.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var failureURLString: String? { get }
```

## See Also

- [var failingURL: URL?](urlerror/failingurl.md)
  The URL which caused a load to fail.
- [var failureURLPeerTrust: SecTrust?](urlerror/failureurlpeertrust.md)
  The state of a failed SSL handshake.
- [var downloadTaskResumeData: Data?](urlerror/downloadtaskresumedata.md)
  An opaque data object used to resume a failed download task.
- [var backgroundTaskCancelledReason: URLError.BackgroundTaskCancelledReason?](urlerror/backgroundtaskcancelledreason-swift.property.md)
  The reason for canceling a background task.
- [URLError.BackgroundTaskCancelledReason](urlerror/backgroundtaskcancelledreason-swift.enum.md)
  An enumeration of reasons used to explain the cancellation of a background task.
- [var networkUnavailableReason: URLError.NetworkUnavailableReason?](urlerror/networkunavailablereason-swift.property.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/failureurlstring)*