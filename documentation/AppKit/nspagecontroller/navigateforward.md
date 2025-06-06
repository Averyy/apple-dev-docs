# navigateForward(_:)

**Framework**: AppKit  
**Kind**: method

Navigates to the next object in the page controller’s arranged objects array, if appropriate.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func navigateForward(_ sender: Any?)
```

#### Discussion

This method is typically invoked in response to a user interacting with a control, the `sender`.

This method is animated and invokes the delegate’s [`pageControllerWillStartLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md) and [`pageControllerDidEndLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md) methods.

## Parameters

- `sender`: The sender.

## See Also

- [func navigateForward(to: Any)](nspagecontroller/navigateforward(to:).md)
  Navigates to the specific object.
- [func navigateBack(Any?)](nspagecontroller/navigateback(_:).md)
  Navigates backwards in the page controller’s arranged objects array.
- [func takeSelectedIndexFrom(Any?)](nspagecontroller/takeselectedindexfrom(_:).md)
  Navigates to the selected index, which is taken from the sender.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontroller/navigateforward(_:))*