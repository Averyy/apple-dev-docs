# start()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Starts the animation represented by the receiver.

**Availability**:
- macOS

## Declaration

```swift
func start()
```

```objc
- (void) startAnimation;
```

#### Discussion

A strong reference to the animation is maintained until the end of the animation or until its [`stop()`](./stop%28%29.md) method is called. If the blocking mode is [`NSAnimation.BlockingMode.blocking`](./blockingmode/blocking.md), this method returns after the animation has completed or the delegate sends it [`stop()`](./stop%28%29.md). If the receiver has a progress of `1.0`, it starts again at `0.0`.

## See Also

### Related Documentation
- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./start%28when,reachesprogress%29.md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
### Controlling and Monitoring an Animation
- [func stop()](./stop%28%29.md)
  Stops the animation represented by the receiver.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value indicating whether the animation is in progress.
- [var currentProgress: NSAnimation.Progress](./currentprogress.md)
  The current progress of the animation.
- [var currentValue: Float](./currentvalue.md)
  The current value of the animation effect, based on the current progress


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/start())*