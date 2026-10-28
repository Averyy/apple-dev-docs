# timeRemaining

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An estimated time, in seconds, to finish downloading the content.

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
var timeRemaining: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval timeRemaining;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

## Discussion

The system attempts to estimate how long it will take to finish downloading the file. If it cannot create a good estimate, the value of this property is set to [`SKDownloadTimeRemainingUnknown`](../skdownloadtimeremainingunknown.md).

## See Also

### Getting State Information
- [var state: SKDownloadState](./state.md)
  The current state of the download object.
- [var progress: Float](./progress.md)
  A value that indicates how much of the file has been downloaded.
- [var SKDownloadTimeRemainingUnknown: TimeInterval](../skdownloadtimeremainingunknown.md)
  Indicates that the system cannot determine how much time is needed to finish downloading the content.
- [enum SKDownloadState](../skdownloadstate.md)
  The states that a download operation can be in.
- [var downloadState: SKDownloadState](./downloadstate.md)
  The current state of the download object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/timeremaining)*