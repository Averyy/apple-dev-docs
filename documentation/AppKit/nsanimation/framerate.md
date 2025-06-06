# frameRate

**Framework**: AppKit  
**Kind**: property

The number of frame updates per second to generate for the animation.

**Availability**:
- macOS ?+

## Declaration

```swift
var frameRate: Float { get set }
```

#### Discussion

The value of this property must be greater than or equal to `0`. Specifying a value of `0.0` causes the animation to run as fast as possible. Setting the property to a negative value raises an exception.

The frame rate is not guaranteed due to differences among systems for the time needed to process a frame. You can change the frame rate while an animation is running and the new value is used at the next frame. The default frame rate is set to a reasonable value (which is subject to future change).

## See Also

- [var animationBlockingMode: NSAnimation.BlockingMode](nsanimation/animationblockingmode.md)
  The blocking mode of the animation.
- [var runLoopModesForAnimating: [RunLoop.Mode]?](nsanimation/runloopmodesforanimating.md)
  An array of strings representing the run loop modes in which the animation can run.
- [var animationCurve: NSAnimation.Curve](nsanimation/animationcurve.md)
  The timing curve for the animation.
- [var duration: TimeInterval](nsanimation/duration.md)
  The duration of the animation, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/framerate)*