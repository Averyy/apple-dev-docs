# pageController(_:didTransitionTo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This message is sent when any page transition is completed.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
optional func pageController(_ pageController: NSPageController, didTransitionTo object: Any)
```

```objc
- (void) pageController:(NSPageController *) pageController didTransitionToObject:(id) object;
```

## Parameters

- `pageController`: The page controller.
- `object`: The object to display.

## See Also

### Transition Notification
- [func pageControllerWillStartLiveTransition(NSPageController)](./pagecontrollerwillstartlivetransition%28_%29.md)
  This message is sent when the user begins a transition.
- [func pageControllerDidEndLiveTransition(NSPageController)](./pagecontrollerdidendlivetransition%28_%29.md)
  This message is sent when a transition animation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate/pagecontroller(_:didtransitionto:))*