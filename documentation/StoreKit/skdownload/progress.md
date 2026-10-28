# progress

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates how much of the file has been downloaded.

**Availability**:
- iOS 6.0+ - Deprecated in 16.0
- iPadOS 6.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var progress: Float { get }
```

```objc
@property (nonatomic, readonly) float progress;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

## Discussion

The value of this property is a floating point number between `0.0` and `1.0`, inclusive, where `0.0` means no data has been download and `1.0` means all the data has been downloaded. Typically, your app uses the value of this property to update a user interface element, such as a progress bar, that displays how much of the file has been downloaded.

Do not use the value of this property to determine whether the download has completed. Instead, use the [`downloadState`](./downloadstate.md) property.

## See Also

### Getting State Information
- [var state: SKDownloadState](./state.md)
  The current state of the download object.
- [var timeRemaining: TimeInterval](./timeremaining.md)
  An estimated time, in seconds, to finish downloading the content.
- [var SKDownloadTimeRemainingUnknown: TimeInterval](../skdownloadtimeremainingunknown.md)
  Indicates that the system cannot determine how much time is needed to finish downloading the content.
- [enum SKDownloadState](../skdownloadstate.md)
  The states that a download operation can be in.
- [var downloadState: SKDownloadState](./downloadstate.md)
  The current state of the download object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/progress)*