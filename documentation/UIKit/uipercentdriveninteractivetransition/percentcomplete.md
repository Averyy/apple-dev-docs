# percentComplete

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The amount of the transition (specified as a percentage of the overall duration) that’s complete.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var percentComplete: CGFloat { get }
```

```objc
@property (readonly) CGFloat percentComplete;
```

#### Discussion

The value in this property reflects the last value passed to the [`update(_:)`](./update%28_%29.md) method.

## See Also

### Related Documentation
- [func update(CGFloat)](./update%28_%29.md)
  Updates the completion percentage of the transition.
### Accessing transition attributes
- [var timingCurve: (any UITimingCurveProvider)?](./timingcurve.md)
  The timing curve to use when driving the animations.
- [var completionCurve: UIView.AnimationCurve](./completioncurve.md)
  Indicates the animation completion curve for an interactive transition.
- [var duration: CGFloat](./duration.md)
  The overall duration (in seconds) of the transition animation.
- [var completionSpeed: CGFloat](./completionspeed.md)
  The speed of the transition animation.
- [var wantsInteractiveStart: Bool](./wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/percentcomplete)*