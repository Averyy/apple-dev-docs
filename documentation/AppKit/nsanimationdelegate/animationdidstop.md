# animationDidStop(_:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate when the specified animation is stopped before it completes its run.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
optional func animationDidStop(_ animation: NSAnimation)
```

#### Discussion

An `NSAnimation` object stops running when it receives a [`stop()`](nsanimation/stop().md) message.

## Parameters

- `animation`: The   instance that was stopped.

## See Also

- [func animationDidEnd(NSAnimation)](nsanimationdelegate/animationdidend(_:).md)
  Sent to the delegate when the specified animation completes its run.
- [func animationShouldStart(NSAnimation) -> Bool](nsanimationdelegate/animationshouldstart(_:).md)
  Sent to the delegate just after an animation is started.
- [func animation(NSAnimation, valueForProgress: NSAnimation.Progress) -> Float](nsanimationdelegate/animation(_:valueforprogress:).md)
  Requests a custom curve value for the current progress value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate/animationdidstop(_:))*