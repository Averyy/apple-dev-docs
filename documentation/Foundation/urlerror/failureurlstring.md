# failureURLString

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The string for the URL which caused a load to fail.

**Availability**:
- iOS 8.0+ - Deprecated in 18.4
- iPadOS 8.0+ - Deprecated in 18.4
- Mac Catalyst 8.0+ - Deprecated in 18.4
- macOS 10.10+ - Deprecated in 15.4
- tvOS 9.0+ - Deprecated in 18.4
- visionOS 1.0+ - Deprecated in 2.4
- watchOS 2.0+ - Deprecated in 11.4

> **Deprecated**: Use failingURL instead

## Declaration

```swift
var failureURLString: String? { get }
```

## See Also

### Error details
- [var failingURL: URL?](./failingurl.md)
  The URL which caused a load to fail.
- [var failureURLPeerTrust: SecTrust?](./failureurlpeertrust.md)
  The state of a failed SSL handshake.
- [var downloadTaskResumeData: Data?](./downloadtaskresumedata.md)
  An opaque data object used to resume a failed download task.
- [var backgroundTaskCancelledReason: URLError.BackgroundTaskCancelledReason?](./backgroundtaskcancelledreason-swift.property.md)
  The reason for canceling a background task.
- [URLError.BackgroundTaskCancelledReason](./backgroundtaskcancelledreason-swift.enum.md)
  An enumeration of reasons used to explain the cancellation of a background task.
- [var networkUnavailableReason: URLError.NetworkUnavailableReason?](./networkunavailablereason-swift.property.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](./networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/failureurlstring)*