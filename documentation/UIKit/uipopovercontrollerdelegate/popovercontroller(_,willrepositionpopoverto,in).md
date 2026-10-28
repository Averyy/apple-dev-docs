# popoverController(_:willRepositionPopoverTo:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the popover controller needs to change the popover’s location in its view.

**Availability**:
- iOS 7.0+ - Deprecated in 9.0
- iPadOS 7.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

## Declaration

```swift
optional func popoverController(_ popoverController: UIPopoverController, willRepositionPopoverTo rect: UnsafeMutablePointer<CGRect>, in view: AutoreleasingUnsafeMutablePointer<UIView>)
```

```objc
- (void) popoverController:(UIPopoverController *) popoverController willRepositionPopoverToRect:(CGRect *) rect inView:(UIView **) view;
```

## Discussion

For popovers that were presented using the [`present(from:in:permittedArrowDirections:animated:)`](../uipopovercontroller/present%28from,in,permittedarrowdirections,animated%29.md) method, the popover controller calls this method when the interface orientation changes. Your delegate can use this method to adjust the proposed position of the popover. The popover controller does not call this method if you presented the popover from a bar button item.

## Parameters

- `popoverController`: The popover controller changing the position of its content.
- `rect`: On input, the proposed rectangle for the popover. This popover is in the coordinate space of the view in the `view` parameter. If you want to propose a different rectangle for the popover, put the new value in this parameter.
- `view`: On input, the proposed view for containing the popover. If you want to propose a different view for the popover, put the new view in this parameter.

## See Also

### Deprecated
- [func popoverControllerShouldDismissPopover(UIPopoverController) -> Bool](./popovercontrollershoulddismisspopover%28_%29.md)
  Asks the delegate if the popover should be dismissed.
- [func popoverControllerDidDismissPopover(UIPopoverController)](./popovercontrollerdiddismisspopover%28_%29.md)
  Tells the delegate that the popover was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate/popovercontroller(_:willrepositionpopoverto:in:))*