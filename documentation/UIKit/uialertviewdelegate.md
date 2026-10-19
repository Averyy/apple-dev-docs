# UIAlertViewDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for the delegate of an alert view object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
protocol UIAlertViewDelegate : NSObjectProtocol
```

#### Overview

The delegate implements the button actions and any other custom behavior. Some of the methods defined in this protocol are optional.

If you add your own buttons or customize the behavior of an alert view, implement a delegate conforming to this protocol to handle the corresponding delegate messages. Use the [`delegate`](uialertview/delegate.md) property of an alert view to specify one of your application objects as the delegate.

If you add your own buttons to an alert view, the delegate must implement the [`alertView(_:clickedButtonAt:)`](uialertviewdelegate/alertview(_:clickedbuttonat:).md) message to respond when those buttons are clicked; otherwise, your custom buttons do nothing. The alert view is automatically dismissed after the [`alertView(_:clickedButtonAt:)`](uialertviewdelegate/alertview(_:clickedbuttonat:).md) delegate method is invoked.

Optionally, you can implement the [`alertViewCancel(_:)`](uialertviewdelegate/alertviewcancel(_:).md) method to take the appropriate action when the system cancels your alert view. If the delegate doesn’t implement this method, the default behavior is to simulate the user clicking the cancel button and closing the view.

You can also optionally augment the behavior of presenting and dismissing alert views using the methods in Customizing behavior.

## Topics

### Deprecated
- [Deprecated symbols](uialertviewdelegate-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol UIActionSheetDelegate](uiactionsheetdelegate.md)
  The interface for the delegate of an action sheet object.
- [protocol UIPopoverControllerDelegate](uipopovercontrollerdelegate.md)
  The interface for the delegate of a popover controller object.
- [protocol UISearchDisplayDelegate](uisearchdisplaydelegate.md)
  The interface for the delegate of a search display controller.
- [protocol UIViewControllerPreviewing](uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.
- [protocol UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md)
  A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate)*