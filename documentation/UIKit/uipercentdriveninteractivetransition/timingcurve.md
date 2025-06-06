# timingCurve

**Framework**: UIKit  
**Kind**: property

The timing curve to use when driving the animations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var timingCurve: (any UITimingCurveProvider)? { get set }
```

## See Also

- [var completionCurve: UIView.AnimationCurve](uipercentdriveninteractivetransition/completioncurve.md)
  Indicates the animation completion curve for an interactive transition.
- [var duration: CGFloat](uipercentdriveninteractivetransition/duration.md)
  The overall duration (in seconds) of the transition animation.
- [var percentComplete: CGFloat](uipercentdriveninteractivetransition/percentcomplete.md)
  The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [var completionSpeed: CGFloat](uipercentdriveninteractivetransition/completionspeed.md)
  The speed of the transition animation.
- [var wantsInteractiveStart: Bool](uipercentdriveninteractivetransition/wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/timingcurve)*