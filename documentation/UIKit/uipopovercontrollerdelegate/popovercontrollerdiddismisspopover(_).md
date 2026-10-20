# popoverControllerDidDismissPopover(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the popover was dismissed.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

## Declaration

```swift
optional func popoverControllerDidDismissPopover(_ popoverController: UIPopoverController)
```

```objc
- (void) popoverControllerDidDismissPopover:(UIPopoverController *) popoverController;
```

#### Discussion

The popover controller does not call this method in response to programmatic calls to the [`dismiss(animated:)`](../uipopovercontroller/dismiss%28animated%29.md) method. If you dismiss the popover programmatically, you should perform any cleanup actions immediately after calling the [`dismiss(animated:)`](../uipopovercontroller/dismiss%28animated%29.md) method.

You can use this method to incorporate any changes from the popover’s content view controller back into your application. If you do not plan to use the object in the `popoverController` parameter again, it is safe to release it from this method.

## Parameters

- `popoverController`: The popover controller that was dismissed.

## See Also

### Deprecated
- [func popoverController(UIPopoverController, willRepositionPopoverTo: UnsafeMutablePointer<CGRect>, in: AutoreleasingUnsafeMutablePointer<UIView>)](./popovercontroller%28_,willrepositionpopoverto,in%29.md)
  Tells the delegate that the popover controller needs to change the popover’s location in its view.
- [func popoverControllerShouldDismissPopover(UIPopoverController) -> Bool](./popovercontrollershoulddismisspopover%28_%29.md)
  Asks the delegate if the popover should be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontrollerdiddismisspopover(_:))*