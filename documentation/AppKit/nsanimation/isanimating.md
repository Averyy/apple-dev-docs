# isAnimating

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the animation is in progress.

**Availability**:
- macOS

## Declaration

```swift
var isAnimating: Bool { get }
```

```objc
@property (readonly, getter=isAnimating) BOOL animating;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the animation is in progress or [`false`](../../Swift/false.md) when it is stopped.

## See Also

### Controlling and Monitoring an Animation
- [func start()](./start%28%29.md)
  Starts the animation represented by the receiver.
- [func stop()](./stop%28%29.md)
  Stops the animation represented by the receiver.
- [var currentProgress: NSAnimation.Progress](./currentprogress.md)
  The current progress of the animation.
- [var currentValue: Float](./currentvalue.md)
  The current value of the animation effect, based on the current progress


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/isanimating)*