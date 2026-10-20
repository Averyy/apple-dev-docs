# animation(_:valueForProgress:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests a custom curve value for the current progress value.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
optional func animation(_ animation: NSAnimation, valueForProgress progress: NSAnimation.Progress) -> Float
```

```objc
- (float) animation:(NSAnimation *) animation valueForProgress:(NSAnimationProgress) progress;
```

#### Return Value

A `float` value representing a custom curve.

#### Discussion

The delegate can compute and return a custom curve value for the given progress value.  If the delegate does not implement this method, `NSAnimation` computes the current curve value.

The animation:valueForProgress: message is sent to the delegate when an `NSAnimation` object receives a [`currentValue`](../nsanimation/currentvalue.md) message. The value the delegate returns is used as the value of [`currentValue`](../nsanimation/currentvalue.md); if there is no delegate, or it doesn’t implement animation:valueForProgress:, `NSAnimation` computes and returns the current value. `NSAnimation` does not invoke [`currentValue`](../nsanimation/currentvalue.md)itself, but subclasses might.

See the description of [`currentValue`](../nsanimation/currentvalue.md) for more information.

## Parameters

- `animation`: An `NSAnimation` object that is running.
- `progress`: A `float` value (typed as `NSAnimationProgress`) that indicates a progress mark of `animation`. This value is always between 0.0 and 1.0.

## See Also

### Related Documentation
- [var currentValue: Float](../nsanimation/currentvalue.md)
  The current value of the animation effect, based on the current progress
### Controlling and Monitoring an Animation
- [func animationDidEnd(NSAnimation)](./animationdidend%28_%29.md)
  Sent to the delegate when the specified animation completes its run.
- [func animationDidStop(NSAnimation)](./animationdidstop%28_%29.md)
  Sent to the delegate when the specified animation is stopped before it completes its run.
- [func animationShouldStart(NSAnimation) -> Bool](./animationshouldstart%28_%29.md)
  Sent to the delegate just after an animation is started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationdelegate/animation(_:valueforprogress:))*