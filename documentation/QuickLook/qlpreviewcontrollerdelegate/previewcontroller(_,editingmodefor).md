# previewController(_:editingModeFor:)

**Framework**: Quick Look  
**Kind**: method

Returns a value that indicates how the preview controller handles edits to the content of the previewed file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewController(_ controller: QLPreviewController, editingModeFor previewItem: any QLPreviewItem) -> QLPreviewItemEditingMode
```

#### Return Value

A value that indicates whether the previewed content is editable and how Quick Look saves the edits. If you return [`QLPreviewItemEditingMode.updateContents`](qlpreviewitemeditingmode/updatecontents.md) or [`QLPreviewItemEditingMode.createCopy`](qlpreviewitemeditingmode/createcopy.md) to allow edits to a preview, make sure to implement the appropriate callbacks.

#### Discussion

The platform invokes this callback when the preview controller loads its data. The system calls it for each preview item that it passes to the data source of the preview controller.

By default, a preview controller doesn’t allow edits to a preview. However, you can implement this method to allow the user to edit the previewed document, and specify the behavior for saving changes. The supported set of edits may change over time, but currently includes adding markup to images or PDFs, as well as simple edits to video files.

If you want to update the underlying file in place, return [`QLPreviewItemEditingMode.updateContents`](qlpreviewitemeditingmode/updatecontents.md), and implement both the [`previewController(_:didUpdateContentsOf:)`](qlpreviewcontrollerdelegate/previewcontroller(_:didupdatecontentsof:).md) and [`previewController(_:didSaveEditedCopyOf:at:)`](qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:).md) delegate methods. The Quick Look feature calls [`previewController(_:didUpdateContentsOf:)`](qlpreviewcontrollerdelegate/previewcontroller(_:didupdatecontentsof:).md) first and updates the preview item’s content. If it can’t update the item directly, it invokes [`previewController(_:didSaveEditedCopyOf:at:)`](qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:).md) and creates a copy of the preview item’s content that contains the edits.

If you prefer to always save edits to a copy of the preview item’s content, return [`QLPreviewItemEditingMode.createCopy`](qlpreviewitemeditingmode/createcopy.md) and implement [`previewController(_:didSaveEditedCopyOf:at:)`](qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:).md).

## Parameters

- `controller`: The controller that displays the preview.
- `previewItem`: The preview item for a file.

## See Also

- [enum QLPreviewItemEditingMode](qlpreviewitemeditingmode.md)
- [func previewController(QLPreviewController, didUpdateContentsOf: any QLPreviewItem)](qlpreviewcontrollerdelegate/previewcontroller(_:didupdatecontentsof:).md)
  Tells the delegate that the content of a preview was updated successfully.
- [func previewController(QLPreviewController, didSaveEditedCopyOf: any QLPreviewItem, at: URL)](qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:).md)
  Tells the delegate that the preview item’s edited content was successfully saved to a copy at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontroller(_:editingmodefor:))*