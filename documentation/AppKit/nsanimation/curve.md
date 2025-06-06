# NSAnimation.Curve

**Framework**: AppKit  
**Kind**: enum

These constants describe the curve of an animation—that is, the relative speed of an animation from start to finish.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Curve
```

#### Overview

You initialize an `NSAnimation` object using one of these constants with [`init(duration:animationCurve:)`](nsanimation/init(duration:animationcurve:).md) and you can set it thereafter with the [`animationCurve`](nsanimation/animationcurve.md) property.

## Topics

### Constants
- [NSAnimation.Curve.easeInOut](nsanimation/curve/easeinout.md)
  Describes an S-curve in which the animation slowly speeds up and then slows down near the end of the animation. This constant is the default.
- [NSAnimation.Curve.easeIn](nsanimation/curve/easein.md)
  Describes an animation that slows down as it reaches the end.
- [NSAnimation.Curve.easeOut](nsanimation/curve/easeout.md)
  Describes an animation that slowly speeds up from the start.
- [NSAnimation.Curve.linear](nsanimation/curve/linear.md)
  Describes an animation in which there is no change in frame rate.
### Initializers
- [init?(rawValue: UInt)](nsanimation/curve/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSAnimation.BlockingMode](nsanimation/blockingmode.md)
  These constants indicate the blocking mode of an `NSAnimation` object when it is running.
- [NSAnimation.Progress](nsanimation/progress.md)
  The animation progress, as a floating-point number between `0.0` and `1.0`.
- [NSAnimationProgressMark Notification Key](nsanimationprogressmark-notification-key.md)
  This constant is returned in the userInfo dictionary of the [`progressMarkNotification`](nsanimation/progressmarknotification.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/curve)*