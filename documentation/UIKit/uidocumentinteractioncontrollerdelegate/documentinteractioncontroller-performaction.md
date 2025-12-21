# documentInteractionController(_:performAction:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller wants its delegate to perform a specified action with the associated document.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, performAction action: Selector?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was performed successfully or [`false`](https://developer.apple.com/documentation/Swift/false) if it was not.

#### Discussion

The supported `action` selectors for this method are `copy:` and `print:`. (The `print:` selector is available in iOS 4.2 and later. Printing is supported only on devices that support multitasking.)

To implement a `copy:` action, write the contents of the document—directly, or modified according to the intent of your app—to the pasteboard.

To implement a `print:` action, use the shared print interaction controller object. Assign the [`url`](uidocumentinteractioncontroller/url.md) property of the document interaction controller to the print interaction controller’s [`printingItem`](uiprintinteractioncontroller/printingitem.md) property. Then present the printing user interface. For details, refer to [`UIPrintInteractionController`](uiprintinteractioncontroller.md) and to [`Printing`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Printing/Printing.html#//apple_ref/doc/uid/TP40010156-CH12) in [`Drawing and Printing Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156).

Instead of implementing printing code in this method, you can rely on the built-in printing support of the Quick Look framework. For document types that can be previewed, the options menu of a document interaction controller always contains a Quick Look item. If the user chooses that item, the resulting Quick Look view includes an action button in the navigation bar that, when tapped, offers a Print button. In this case, the system automatically handles printing. For details, refer to [`QLPreviewController`](https://developer.apple.com/documentation/QuickLook/QLPreviewController) and to [`Using the Quick Look Framework`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/UsingtheQuickLookFramework.html#//apple_ref/doc/uid/TP40010413) in [`Document Interaction Programming Topics for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010403).

## Parameters

- `controller`: The document interaction controller managing an associated document.
- `action`: The selector representing the action to perform. You can invoke this selector directly on the object responsible for performing the action or use it to call the appropriate method.

## See Also

- [func documentInteractionController(UIDocumentInteractionController, canPerformAction: Selector?) -> Bool](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:canperformaction:).md)
  Called when a document interaction controller needs to know whether the specified action can be performed on the associated document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:performaction:))*