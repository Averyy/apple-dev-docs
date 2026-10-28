# documentInteractionControllerWillPresentOpenInMenu(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when a document interaction controller is about to display an Open In menu.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionControllerWillPresentOpenInMenu(_ controller: UIDocumentInteractionController)
```

```objc
- (void) documentInteractionControllerWillPresentOpenInMenu:(UIDocumentInteractionController *) controller;
```

## Discussion

The Open In menu is used to select an application for opening the current file. You can use this method to update your user interface in response to displaying the menu.

## Parameters

- `controller`: The document interaction controller that is about to display a menu.

## See Also

### Presenting the user interface
- [func documentInteractionControllerWillBeginPreview(UIDocumentInteractionController)](./documentinteractioncontrollerwillbeginpreview%28_%29.md)
  Called when a document interaction controller is about to display a preview for its document.
- [func documentInteractionControllerDidEndPreview(UIDocumentInteractionController)](./documentinteractioncontrollerdidendpreview%28_%29.md)
  Called when a document interaction controller has dismissed its document preview.
- [func documentInteractionControllerWillPresentOptionsMenu(UIDocumentInteractionController)](./documentinteractioncontrollerwillpresentoptionsmenu%28_%29.md)
  Called when a document interaction controller is about to display an options menu.
- [func documentInteractionControllerDidDismissOptionsMenu(UIDocumentInteractionController)](./documentinteractioncontrollerdiddismissoptionsmenu%28_%29.md)
  Called when a document interaction controller has dismissed its options menu.
- [func documentInteractionControllerDidDismissOpenInMenu(UIDocumentInteractionController)](./documentinteractioncontrollerdiddismissopeninmenu%28_%29.md)
  Called when a document interaction controller has dismissed its Open In menu.
- [func documentInteractionController(UIDocumentInteractionController, canPerformAction: Selector?) -> Bool](./documentinteractioncontroller%28_,canperformaction%29.md)
  Called when a document interaction controller needs to know whether the specified action can be performed on the associated document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontrollerwillpresentopeninmenu(_:))*