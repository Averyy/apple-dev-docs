# backgroundTaskCancelledReason

**Framework**: Foundation  
**Kind**: property

The reason for canceling a background task.

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
var backgroundTaskCancelledReason: URLError.BackgroundTaskCancelledReason? { get }
```

#### Discussion

If the error doesn’t involve cancellation of a background task, this property is `nil`.

## See Also

- [var failingURL: URL?](urlerror/failingurl.md)
  The URL which caused a load to fail.
- [var failureURLPeerTrust: SecTrust?](urlerror/failureurlpeertrust.md)
  The state of a failed SSL handshake.
- [var failureURLString: String?](urlerror/failureurlstring.md)
  The string for the URL which caused a load to fail.
- [var downloadTaskResumeData: Data?](urlerror/downloadtaskresumedata.md)
  An opaque data object used to resume a failed download task.
- [URLError.BackgroundTaskCancelledReason](urlerror/backgroundtaskcancelledreason-swift.enum.md)
  An enumeration of reasons used to explain the cancellation of a background task.
- [var networkUnavailableReason: URLError.NetworkUnavailableReason?](urlerror/networkunavailablereason-swift.property.md)
  The reason the network was unavailable for a task.
- [URLError.NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md)
  An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.property)*