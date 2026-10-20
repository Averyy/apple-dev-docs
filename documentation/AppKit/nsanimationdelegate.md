# NSAnimationDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by delegates of [`NSAnimation`](./nsanimation.md) objects.

**Availability**:
- macOS

## Declaration

```swift
protocol NSAnimationDelegate : NSObjectProtocol
```

```objc
@protocol NSAnimationDelegate <NSObject>
```

## Topics

### Controlling and Monitoring an Animation
- [func animationDidEnd(NSAnimation)](./nsanimationdelegate/animationdidend%28_%29.md)
  Sent to the delegate when the specified animation completes its run.
- [func animationDidStop(NSAnimation)](./nsanimationdelegate/animationdidstop%28_%29.md)
  Sent to the delegate when the specified animation is stopped before it completes its run.
- [func animationShouldStart(NSAnimation) -> Bool](./nsanimationdelegate/animationshouldstart%28_%29.md)
  Sent to the delegate just after an animation is started.
- [func animation(NSAnimation, valueForProgress: NSAnimation.Progress) -> Float](./nsanimationdelegate/animation%28_,valueforprogress%29.md)
  Requests a custom curve value for the current progress value.
### Managing Progress Marks
- [func animation(NSAnimation, didReachProgressMark: NSAnimation.Progress)](./nsanimationdelegate/animation%28_,didreachprogressmark%29.md)
  Sent to the delegate when an animation reaches a specific progress mark.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSTitlebarAccessoryViewController](./nstitlebaraccessoryviewcontroller.md)

## See Also

### Custom Animations
- [class NSAnimation](./nsanimation.md)
  An object that manages the timing and progress of animations in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate)*