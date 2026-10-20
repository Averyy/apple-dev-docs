# NSAnimation.Curve

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants describe the curve of an animation—that is, the relative speed of an animation from start to finish.

**Availability**:
- macOS

## Declaration

```swift
enum Curve
```

```c
enum NSAnimationCurve : NSUInteger;
```

#### Overview

You initialize an `NSAnimation` object using one of these constants with [`init(duration:animationCurve:)`](./init%28duration,animationcurve%29.md) and you can set it thereafter with the [`animationCurve`](./animationcurve.md) property.

## Topics

### Constants
- [NSAnimation.Curve.easeInOut](./curve/easeinout.md)
  Describes an S-curve in which the animation slowly speeds up and then slows down near the end of the animation. This constant is the default.
- [NSAnimation.Curve.easeIn](./curve/easein.md)
  Describes an animation that slows down as it reaches the end.
- [NSAnimation.Curve.easeOut](./curve/easeout.md)
  Describes an animation that slowly speeds up from the start.
- [NSAnimation.Curve.linear](./curve/linear.md)
  Describes an animation in which there is no change in frame rate.
### Initializers
- [init?(rawValue: UInt)](./curve/init%28rawvalue%29.md)

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
- [NSAnimation.BlockingMode](./blockingmode.md)
  These constants indicate the blocking mode of an `NSAnimation` object when it is running.
- [NSAnimation.Progress](./progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [NSAnimationProgressMark Notification Key](../nsanimationprogressmark-notification-key.md)
  This constant is returned in the userInfo dictionary of the [`progressMarkNotification`](./progressmarknotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/curve)*