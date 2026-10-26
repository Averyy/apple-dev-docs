# UIPopoverControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for the delegate of a popover controller object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

> **Deprecated**: In iOS 9 and later, a popover is implemented as a [`UIViewController`](./uiviewcontroller.md) presentation. To create a popover, use [`UIPopoverPresentationController`](./uipopoverpresentationcontroller.md) and specify the [`UIModalPresentationStyle.popover`](./uimodalpresentationstyle/popover.md) style.

## Declaration

```swift
@MainActor
protocol UIPopoverControllerDelegate : NSObjectProtocol
```

```objc
@protocol UIPopoverControllerDelegate <NSObject>
```

#### Overview

Popover controllers notify their delegate whenever user interactions would cause the dismissal of the popover and, in some cases, give the user a chance to prevent that dismissal.

For more information about the [`UIPopoverController`](./uipopovercontroller.md) class, see [`UIPopoverController`](./uipopovercontroller.md).

## Topics

### Deprecated
- [func popoverController(UIPopoverController, willRepositionPopoverTo: UnsafeMutablePointer<CGRect>, in: AutoreleasingUnsafeMutablePointer<UIView>)](./uipopovercontrollerdelegate/popovercontroller%28_,willrepositionpopoverto,in%29.md)
  Tells the delegate that the popover controller needs to change the popover’s location in its view.
- [func popoverControllerShouldDismissPopover(UIPopoverController) -> Bool](./uipopovercontrollerdelegate/popovercontrollershoulddismisspopover%28_%29.md)
  Asks the delegate if the popover should be dismissed.
- [func popoverControllerDidDismissPopover(UIPopoverController)](./uipopovercontrollerdelegate/popovercontrollerdiddismisspopover%28_%29.md)
  Tells the delegate that the popover was dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated protocols
- [protocol UIActionSheetDelegate](./uiactionsheetdelegate.md)
  The interface for the delegate of an action sheet object.
- [protocol UIAlertViewDelegate](./uialertviewdelegate.md)
  The interface for the delegate of an alert view object.
- [protocol UISearchDisplayDelegate](./uisearchdisplaydelegate.md)
  The interface for the delegate of a search display controller.
- [protocol UIViewControllerPreviewing](./uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.
- [protocol UIViewControllerPreviewingDelegate](./uiviewcontrollerpreviewingdelegate.md)
  A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.
- [UIAccelerometerDelegate](./uiaccelerometerdelegate.md)
  The interface for receiving acceleration-related data from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontrollerdelegate)*