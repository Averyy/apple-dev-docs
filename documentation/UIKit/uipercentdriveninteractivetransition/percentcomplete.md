# percentComplete

**Framework**: UIKit  
**Kind**: property

The amount of the transition (specified as a percentage of the overall duration) that’s complete.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var percentComplete: CGFloat { get }
```

#### Discussion

The value in this property reflects the last value passed to the [`update(_:)`](uipercentdriveninteractivetransition/update(_:).md) method.

## See Also

- [func update(CGFloat)](uipercentdriveninteractivetransition/update(_:).md)
  Updates the completion percentage of the transition.
- [var timingCurve: (any UITimingCurveProvider)?](uipercentdriveninteractivetransition/timingcurve.md)
  The timing curve to use when driving the animations.
- [var completionCurve: UIView.AnimationCurve](uipercentdriveninteractivetransition/completioncurve.md)
  Indicates the animation completion curve for an interactive transition.
- [var duration: CGFloat](uipercentdriveninteractivetransition/duration.md)
  The overall duration (in seconds) of the transition animation.
- [var completionSpeed: CGFloat](uipercentdriveninteractivetransition/completionspeed.md)
  The speed of the transition animation.
- [var wantsInteractiveStart: Bool](uipercentdriveninteractivetransition/wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/percentcomplete)*