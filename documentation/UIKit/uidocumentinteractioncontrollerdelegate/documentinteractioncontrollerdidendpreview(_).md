# documentInteractionControllerDidEndPreview(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) documentInteractionControllerDidEndPreview:(UIDocumentInteractionController *) controller;
```

#### Discussion

This method is called after the view containing the document preview has been removed from the application’s key window. You can use this notification to remove any interface elements you set up behind the preview elements.

## Parameters

- `controller`: The document interaction controller that dismissed its document preview.

## See Also

### Presenting the user interface
- [func documentInteractionControllerWillBeginPreview(UIDocumentInteractionController)](./documentinteractioncontrollerwillbeginpreview%28_%29.md)
  Called when a document interaction controller is about to display a preview for its document.
- [func documentInteractionControllerWillPresentOptionsMenu(UIDocumentInteractionController)](./documentinteractioncontrollerwillpresentoptionsmenu%28_%29.md)
  Called when a document interaction controller is about to display an options menu.
- [func documentInteractionControllerDidDismissOptionsMenu(UIDocumentInteractionController)](./documentinteractioncontrollerdiddismissoptionsmenu%28_%29.md)
  Called when a document interaction controller has dismissed its options menu.
- [func documentInteractionControllerWillPresentOpenInMenu(UIDocumentInteractionController)](./documentinteractioncontrollerwillpresentopeninmenu%28_%29.md)
  Called when a document interaction controller is about to display an Open In menu.
- [func documentInteractionControllerDidDismissOpenInMenu(UIDocumentInteractionController)](./documentinteractioncontrollerdiddismissopeninmenu%28_%29.md)
  Called when a document interaction controller has dismissed its Open In menu.
- [func documentInteractionController(UIDocumentInteractionController, canPerformAction: Selector?) -> Bool](./documentinteractioncontroller%28_,canperformaction%29.md)
  Called when a document interaction controller needs to know whether the specified action can be performed on the associated document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerdidendpreview(_:))*