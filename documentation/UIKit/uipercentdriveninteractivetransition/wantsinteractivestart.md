# wantsInteractiveStart

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the animations are interactive initially.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var wantsInteractiveStart: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), interactive animations start as paused, allowing you to drive the animations yourself from the start. You might set this property to [`false`](https://developer.apple.com/documentation/Swift/false) when you want to start your animations without interactivity. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var timingCurve: (any UITimingCurveProvider)?](uipercentdriveninteractivetransition/timingcurve.md)
  The timing curve to use when driving the animations.
- [var completionCurve: UIView.AnimationCurve](uipercentdriveninteractivetransition/completioncurve.md)
  Indicates the animation completion curve for an interactive transition.
- [var duration: CGFloat](uipercentdriveninteractivetransition/duration.md)
  The overall duration (in seconds) of the transition animation.
- [var percentComplete: CGFloat](uipercentdriveninteractivetransition/percentcomplete.md)
  The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [var completionSpeed: CGFloat](uipercentdriveninteractivetransition/completionspeed.md)
  The speed of the transition animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/wantsinteractivestart)*