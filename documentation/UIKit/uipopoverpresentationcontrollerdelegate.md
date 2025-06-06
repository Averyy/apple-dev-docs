# UIPopoverPresentationControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for a popover presentation delegate, which lets you customize the behavior of a popover-based presentation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIPopoverPresentationControllerDelegate : UIAdaptivePresentationControllerDelegate
```

#### Overview

A popover presentation controller notifies your delegate at appropriate points during the presentation process. You can use the delegate methods to customize this process and respond to changes dynamically.

After defining an object that adopts this protocol, assign that object to the [`delegate`](uipopoverpresentationcontroller/delegate.md) property of a [`UIPopoverPresentationController`](uipopoverpresentationcontroller.md) object. You must present a view controller using the [`UIModalPresentationStyle.popover`](uimodalpresentationstyle/popover.md) style before you can obtain such an object. For more information about popover presentation controllers, see [`UIPopoverPresentationController`](uipopoverpresentationcontroller.md).

## Topics

### Presenting and dismissing the popover
- [func prepareForPopoverPresentation(UIPopoverPresentationController)](uipopoverpresentationcontrollerdelegate/prepareforpopoverpresentation(_:).md)
  Notifies the delegate that the popover is about to be presented.
- [func popoverPresentationControllerShouldDismissPopover(UIPopoverPresentationController) -> Bool](uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollershoulddismisspopover(_:).md)
  Asks the delegate if the popover should be dismissed.
- [func popoverPresentationControllerDidDismissPopover(UIPopoverPresentationController)](uipopoverpresentationcontrollerdelegate/popoverpresentationcontrollerdiddismisspopover(_:).md)
  Tells the delegate that the popover was dismissed.
### Repositioning the popover
- [func popoverPresentationController(UIPopoverPresentationController, willRepositionPopoverTo: UnsafeMutablePointer<CGRect>, in: AutoreleasingUnsafeMutablePointer<UIView>)](uipopoverpresentationcontrollerdelegate/popoverpresentationcontroller(_:willrepositionpopoverto:in:).md)
  Tells the delegate that UIKit needs to reposition the popover’s location.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)

## See Also

- [var delegate: (any UIPopoverPresentationControllerDelegate)?](uipopoverpresentationcontroller/delegate.md)
  The delegate that handles popover-related messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontrollerdelegate)*