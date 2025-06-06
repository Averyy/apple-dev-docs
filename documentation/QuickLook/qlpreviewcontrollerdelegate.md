# QLPreviewControllerDelegate

**Framework**: Quick Look  
**Kind**: protocol

The protocol that a delegate of a preview controller needs to adopt to handle Quick Look previews.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol QLPreviewControllerDelegate : NSObjectProtocol
```

#### Overview

The delegate of a [`QLPreviewController`](qlpreviewcontroller.md) object needs to adopt this protocol to:

- Provide a zoom animation for Quick Look previews.
- Specify whether your app opens a URL that the user taps in a preview.
- Respond to the opening or closing of a preview.

The methods described here are optional, but expected.

## Topics

### Responding to preview requests
- [func previewController(QLPreviewController, frameFor: any QLPreviewItem, inSourceView: AutoreleasingUnsafeMutablePointer<UIView?>) -> CGRect](qlpreviewcontrollerdelegate/previewcontroller(_:framefor:insourceview:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a zoom effect.
- [func previewController(QLPreviewController, transitionImageFor: any QLPreviewItem, contentRect: UnsafeMutablePointer<CGRect>) -> UIImage?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionimagefor:contentrect:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewController(QLPreviewController, transitionViewFor: any QLPreviewItem) -> UIView?](qlpreviewcontrollerdelegate/previewcontroller(_:transitionviewfor:).md)
  Tells the delegate that the system is about to present the preview full screen or dismiss it, and asks for information to provide a smooth transition when zooming.
- [func previewControllerWillDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerwilldismiss(_:).md)
  Tells the delegate that the preview is about to close.
- [func previewControllerDidDismiss(QLPreviewController)](qlpreviewcontrollerdelegate/previewcontrollerdiddismiss(_:).md)
  Tells the delegate that the preview was closed.
### Responding to user actions
- [func previewController(QLPreviewController, shouldOpen: URL, for: any QLPreviewItem) -> Bool](qlpreviewcontrollerdelegate/previewcontroller(_:shouldopen:for:).md)
  Tells the delegate that the preview controller is trying to open a URL.
### Editing the content of a preview
- [func previewController(QLPreviewController, editingModeFor: any QLPreviewItem) -> QLPreviewItemEditingMode](qlpreviewcontrollerdelegate/previewcontroller(_:editingmodefor:).md)
  Returns a value that indicates how the preview controller handles edits to the content of the previewed file.
- [enum QLPreviewItemEditingMode](qlpreviewitemeditingmode.md)
- [func previewController(QLPreviewController, didUpdateContentsOf: any QLPreviewItem)](qlpreviewcontrollerdelegate/previewcontroller(_:didupdatecontentsof:).md)
  Tells the delegate that the content of a preview was updated successfully.
- [func previewController(QLPreviewController, didSaveEditedCopyOf: any QLPreviewItem, at: URL)](qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:).md)
  Tells the delegate that the preview item’s edited content was successfully saved to a copy at the given URL.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var dataSource: (any QLPreviewControllerDataSource)?](qlpreviewcontroller/datasource.md)
  The preview controller’s data source.
- [protocol QLPreviewControllerDataSource](qlpreviewcontrollerdatasource.md)
  The protocol that a data source for a preview controller needs to adopt to provide preview items to the controller.
- [var delegate: (any QLPreviewControllerDelegate)?](qlpreviewcontroller/delegate.md)
  The preview controller’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate)*