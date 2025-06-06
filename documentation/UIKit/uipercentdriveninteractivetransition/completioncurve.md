# completionCurve

**Framework**: UIKit  
**Kind**: property

Indicates the animation completion curve for an interactive transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var completionCurve: UIView.AnimationCurve { get set }
```

#### Discussion

When the interactive part of a view controller transition is complete, you can set this property to indicate a desired animation completion curve. Default value is [`UIView.AnimationCurve.easeInOut`](uiview/animationcurve/easeinout.md).

During the interactive portion of a view controller transition, the animation curve is linear.

## See Also

- [var timingCurve: (any UITimingCurveProvider)?](uipercentdriveninteractivetransition/timingcurve.md)
  The timing curve to use when driving the animations.
- [var duration: CGFloat](uipercentdriveninteractivetransition/duration.md)
  The overall duration (in seconds) of the transition animation.
- [var percentComplete: CGFloat](uipercentdriveninteractivetransition/percentcomplete.md)
  The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [var completionSpeed: CGFloat](uipercentdriveninteractivetransition/completionspeed.md)
  The speed of the transition animation.
- [var wantsInteractiveStart: Bool](uipercentdriveninteractivetransition/wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/completioncurve)*