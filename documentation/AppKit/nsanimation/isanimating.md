# isAnimating

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the animation is in progress.

**Availability**:
- macOS ?+

## Declaration

```swift
var isAnimating: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the animation is in progress or [`false`](https://developer.apple.com/documentation/swift/false) when it is stopped.

## See Also

- [func start()](nsanimation/start.md)
  Starts the animation represented by the receiver.
- [func stop()](nsanimation/stop.md)
  Stops the animation represented by the receiver.
- [var currentProgress: NSAnimation.Progress](nsanimation/currentprogress.md)
  The current progress of the animation.
- [var currentValue: Float](nsanimation/currentvalue.md)
  The current value of the animation effect, based on the current progress


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/isanimating)*