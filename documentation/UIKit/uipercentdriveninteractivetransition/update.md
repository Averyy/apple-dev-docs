# update(_:)

**Framework**: UIKit  
**Kind**: method

Updates the completion percentage of the transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func update(_ percentComplete: CGFloat)
```

#### Discussion

This is a convenience method that calls through to the [`updateInteractiveTransition(_:)`](uiviewcontrollercontexttransitioning/updateinteractivetransition(_:).md) method of the context object.

While tracking user events, your code should call this method regularly to update the current progress toward completing the transition. If, during tracking, the interactions cross a threshold that you consider signifies the completion or cancellation of the transition, stop tracking events and call the [`finish()`](uipercentdriveninteractivetransition/finish().md) or [`cancel()`](uipercentdriveninteractivetransition/cancel().md) method.

## Parameters

- `percentComplete`: The percentage of the transition that is currently complete, specified as a floating-point number in the range   to  . If you specify a value less than  , this method changes it to  . Specifying a value greater than   would cause the animation to appear complete already.

## See Also

- [func pause()](uipercentdriveninteractivetransition/pause.md)
  Pauses an interruptible transition animation.
- [func cancel()](uipercentdriveninteractivetransition/cancel.md)
  Notifies the system that user interactions canceled the transition.
- [func finish()](uipercentdriveninteractivetransition/finish.md)
  Notifies the system that user interactions signaled the completion of the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/update(_:))*