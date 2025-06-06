# duration

**Framework**: UIKit  
**Kind**: property

The overall duration (in seconds) of the transition animation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var duration: CGFloat { get }
```

#### Discussion

This property reflects the duration of the transition animation if it were to occur without user interactions. It is obtained from the standard animator object returned by your delegate. The actual duration can vary depending on the user interactions you are tracking and responding to.

## See Also

- [func transitionDuration(using: (any UIViewControllerContextTransitioning)?) -> TimeInterval](uiviewcontrolleranimatedtransitioning/transitionduration(using:).md)
  Asks your animator object for the duration (in seconds) of the transition animation.
- [var timingCurve: (any UITimingCurveProvider)?](uipercentdriveninteractivetransition/timingcurve.md)
  The timing curve to use when driving the animations.
- [var completionCurve: UIView.AnimationCurve](uipercentdriveninteractivetransition/completioncurve.md)
  Indicates the animation completion curve for an interactive transition.
- [var percentComplete: CGFloat](uipercentdriveninteractivetransition/percentcomplete.md)
  The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [var completionSpeed: CGFloat](uipercentdriveninteractivetransition/completionspeed.md)
  The speed of the transition animation.
- [var wantsInteractiveStart: Bool](uipercentdriveninteractivetransition/wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/duration)*