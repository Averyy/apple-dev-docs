# animationCurve

**Framework**: AppKit  
**Kind**: property

The timing curve for the animation.

**Availability**:
- macOS ?+

## Declaration

```swift
var animationCurve: NSAnimation.Curve { get set }
```

#### Discussion

The animation curve describes the relative frame rate over the course of the animation; predefined curves are linear, ease in (slow down near end), ease out (slowly speed up at start), and ease in-ease out (S-curve). Changing the value of this property changes the timing of an in-progress animation. The value of this property is ignored if the delegate implements the [`animation(_:valueForProgress:)`](nsanimationdelegate/animation(_:valueforprogress:).md) method.

Setting this property to an invalid value raises an exception. For a list of valid animation values, see [`NSAnimation.Curve`](nsanimation/curve.md).

## See Also

- [var animationBlockingMode: NSAnimation.BlockingMode](nsanimation/animationblockingmode.md)
  The blocking mode of the animation.
- [var runLoopModesForAnimating: [RunLoop.Mode]?](nsanimation/runloopmodesforanimating.md)
  An array of strings representing the run loop modes in which the animation can run.
- [var duration: TimeInterval](nsanimation/duration.md)
  The duration of the animation, in seconds.
- [var frameRate: Float](nsanimation/framerate.md)
  The number of frame updates per second to generate for the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/animationcurve)*