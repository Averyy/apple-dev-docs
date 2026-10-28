# currentValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current value of the animation effect, based on the current progress

**Availability**:
- macOS

## Declaration

```swift
var currentValue: Float { get }
```

```objc
@property (readonly) float currentValue;
```

## Discussion

An `NSAnimation` object gets the current value from delegate’s [`animation(_:valueForProgress:)`](../nsanimationdelegate/animation%28_,valueforprogress%29.md) method. If that method is not implemented, the animation computes the current value from the current progress by factoring in the animation curve. An animation object does not access this property directly. Instances of `NSAnimation` subclasses or other objects can invoke this method on a periodic basis to get the current value.

Subclasses may override this property and return a custom curve value instead of implementing [`animation(_:valueForProgress:)`](../nsanimationdelegate/animation%28_,valueforprogress%29.md), thereby saving on the overhead of using a delegate. The current value can be less than `0.0` or greater than `1.0`. For example, if you make the value greater than `1.0` you can achieve a “rubber effect” where the size of a view is temporarily larger before its final size.

## See Also

### Related Documentation
- [var animationCurve: NSAnimation.Curve](./animationcurve.md)
  The timing curve for the animation.
### Controlling and Monitoring an Animation
- [func start()](./start%28%29.md)
  Starts the animation represented by the receiver.
- [func stop()](./stop%28%29.md)
  Stops the animation represented by the receiver.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value indicating whether the animation is in progress.
- [var currentProgress: NSAnimation.Progress](./currentprogress.md)
  The current progress of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimation/currentvalue)*