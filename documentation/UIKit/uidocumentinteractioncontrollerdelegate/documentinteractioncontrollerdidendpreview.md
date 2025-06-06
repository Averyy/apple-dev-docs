# documentInteractionControllerDidEndPreview(_:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller has dismissed its document preview.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionControllerDidEndPreview(_ controller: UIDocumentInteractionController)
```

#### Discussion

This method is called after the view containing the document preview has been removed from the application’s key window. You can use this notification to remove any interface elements you set up behind the preview elements.

## Parameters

- `controller`: The document interaction controller that dismissed its document preview.

## See Also

- [func documentInteractionControllerWillBeginPreview(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(_:).md)
  Called when a document interaction controller is about to display a preview for its document.
- [func documentInteractionControllerWillPresentOptionsMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentoptionsmenu(_:).md)
  Called when a document interaction controller is about to display an options menu.
- [func documentInteractionControllerDidDismissOptionsMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissoptionsmenu(_:).md)
  Called when a document interaction controller has dismissed its options menu.
- [func documentInteractionControllerWillPresentOpenInMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(_:).md)
  Called when a document interaction controller is about to display an Open In menu.
- [func documentInteractionControllerDidDismissOpenInMenu(UIDocumentInteractionController)](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu(_:).md)
  Called when a document interaction controller has dismissed its Open In menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview(_:))*