# popoverControllerShouldDismissPopover(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the popover should be dismissed.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
optional func popoverControllerShouldDismissPopover(_ popoverController: UIPopoverController) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the popover should be dismissed or [`false`](https://developer.apple.com/documentation/swift/false) if it should remain visible.

#### Discussion

This method is called in response to user-initiated attempts to dismiss the popover. It is not called when you dismiss the popover using the [`dismiss(animated:)`](uipopovercontroller/dismiss(animated:).md) method of the popover controller.

If you do not implement this method in your delegate, the default return value is assumed to be [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `popoverController`: The popover controller to be dismissed.

## See Also

- [func popoverControllerDidDismissPopover(UIPopoverController)](uipopovercontrollerdelegate/popovercontrollerdiddismisspopover(_:).md)
  Tells the delegate that the popover was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontrollershoulddismisspopover(_:))*