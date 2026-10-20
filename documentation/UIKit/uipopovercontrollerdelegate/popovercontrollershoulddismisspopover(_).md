# popoverControllerShouldDismissPopover(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the popover should be dismissed.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

## Declaration

```swift
optional func popoverControllerShouldDismissPopover(_ popoverController: UIPopoverController) -> Bool
```

```objc
- (BOOL) popoverControllerShouldDismissPopover:(UIPopoverController *) popoverController;
```

#### Return Value

[`true`](../../Swift/true.md) if the popover should be dismissed or [`false`](../../Swift/false.md) if it should remain visible.

#### Discussion

This method is called in response to user-initiated attempts to dismiss the popover. It is not called when you dismiss the popover using the [`dismiss(animated:)`](../uipopovercontroller/dismiss%28animated%29.md) method of the popover controller.

If you do not implement this method in your delegate, the default return value is assumed to be [`true`](../../Swift/true.md).

## Parameters

- `popoverController`: The popover controller to be dismissed.

## See Also

### Deprecated
- [func popoverController(UIPopoverController, willRepositionPopoverTo: UnsafeMutablePointer<CGRect>, in: AutoreleasingUnsafeMutablePointer<UIView>)](./popovercontroller%28_,willrepositionpopoverto,in%29.md)
  Tells the delegate that the popover controller needs to change the popover’s location in its view.
- [func popoverControllerDidDismissPopover(UIPopoverController)](./popovercontrollerdiddismisspopover%28_%29.md)
  Tells the delegate that the popover was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontrollershoulddismisspopover(_:))*