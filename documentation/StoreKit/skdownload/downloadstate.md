# downloadState

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The current state of the download object.

**Availability**:
- iOS 6.0+ - Deprecated in 12.0
- iPadOS 6.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 12.0

## Declaration

```swift
var downloadState: SKDownloadState { get }
```

```objc
@property (nonatomic, readonly) SKDownloadState downloadState;
```

## Mentions

- [Unlocking purchased content](../unlocking-purchased-content.md)

#### Discussion

After you queue a download object, the payment queue object calls your transaction observer when the state of the download object changes. Your transaction observer should read the [`downloadState`](./downloadstate.md) property and use it to determine how to proceed. For more information on the different states, see [`SKDownloadState`](../skdownloadstate.md).

## See Also

### Getting State Information
- [var state: SKDownloadState](./state.md)
  The current state of the download object.
- [var progress: Float](./progress.md)
  A value that indicates how much of the file has been downloaded.
- [var timeRemaining: TimeInterval](./timeremaining.md)
  An estimated time, in seconds, to finish downloading the content.
- [var SKDownloadTimeRemainingUnknown: TimeInterval](../skdownloadtimeremainingunknown.md)
  Indicates that the system cannot determine how much time is needed to finish downloading the content.
- [enum SKDownloadState](../skdownloadstate.md)
  The states that a download operation can be in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skdownload/downloadstate)*