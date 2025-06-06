# documentInteractionControllerWillBeginPreview(_:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller is about to display a preview for its document.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionControllerWillBeginPreview(_ controller: UIDocumentInteractionController)
```

#### Discussion

This method is called shortly before the view containing the document preview is presented modally. You can use this notification to set up any additional interface elements behind the preview elements.

## Parameters

- `controller`: The document interaction controller that is about to preview its document.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(_:))*