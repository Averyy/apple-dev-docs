# animationDidStop(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when the specified animation is stopped before it completes its run.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
optional func animationDidStop(_ animation: NSAnimation)
```

```objc
- (void) animationDidStop:(NSAnimation *) animation;
```

#### Discussion

An `NSAnimation` object stops running when it receives a [`stop()`](../nsanimation/stop%28%29.md) message.

## Parameters

- `animation`: The `NSAnimation` instance that was stopped.

## See Also

### Controlling and Monitoring an Animation
- [func animationDidEnd(NSAnimation)](./animationdidend%28_%29.md)
  Sent to the delegate when the specified animation completes its run.
- [func animationShouldStart(NSAnimation) -> Bool](./animationshouldstart%28_%29.md)
  Sent to the delegate just after an animation is started.
- [func animation(NSAnimation, valueForProgress: NSAnimation.Progress) -> Float](./animation%28_,valueforprogress%29.md)
  Requests a custom curve value for the current progress value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate/animationdidstop(_:))*