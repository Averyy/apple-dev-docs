# pageController(_:didTransitionTo:)

**Framework**: AppKit  
**Kind**: method

This message is sent when any page transition is completed.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageController(_ pageController: NSPageController, didTransitionTo object: Any)
```

## Parameters

- `pageController`: The page controller.
- `object`: The object to display.

## See Also

- [func pageControllerWillStartLiveTransition(NSPageController)](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md)
  This message is sent when the user begins a transition.
- [func pageControllerDidEndLiveTransition(NSPageController)](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md)
  This message is sent when a transition animation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontroller(_:didtransitionto:))*