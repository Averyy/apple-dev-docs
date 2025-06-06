# animationBlockingMode

**Framework**: AppKit  
**Kind**: property

The blocking mode of the animation.

**Availability**:
- macOS ?+

## Declaration

```swift
var animationBlockingMode: NSAnimation.BlockingMode { get set }
```

#### Discussion

The value in this property determines whether the animation blocks a given thread. The default value of this property is [`NSAnimation.BlockingMode.blocking`](nsanimation/blockingmode/blocking.md), which means that the animation runs on the main thread in a custom run-loop mode that blocks user events. When changing the value of this property, the new blocking mode takes effect the next time the animation is started and has no effect on an in-progress animation.

If you set the block mode to [`NSAnimation.BlockingMode.nonblocking`](nsanimation/blockingmode/nonblocking.md), the animation runs in the main thread in one of the standard run-loop modes or in a mode returned from [`NSAnimation`](nsanimation.md). If you set the mode to [`NSAnimation.BlockingMode.nonblockingThreaded`](nsanimation/blockingmode/nonblockingthreaded.md), a new thread is spawned to run the animation.

## See Also

- [var runLoopModesForAnimating: [RunLoop.Mode]?](nsanimation/runloopmodesforanimating.md)
  An array of strings representing the run loop modes in which the animation can run.
- [var animationCurve: NSAnimation.Curve](nsanimation/animationcurve.md)
  The timing curve for the animation.
- [var duration: TimeInterval](nsanimation/duration.md)
  The duration of the animation, in seconds.
- [var frameRate: Float](nsanimation/framerate.md)
  The number of frame updates per second to generate for the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/animationblockingmode)*