# state

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The current state of the download object.

**Availability**:
- iOS 12.0+ - Deprecated in 16.0
- iPadOS 12.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.8+ - Deprecated in 13.0
- tvOS 12.0+ - Deprecated in 16.0
- watchOS 6.2+ - Deprecated in 9.0

> **Deprecated**: Hosted content is no longer supported.

## Declaration

```swift
var state: SKDownloadState { get }
```

```objc
@property (nonatomic, readonly) SKDownloadState state;
```

## Discussion

After you queue a download object, the payment queue object calls your transaction observer when the state of the download object changes. Your transaction observer should read the [`state`](./state.md) property and use it to determine how to proceed. For more information on the different states, see [`SKDownloadState`](../skdownloadstate.md).

## See Also

### Getting State Information
- [var progress: Float](./progress.md)
  A value that indicates how much of the file has been downloaded.
- [var timeRemaining: TimeInterval](./timeremaining.md)
  An estimated time, in seconds, to finish downloading the content.
- [var SKDownloadTimeRemainingUnknown: TimeInterval](../skdownloadtimeremainingunknown.md)
  Indicates that the system cannot determine how much time is needed to finish downloading the content.
- [enum SKDownloadState](../skdownloadstate.md)
  The states that a download operation can be in.
- [var downloadState: SKDownloadState](./downloadstate.md)
  The current state of the download object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/state)*