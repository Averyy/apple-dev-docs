# UIPercentDrivenInteractiveTransition

**Framework**: UIKit  
**Kind**: class

An object that drives an interactive animation between one view controller and another.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPercentDrivenInteractiveTransition
```

#### Overview

A percent-driven interactive transition object relies on a transition animator delegate—a custom object that adopts the [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) protocol—to set up and perform the animations.

To use this concrete class, return an instance of it from your view controller delegate when asked for an interactive transition controller. As user events arrive that would affect the progress of a transition, call the [`update(_:)`](uipercentdriveninteractivetransition/update(_:).md), [`cancel()`](uipercentdriveninteractivetransition/cancel().md), and [`finish()`](uipercentdriveninteractivetransition/finish().md) methods to reflect the current progress. For example, you might call these methods from a gesture recognizer to reflect how much of the gesture is completed.

You can subclass [`UIPercentDrivenInteractiveTransition`](uipercentdriveninteractivetransition.md), but if you do so you must start each of your method overrides with a call to the `super` implementation of the method.

## Topics

### Accessing transition attributes
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
- [var wantsInteractiveStart: Bool](uipercentdriveninteractivetransition/wantsinteractivestart.md)
  A Boolean value indicating whether the animations are interactive initially.
### Managing a transition
- [func update(CGFloat)](uipercentdriveninteractivetransition/update(_:).md)
  Updates the completion percentage of the transition.
- [func pause()](uipercentdriveninteractivetransition/pause.md)
  Pauses an interruptible transition animation.
- [func cancel()](uipercentdriveninteractivetransition/cancel.md)
  Notifies the system that user interactions canceled the transition.
- [func finish()](uipercentdriveninteractivetransition/finish.md)
  Notifies the system that user interactions signaled the completion of the transition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md)

## See Also

- [protocol UIViewControllerInteractiveTransitioning](uiviewcontrollerinteractivetransitioning.md)
  A set of methods that enable an object (such as a navigation controller) to drive a view controller transition.
- [protocol UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md)
  An interface for modifying an animation while it’s running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition)*