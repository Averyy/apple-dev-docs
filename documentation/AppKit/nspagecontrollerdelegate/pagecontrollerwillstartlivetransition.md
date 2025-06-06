# pageControllerWillStartLiveTransition(_:)

**Framework**: AppKit  
**Kind**: method

This message is sent when the user begins a transition.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageControllerWillStartLiveTransition(_ pageController: NSPageController)
```

#### Discussion

This message is sent when the user begins a transition whether via a swipe gesture of one of the page controller’s target-action navigation methods.

## Parameters

- `pageController`: The page controller.

## See Also

- [func pageControllerDidEndLiveTransition(NSPageController)](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md)
  This message is sent when a transition animation completes.
- [func pageController(NSPageController, didTransitionTo: Any)](nspagecontrollerdelegate/pagecontroller(_:didtransitionto:).md)
  This message is sent when any page transition is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:))*