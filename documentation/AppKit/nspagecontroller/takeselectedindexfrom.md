# takeSelectedIndexFrom(_:)

**Framework**: AppKit  
**Kind**: method

Navigates to the selected index, which is taken from the sender.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func takeSelectedIndexFrom(_ sender: Any?)
```

#### Discussion

When invoked, this method causes the page controller’s view to display the object specified by the value taken from the `sender` control.

This method is animated and invokes the delegate’s [`pageControllerWillStartLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md) and [`pageControllerDidEndLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md) methods.

## Parameters

- `sender`: The control that invoked the action.

## See Also

- [func navigateForward(to: Any)](nspagecontroller/navigateforward(to:).md)
  Navigates to the specific object.
- [func navigateBack(Any?)](nspagecontroller/navigateback(_:).md)
  Navigates backwards in the page controller’s arranged objects array.
- [func navigateForward(Any?)](nspagecontroller/navigateforward(_:).md)
  Navigates to the next object in the page controller’s arranged objects array, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/takeselectedindexfrom(_:))*