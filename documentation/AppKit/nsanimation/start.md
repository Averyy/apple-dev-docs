# start()

**Framework**: AppKit  
**Kind**: method

Starts the animation represented by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func start()
```

#### Discussion

A strong reference to the animation is maintained until the end of the animation or until its [`stop()`](nsanimation/stop().md) method is called. If the blocking mode is [`NSAnimation.BlockingMode.blocking`](nsanimation/blockingmode/blocking.md), this method returns after the animation has completed or the delegate sends it [`stop()`](nsanimation/stop().md). If the receiver has a progress of `1.0`, it starts again at `0.0`.

## See Also

- [func start(when: NSAnimation, reachesProgress: NSAnimation.Progress)](nsanimation/start(when:reachesprogress:).md)
  Starts running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func stop()](nsanimation/stop.md)
  Stops the animation represented by the receiver.
- [var isAnimating: Bool](nsanimation/isanimating.md)
  A Boolean value indicating whether the animation is in progress.
- [var currentProgress: NSAnimation.Progress](nsanimation/currentprogress.md)
  The current progress of the animation.
- [var currentValue: Float](nsanimation/currentvalue.md)
  The current value of the animation effect, based on the current progress


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/start())*