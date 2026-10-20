# animationShouldStart(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate just after an animation is started.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
optional func animationShouldStart(_ animation: NSAnimation) -> Bool
```

```objc
- (BOOL) animationShouldStart:(NSAnimation *) animation;
```

#### Return Value

[`false`](../../Swift/false.md) to cancel the animation, [`true`](../../Swift/true.md) to have the animation proceed.

#### Discussion

The delegate is sent this message just after `animation` receives a [`start()`](../nsanimation/start%28%29.md) message. The delegate can use this method to prepare objects and resources for the effect.

## Parameters

- `animation`: The `NSAnimation` object that was just started.

## See Also

### Controlling and Monitoring an Animation
- [func animationDidEnd(NSAnimation)](./animationdidend%28_%29.md)
  Sent to the delegate when the specified animation completes its run.
- [func animationDidStop(NSAnimation)](./animationdidstop%28_%29.md)
  Sent to the delegate when the specified animation is stopped before it completes its run.
- [func animation(NSAnimation, valueForProgress: NSAnimation.Progress) -> Float](./animation%28_,valueforprogress%29.md)
  Requests a custom curve value for the current progress value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate/animationshouldstart(_:))*