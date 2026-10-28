# duration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The overall duration (in seconds) of the transition animation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var duration: CGFloat { get }
```

```objc
@property (readonly) CGFloat duration;
```

## Discussion

This property reflects the duration of the transition animation if it were to occur without user interactions. It is obtained from the standard animator object returned by your delegate. The actual duration can vary depending on the user interactions you are tracking and responding to.

## See Also

### Related Documentation
- [func transitionDuration(using: (any UIViewControllerContextTransitioning)?) -> TimeInterval](../uiviewcontrolleranimatedtransitioning/transitionduration%28using%29.md)
  Asks your animator object for the duration (in seconds) of the transition animation.
### Accessing transition attributes
- [var timingCurve: (any UITimingCurveProvider)?](./timingcurve.md)
  The timing curve to use when driving the animations.
- [var completionCurve: UIView.AnimationCurve](./completioncurve.md)
  Indicates the animation completion curve for an interactive transition.
- [var percentComplete: CGFloat](./percentcomplete.md)
  The amount of the transition (specified as a percentage of the overall duration) that’s complete.
- [var completionSpeed: CGFloat](./completionspeed.md)
  The speed of the transition animation.
- [var wantsInteractiveStart: Bool](./wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/duration)*