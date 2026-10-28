# pageControllerWillStartLiveTransition(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This message is sent when the user begins a transition.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageControllerWillStartLiveTransition(_ pageController: NSPageController)
```

```objc
- (void) pageControllerWillStartLiveTransition:(NSPageController *) pageController;
```

## Discussion

This message is sent when the user begins a transition whether via a swipe gesture of one of the page controller’s target-action navigation methods.

## Parameters

- `pageController`: The page controller.

## See Also

### Transition Notification
- [func pageControllerDidEndLiveTransition(NSPageController)](./pagecontrollerdidendlivetransition%28_%29.md)
  This message is sent when a transition animation completes.
- [func pageController(NSPageController, didTransitionTo: Any)](./pagecontroller%28_,didtransitionto%29.md)
  This message is sent when any page transition is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:))*