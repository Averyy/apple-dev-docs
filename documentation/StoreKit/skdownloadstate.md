# SKDownloadState

**Framework**: StoreKit  
**Kind**: enum

The states that a download operation can be in.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
@frozen
enum SKDownloadState
```

## Topics

### Constants
- [SKDownloadState.waiting](skdownloadstate/waiting.md)
  Indicates that the download has not started yet.
- [SKDownloadState.active](skdownloadstate/active.md)
  Indicates that the content is currently being downloaded.
- [SKDownloadState.paused](skdownloadstate/paused.md)
  Indicates that your app paused the download.
- [SKDownloadState.finished](skdownloadstate/finished.md)
  Indicates that the content was successfully downloaded.
- [SKDownloadState.failed](skdownloadstate/failed.md)
  Indicates that an error occurred while the file was being downloaded.
- [SKDownloadState.cancelled](skdownloadstate/cancelled.md)
  Indicates that your app canceled the download.
### Initializers
- [init?(rawValue: Int)](skdownloadstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: SKDownloadState](skdownload/state.md)
  The current state of the download object.
- [var progress: Float](skdownload/progress.md)
  A value that indicates how much of the file has been downloaded.
- [var timeRemaining: TimeInterval](skdownload/timeremaining.md)
  An estimated time, in seconds, to finish downloading the content.
- [var SKDownloadTimeRemainingUnknown: TimeInterval](skdownloadtimeremainingunknown.md)
  Indicates that the system cannot determine how much time is needed to finish downloading the content.
- [var downloadState: SKDownloadState](skdownload/downloadstate.md)
  The current state of the download object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownloadstate)*