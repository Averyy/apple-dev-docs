# stop()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stops the animation represented by the receiver.

**Availability**:
- macOS

## Declaration

```swift
func stop()
```

```objc
- (void) stopAnimation;
```

#### Discussion

The current progress of the receiver is not reset.  When this method is sent to instances of [`NSViewAnimation`](../nsviewanimation.md) (a subclass of `NSAnimation`) the receiver moves to the end frame location.

## See Also

### Related Documentation
- [func stop(when: NSAnimation, reachesProgress: NSAnimation.Progress)](./stop%28when,reachesprogress%29.md)
  Stops running the animation represented by the receiver when another animation reaches a specific progress mark.
### Controlling and Monitoring an Animation
- [func start()](./start%28%29.md)
  Starts the animation represented by the receiver.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value indicating whether the animation is in progress.
- [var currentProgress: NSAnimation.Progress](./currentprogress.md)
  The current progress of the animation.
- [var currentValue: Float](./currentvalue.md)
  The current value of the animation effect, based on the current progress


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/stop())*