# documentInteractionControllerWillBeginPreview(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) documentInteractionControllerWillBeginPreview:(UIDocumentInteractionController *) controller;
```

## Discussion

This method is called shortly before the view containing the document preview is presented modally. You can use this notification to set up any additional interface elements behind the preview elements.

## Parameters

- `controller`: The document interaction controller that is about to preview its document.

## See Also

### Presenting the user interface
- [func documentInteractionControllerDidEndPreview(UIDocumentInteractionController)](./documentinteractioncontrollerdidendpreview%28_%29.md)
  Called when a document interaction controller has dismissed its document preview.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillbeginpreview(_:))*