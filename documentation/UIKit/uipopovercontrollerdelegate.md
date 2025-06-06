# UIPopoverControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for the delegate of a popover controller object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIPopoverControllerDelegate : NSObjectProtocol
```

#### Overview

Popover controllers notify their delegate whenever user interactions would cause the dismissal of the popover and, in some cases, give the user a chance to prevent that dismissal.

For more information about the [`UIPopoverController`](uipopovercontroller.md) class, see [`UIPopoverController`](uipopovercontroller.md).

## Topics

### Responding to popover position changes
- [func popoverController(UIPopoverController, willRepositionPopoverTo: UnsafeMutablePointer<CGRect>, in: AutoreleasingUnsafeMutablePointer<UIView>)](uipopovercontrollerdelegate/popovercontroller(_:willrepositionpopoverto:in:).md)
  Tells the delegate that the popover controller needs to change the popover’s location in its view.
### Managing the popover’s dismissal
- [func popoverControllerShouldDismissPopover(UIPopoverController) -> Bool](uipopovercontrollerdelegate/popovercontrollershoulddismisspopover(_:).md)
  Asks the delegate if the popover should be dismissed.
- [func popoverControllerDidDismissPopover(UIPopoverController)](uipopovercontrollerdelegate/popovercontrollerdiddismisspopover(_:).md)
  Tells the delegate that the popover was dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UIAccelerometerDelegate](uiaccelerometerdelegate.md)
  The interface for receiving acceleration-related data from the system.
- [protocol UIActionSheetDelegate](uiactionsheetdelegate.md)
  The interface for the delegate of an action sheet object.
- [protocol UIAlertViewDelegate](uialertviewdelegate.md)
  The interface for the delegate of an alert view object.
- [protocol UISearchDisplayDelegate](uisearchdisplaydelegate.md)
  The interface for the delegate of a search display controller.
- [protocol UIViewControllerPreviewing](uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.
- [protocol UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md)
  A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate)*