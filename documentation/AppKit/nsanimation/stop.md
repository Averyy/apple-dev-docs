# stop()

**Framework**: AppKit  
**Kind**: method

Stops the animation represented by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func stop()
```

#### Discussion

The current progress of the receiver is not reset.  When this method is sent to instances of [`NSViewAnimation`](nsviewanimation.md) (a subclass of `NSAnimation`) the receiver moves to the end frame location.

## See Also

- [func stop(when: NSAnimation, reachesProgress: NSAnimation.Progress)](nsanimation/stop(when:reachesprogress:).md)
  Stops running the animation represented by the receiver when another animation reaches a specific progress mark.
- [func start()](nsanimation/start.md)
  Starts the animation represented by the receiver.
- [var isAnimating: Bool](nsanimation/isanimating.md)
  A Boolean value indicating whether the animation is in progress.
- [var currentProgress: NSAnimation.Progress](nsanimation/currentprogress.md)
  The current progress of the animation.
- [var currentValue: Float](nsanimation/currentvalue.md)
  The current value of the animation effect, based on the current progress


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/stop())*