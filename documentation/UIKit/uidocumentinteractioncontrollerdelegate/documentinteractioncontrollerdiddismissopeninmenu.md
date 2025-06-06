# documentInteractionControllerDidDismissOpenInMenu(_:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller has dismissed its Open In menu.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionControllerDidDismissOpenInMenu(_ controller: UIDocumentInteractionController)
```

#### Discussion

You can use this method to remove any additional views or content you placed underneath the Open In menu in your [`documentInteractionControllerWillPresentOpenInMenu(_:)`](uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(_:).md) method.

## Parameters

- `controller`: The document interaction controller that dismissed its menu.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdiddismissopeninmenu(_:))*