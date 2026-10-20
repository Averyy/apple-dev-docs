# pageControllerDidEndLiveTransition(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This message is sent when a transition animation completes.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageControllerDidEndLiveTransition(_ pageController: NSPageController)
```

```objc
- (void) pageControllerDidEndLiveTransition:(NSPageController *) pageController;
```

#### Discussion

This message is sent when a transition animation completes either via swipe gesture or one of the page controller’s target-action navigation methods.

Your content view is still hidden and you must call the [`completeTransition()`](../nspagecontroller/completetransition%28%29.md) method on `pageController` when your content is ready to show.

If completed successfully, a [`pageController(_:didTransitionTo:)`](./pagecontroller%28_,didtransitionto%29.md) will already have been sent.

## Parameters

- `pageController`: The page controller.

## See Also

### Transition Notification
- [func pageControllerWillStartLiveTransition(NSPageController)](./pagecontrollerwillstartlivetransition%28_%29.md)
  This message is sent when the user begins a transition.
- [func pageController(NSPageController, didTransitionTo: Any)](./pagecontroller%28_,didtransitionto%29.md)
  This message is sent when any page transition is completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:))*