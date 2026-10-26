# UIActionSheetDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for the delegate of an action sheet object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

> **Deprecated**: Use [`UIAlertController`](./uialertcontroller.md) instead.

## Declaration

```swift
@MainActor
protocol UIActionSheetDelegate : NSObjectProtocol
```

```objc
@protocol UIActionSheetDelegate <NSObject>
```

#### Overview

The delegate implements the button actions and any other custom behavior. Some of the methods defined in this protocol are optional.

If you add your own buttons or customize the behavior of an action sheet, implement a delegate conforming to this protocol to handle the corresponding delegate messages. Use the [`delegate`](./uiactionsheet/delegate.md) property of the action sheet object to specify one of your application objects as the delegate.

If you add your own buttons to an action sheet, the delegate must implement the [`actionSheet(_:clickedButtonAt:)`](./uiactionsheetdelegate/actionsheet%28_,clickedbuttonat%29.md) message to respond when those buttons are clicked; otherwise, your custom buttons do nothing. The action sheet is automatically dismissed after the [`actionSheet(_:clickedButtonAt:)`](./uiactionsheetdelegate/actionsheet%28_,clickedbuttonat%29.md) delegate method is invoked.

Optionally, you can implement the [`actionSheetCancel(_:)`](./uiactionsheetdelegate/actionsheetcancel%28_%29.md) method to take the appropriate action when the system cancels your action sheet. If the delegate does not implement this method, the default behavior is to simulate the user clicking the cancel button and closing the view.

You can also optionally augment the behavior of presenting and dismissing action sheets using the methods in Customizing behavior.

## Topics

### Deprecated
- [Deprecated symbols](./uiactionsheetdelegate-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIDocumentInteractionController](./uidocumentinteractioncontroller.md)

## See Also

### Deprecated protocols
- [protocol UIAlertViewDelegate](./uialertviewdelegate.md)
  The interface for the delegate of an alert view object.
- [protocol UIPopoverControllerDelegate](./uipopovercontrollerdelegate.md)
  The interface for the delegate of a popover controller object.
- [protocol UISearchDisplayDelegate](./uisearchdisplaydelegate.md)
  The interface for the delegate of a search display controller.
- [protocol UIViewControllerPreviewing](./uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.
- [protocol UIViewControllerPreviewingDelegate](./uiviewcontrollerpreviewingdelegate.md)
  A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.
- [UIAccelerometerDelegate](./uiaccelerometerdelegate.md)
  The interface for receiving acceleration-related data from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate)*