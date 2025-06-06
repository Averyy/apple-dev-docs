# progress

**Framework**: StoreKit  
**Kind**: property

A value that indicates how much of the file has been downloaded.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- watchOS 6.2+

## Declaration

```swift
var progress: Float { get }
```

## Mentions

- [Unlocking purchased content](unlocking-purchased-content.md)

#### Discussion

The value of this property is a floating point number between `0.0` and `1.0`, inclusive, where `0.0` means no data has been download and `1.0` means all the data has been downloaded. Typically, your app uses the value of this property to update a user interface element, such as a progress bar, that displays how much of the file has been downloaded.

Do not use the value of this property to determine whether the download has completed. Instead, use the [`downloadState`](skdownload/downloadstate.md) property.

## See Also

- [var state: SKDownloadState](skdownload/state.md)
  The current state of the download object.
- [var timeRemaining: TimeInterval](skdownload/timeremaining.md)
  An estimated time, in seconds, to finish downloading the content.
- [var SKDownloadTimeRemainingUnknown: TimeInterval](skdownloadtimeremainingunknown.md)
  Indicates that the system cannot determine how much time is needed to finish downloading the content.
- [enum SKDownloadState](skdownloadstate.md)
  The states that a download operation can be in.
- [var downloadState: SKDownloadState](skdownload/downloadstate.md)
  The current state of the download object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/progress)*