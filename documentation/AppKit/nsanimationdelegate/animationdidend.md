# animationDidEnd(_:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate when the specified animation completes its run.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
optional func animationDidEnd(_ animation: NSAnimation)
```

#### Discussion

When an `NSAnimation` object reaches the end of its planned duration, it has a progress value of 1.0.

## Parameters

- `animation`: The `NSAnimation` instance that completed its run.

## See Also

- [protocol NSAnimationDelegate](nsanimationdelegate.md)
  A set of optional methods implemented by delegates of [`NSAnimation`](nsanimation.md) objects.
- [var currentProgress: NSAnimation.Progress](nsanimation/currentprogress.md)
  The current progress of the animation.
- [func animationDidStop(NSAnimation)](nsanimationdelegate/animationdidstop(_:).md)
  Sent to the delegate when the specified animation is stopped before it completes its run.
- [func animationShouldStart(NSAnimation) -> Bool](nsanimationdelegate/animationshouldstart(_:).md)
  Sent to the delegate just after an animation is started.
- [func animation(NSAnimation, valueForProgress: NSAnimation.Progress) -> Float](nsanimationdelegate/animation(_:valueforprogress:).md)
  Requests a custom curve value for the current progress value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate/animationdidend(_:))*