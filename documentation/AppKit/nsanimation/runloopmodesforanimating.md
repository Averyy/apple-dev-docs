# runLoopModesForAnimating

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of strings representing the run loop modes in which the animation can run.

**Availability**:
- macOS

## Declaration

```swift
var runLoopModesForAnimating: [RunLoop.Mode]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSString *> * runLoopModesForAnimating;
```

## Discussion

The default value of this property is `nil`, which indicates that the animation can be run in the default, modal, or event-tracking modes. The value of this property is ignored if the animation blocking mode is something other than [`NSAnimation.BlockingMode.nonblocking`](./blockingmode/nonblocking.md).

For information about run loop modes and for constants, see [`RunLoop`](../../Foundation/runloop.md).

## See Also

### Configuring an Animation
- [var animationBlockingMode: NSAnimation.BlockingMode](./animationblockingmode.md)
  The blocking mode of the animation.
- [var animationCurve: NSAnimation.Curve](./animationcurve.md)
  The timing curve for the animation.
- [var duration: TimeInterval](./duration.md)
  The duration of the animation, in seconds.
- [var frameRate: Float](./framerate.md)
  The number of frame updates per second to generate for the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/runloopmodesforanimating)*