# pause()

**Framework**: UIKit  
**Kind**: method

Pauses an interruptible transition animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func pause()
```

#### Discussion

This is a convenience method that calls through to the [`pauseInteractiveTransition()`](uiviewcontrollercontexttransitioning/pauseinteractivetransition().md) method of the context object. You might call this method so that you can begin driving an animation interactively. For example, when the user’s finger touches the screen, your gesture handler would call this method to stop the animation and then use changes to the touch location to update the [`percentComplete`](uipercentdriveninteractivetransition/percentcomplete.md) property.

## See Also

- [func update(CGFloat)](uipercentdriveninteractivetransition/update(_:).md)
  Updates the completion percentage of the transition.
- [func cancel()](uipercentdriveninteractivetransition/cancel.md)
  Notifies the system that user interactions canceled the transition.
- [func finish()](uipercentdriveninteractivetransition/finish.md)
  Notifies the system that user interactions signaled the completion of the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/pause())*