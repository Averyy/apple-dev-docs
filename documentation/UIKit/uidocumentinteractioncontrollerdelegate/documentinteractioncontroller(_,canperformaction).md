# documentInteractionController(_:canPerformAction:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when a document interaction controller needs to know whether the specified action can be performed on the associated document.

**Availability**:
- iOS 3.2+ - Deprecated in 6.0
- iPadOS 3.2+ - Deprecated in 6.0
- Mac Catalyst 3.2+ - Deprecated in 6.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Apps should use [`UIActivityViewController`](../uiactivityviewcontroller.md) for actions.

## Declaration

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, canPerformAction action: Selector?) -> Bool
```

```objc
- (BOOL) documentInteractionController:(UIDocumentInteractionController *) controller canPerformAction:(SEL) action;
```

## Return Value

[`true`](../../Swift/true.md) if the specified action is supported for the associated document or [`false`](../../Swift/false.md) if it is not. If you do not implement this method, the return value is assumed to be [`false`](../../Swift/false.md).

## Discussion

When building the options menu (invoked, for example, by the user performing a long press gesture), a document interaction controller calls this method to find out if your app can perform various actions. If you implement this method for a given action, you must also implement the [`documentInteractionController(_:performAction:)`](./documentinteractioncontroller%28_,performaction%29.md) method for that action.

The supported `action` selectors for this method are `copy:` and `print:`. (The `print:` selector is available in iOS 4.2 and later. Printing is supported only on devices that support multitasking.)

For each action that you implement in the [`documentInteractionController(_:performAction:)`](./documentinteractioncontroller%28_,performaction%29.md) delegate method, return [`true`](../../Swift/true.md) from this method if that action is available for the document.

## Parameters

- `controller`: The document interaction controller managing an associated document.
- `action`: The selector representing the action in question.

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
- [func documentInteractionControllerWillPresentOpenInMenu(UIDocumentInteractionController)](./documentinteractioncontrollerwillpresentopeninmenu%28_%29.md)
  Called when a document interaction controller is about to display an Open In menu.
- [func documentInteractionControllerDidDismissOpenInMenu(UIDocumentInteractionController)](./documentinteractioncontrollerdiddismissopeninmenu%28_%29.md)
  Called when a document interaction controller has dismissed its Open In menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:canperformaction:))*