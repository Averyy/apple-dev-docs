# SKDownloadTimeRemainingUnknown

**Framework**: StoreKit  
**Kind**: var  
**Role**: Global Variable

Indicates that the system cannot determine how much time is needed to finish downloading the content.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var SKDownloadTimeRemainingUnknown: TimeInterval
```

```c
extern NSTimeInterval SKDownloadTimeRemainingUnknown;
```

## See Also

### Getting State Information
- [var state: SKDownloadState](./skdownload/state.md)
  The current state of the download object.
- [var progress: Float](./skdownload/progress.md)
  A value that indicates how much of the file has been downloaded.
- [var timeRemaining: TimeInterval](./skdownload/timeremaining.md)
  An estimated time, in seconds, to finish downloading the content.
- [enum SKDownloadState](./skdownloadstate.md)
  The states that a download operation can be in.
- [var downloadState: SKDownloadState](./skdownload/downloadstate.md)
  The current state of the download object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownloadtimeremainingunknown)*