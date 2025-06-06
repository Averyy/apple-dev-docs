# animationShouldStart(_:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate just after an animation is started.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
optional func animationShouldStart(_ animation: NSAnimation) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/swift/false) to cancel the animation, [`true`](https://developer.apple.com/documentation/swift/true) to have the animation proceed.

#### Discussion

The delegate is sent this message just after `animation` receives a [`start()`](nsanimation/start().md) message. The delegate can use this method to prepare objects and resources for the effect.

## Parameters

- `animation`: The   object that was just started.

## See Also

- [func animationDidEnd(NSAnimation)](nsanimationdelegate/animationdidend(_:).md)
  Sent to the delegate when the specified animation completes its run.
- [func animationDidStop(NSAnimation)](nsanimationdelegate/animationdidstop(_:).md)
  Sent to the delegate when the specified animation is stopped before it completes its run.
- [func animation(NSAnimation, valueForProgress: NSAnimation.Progress) -> Float](nsanimationdelegate/animation(_:valueforprogress:).md)
  Requests a custom curve value for the current progress value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate/animationshouldstart(_:))*