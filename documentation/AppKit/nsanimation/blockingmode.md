# NSAnimation.BlockingMode

**Framework**: AppKit  
**Kind**: enum

These constants indicate the blocking mode of an `NSAnimation` object when it is running.

**Availability**:
- macOS ?+

## Declaration

```swift
enum BlockingMode
```

#### Overview

You specify one of these constants in the [`animationBlockingMode`](nsanimation/animationblockingmode.md) property.

## Topics

### Constants
- [NSAnimation.BlockingMode.blocking](nsanimation/blockingmode/blocking.md)
  Requests the animation to run in the main thread in a custom run-loop mode that blocks user input.
- [NSAnimation.BlockingMode.nonblocking](nsanimation/blockingmode/nonblocking.md)
  Requests the animation to run in a standard or specified run-loop mode that allows user input.
- [NSAnimation.BlockingMode.nonblockingThreaded](nsanimation/blockingmode/nonblockingthreaded.md)
  Requests the animation to run in a separate thread that is spawned by the `NSAnimation` object.
### Initializers
- [init?(rawValue: UInt)](nsanimation/blockingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAnimation.Curve](nsanimation/curve.md)
  These constants describe the curve of an animation—that is, the relative speed of an animation from start to finish.
- [NSAnimation.Progress](nsanimation/progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [NSAnimationProgressMark Notification Key](nsanimationprogressmark-notification-key.md)
  This constant is returned in the userInfo dictionary of the [`progressMarkNotification`](nsanimation/progressmarknotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/blockingmode)*