# NSAnimation.BlockingMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants indicate the blocking mode of an `NSAnimation` object when it is running.

**Availability**:
- macOS

## Declaration

```swift
enum BlockingMode
```

```c
enum NSAnimationBlockingMode : NSUInteger;
```

## Overview

You specify one of these constants in the [`animationBlockingMode`](./animationblockingmode.md) property.

## Topics

### Constants
- [NSAnimation.BlockingMode.blocking](./blockingmode/blocking.md)
  Requests the animation to run in the main thread in a custom run-loop mode that blocks user input.
- [NSAnimation.BlockingMode.nonblocking](./blockingmode/nonblocking.md)
  Requests the animation to run in a standard or specified run-loop mode that allows user input.
- [NSAnimation.BlockingMode.nonblockingThreaded](./blockingmode/nonblockingthreaded.md)
  Requests the animation to run in a separate thread that is spawned by the `NSAnimation` object.
### Initializers
- [init?(rawValue: UInt)](./blockingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSAnimation.Curve](./curve.md)
  These constants describe the curve of an animation—that is, the relative speed of an animation from start to finish.
- [NSAnimation.Progress](./progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [NSAnimationProgressMark Notification Key](../nsanimationprogressmark-notification-key.md)
  This constant is returned in the userInfo dictionary of the [`progressMarkNotification`](./progressmarknotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/blockingmode)*