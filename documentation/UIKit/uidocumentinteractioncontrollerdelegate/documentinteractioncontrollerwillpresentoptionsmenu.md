# documentInteractionControllerWillPresentOptionsMenu(_:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller is about to display an options menu.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionControllerWillPresentOptionsMenu(_ controller: UIDocumentInteractionController)
```

#### Discussion

The options menu is used to present the user with options for previewing the document, opening it in an application, or copying its contents. You can use this method to update your user interface in response to displaying the menu.

## Parameters

- `controller`: The document interaction controller that is about to display an options menu.

## See Also

- [func documentInteractionControllerWillBeginPreview(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(_:).md)
  Called when a document interaction controller is about to display a preview for its document.
- [func documentInteractionControllerDidEndPreview(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview(_:).md)
  Called when a document interaction controller has dismissed its document preview.
- [func documentInteractionControllerDidDismissOptionsMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissoptionsmenu(_:).md)
  Called when a document interaction controller has dismissed its options menu.
- [func documentInteractionControllerWillPresentOpenInMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(_:).md)
  Called when a document interaction controller is about to display an Open In menu.
- [func documentInteractionControllerDidDismissOpenInMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu(_:).md)
  Called when a document interaction controller has dismissed its Open In menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentoptionsmenu(_:))*