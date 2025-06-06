# popoverControllerDidDismissPopover(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the popover was dismissed.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func popoverControllerDidDismissPopover(_ popoverController: UIPopoverController)
```

#### Discussion

The popover controller does not call this method in response to programmatic calls to the [`dismiss(animated:)`](uipopovercontroller/dismiss(animated:).md) method. If you dismiss the popover programmatically, you should perform any cleanup actions immediately after calling the [`dismiss(animated:)`](uipopovercontroller/dismiss(animated:).md) method.

You can use this method to incorporate any changes from the popover’s content view controller back into your application. If you do not plan to use the object in the `popoverController` parameter again, it is safe to release it from this method.

## Parameters

- `popoverController`: The popover controller that was dismissed.

## See Also

- [func popoverControllerShouldDismissPopover(UIPopoverController) -> Bool](uipopovercontrollerdelegate/popovercontrollershoulddismisspopover(_:).md)
  Asks the delegate if the popover should be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontrollerdiddismisspopover(_:))*