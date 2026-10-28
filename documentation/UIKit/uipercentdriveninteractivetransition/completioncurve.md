# completionCurve

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Indicates the animation completion curve for an interactive transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var completionCurve: UIView.AnimationCurve { get set }
```

```objc
@property (nonatomic, assign) UIViewAnimationCurve completionCurve;
```

## Discussion

When the interactive part of a view controller transition is complete, you can set this property to indicate a desired animation completion curve. Default value is [`UIView.AnimationCurve.easeInOut`](../uiview/animationcurve/easeinout.md).

During the interactive portion of a view controller transition, the animation curve is linear.

## See Also

### Accessing transition attributes
- [var timingCurve: (any UITimingCurveProvider)?](./timingcurve.md)
  The timing curve to use when driving the animations.
- [var duration: CGFloat](./duration.md)
  The overall duration (in seconds) of the transition animation.
- [var percentComplete: CGFloat](./percentcomplete.md)
  The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [var completionSpeed: CGFloat](./completionspeed.md)
  The speed of the transition animation.
- [var wantsInteractiveStart: Bool](./wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/completioncurve)*