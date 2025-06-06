# UIDocumentInteractionControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods you can implement to respond to messages from a document interaction controller.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol UIDocumentInteractionControllerDelegate : NSObjectProtocol
```

#### Overview

Use this protocol to participate when document previews are displayed and when a document is about to be opened by another application. You can also use this protocol to respond to commands (such as “copy” and “print”) from a document interaction controller’s options menu.

If you use a document interaction controller to display a document preview, your delegate must implement the [`documentInteractionControllerViewControllerForPreview(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(_:).md) method. All other methods of this protocol are optional.

For more information about using a document interaction controller, see [`UIDocumentInteractionController`](uidocumentinteractioncontroller.md).

## Topics

### Configuring the parent view controller
- [func documentInteractionControllerViewControllerForPreview(UIDocumentInteractionController) -> UIViewController](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewcontrollerforpreview(_:).md)
  Called when a document interaction controller needs a view controller for presenting a document preview.
- [func documentInteractionControllerViewForPreview(UIDocumentInteractionController) -> UIView?](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerviewforpreview(_:).md)
  Called when a document interaction controller needs the starting point for animating the display of a document preview.
- [func documentInteractionControllerRectForPreview(UIDocumentInteractionController) -> CGRect](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerrectforpreview(_:).md)
  Called when a document interaction controller needs the rectangle to use as the starting point for animating the display of a document preview.
### Presenting the user interface
- [func documentInteractionControllerWillBeginPreview(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(_:).md)
  Called when a document interaction controller is about to display a preview for its document.
- [func documentInteractionControllerDidEndPreview(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview(_:).md)
  Called when a document interaction controller has dismissed its document preview.
- [func documentInteractionControllerWillPresentOptionsMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentoptionsmenu(_:).md)
  Called when a document interaction controller is about to display an options menu.
- [func documentInteractionControllerDidDismissOptionsMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissoptionsmenu(_:).md)
  Called when a document interaction controller has dismissed its options menu.
- [func documentInteractionControllerWillPresentOpenInMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(_:).md)
  Called when a document interaction controller is about to display an Open In menu.
- [func documentInteractionControllerDidDismissOpenInMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu(_:).md)
  Called when a document interaction controller has dismissed its Open In menu.
### Opening files
- [func documentInteractionController(UIDocumentInteractionController, willBeginSendingToApplication: String?)](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:willbeginsendingtoapplication:).md)
  Called when a document interaction controller’s document is about to be opened by the specified application.
- [func documentInteractionController(UIDocumentInteractionController, didEndSendingToApplication: String?)](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:didendsendingtoapplication:).md)
  Called when a document interaction controller’s document has been handed off to the specified application.
### Deprecated
- [func documentInteractionController(UIDocumentInteractionController, canPerformAction: Selector?) -> Bool](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:canperformaction:).md)
  Called when a document interaction controller needs to know whether the specified action can be performed on the associated document.
- [func documentInteractionController(UIDocumentInteractionController, performAction: Selector?) -> Bool](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:performaction:).md)
  Called when a document interaction controller wants its delegate to perform a specified action with the associated document.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UIDocumentInteractionControllerDelegate)?](uidocumentinteractioncontroller/delegate.md)
  The delegate you want to receive document interaction notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate)*