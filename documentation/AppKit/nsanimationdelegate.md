# NSAnimationDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods implemented by delegates of [`NSAnimation`](nsanimation.md) objects.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAnimationDelegate : NSObjectProtocol
```

## Topics

### Controlling and Monitoring an Animation
- [func animationDidEnd(NSAnimation)](nsanimationdelegate/animationdidend(_:).md)
  Sent to the delegate when the specified animation completes its run.
- [func animationDidStop(NSAnimation)](nsanimationdelegate/animationdidstop(_:).md)
  Sent to the delegate when the specified animation is stopped before it completes its run.
- [func animationShouldStart(NSAnimation) -> Bool](nsanimationdelegate/animationshouldstart(_:).md)
  Sent to the delegate just after an animation is started.
- [func animation(NSAnimation, valueForProgress: NSAnimation.Progress) -> Float](nsanimationdelegate/animation(_:valueforprogress:).md)
  Requests a custom curve value for the current progress value.
### Managing Progress Marks
- [func animation(NSAnimation, didReachProgressMark: NSAnimation.Progress)](nsanimationdelegate/animation(_:didreachprogressmark:).md)
  Sent to the delegate when an animation reaches a specific progress mark.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTitlebarAccessoryViewController](nstitlebaraccessoryviewcontroller.md)

## See Also

- [class NSAnimation](nsanimation.md)
  An object that manages the timing and progress of animations in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate)*