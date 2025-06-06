# previewController(_:didUpdateContentsOf:)

**Framework**: Quick Look  
**Kind**: method

Tells the delegate that the content of a preview was updated successfully.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewController(_ controller: QLPreviewController, didUpdateContentsOf previewItem: any QLPreviewItem)
```

#### Discussion

The platform invokes this callback after the preview controller successfully overwrites the file at the `previewItem’`s [`previewItemURL`](qlpreviewitem/previewitemurl.md) with an updated file.

The platform may invoke the callback multiple times consecutively with the successive edited versions of the preview item. It typically invokes the callback once for each time the user saves their edits.

## Parameters

- `controller`: The controller that displays the preview.
- `previewItem`: The preview item for a file.

## See Also

- [func previewController(QLPreviewController, editingModeFor: any QLPreviewItem) -> QLPreviewItemEditingMode](qlpreviewcontrollerdelegate/previewcontroller(_:editingmodefor:).md)
  Returns a value that indicates how the preview controller handles edits to the content of the previewed file.
- [enum QLPreviewItemEditingMode](qlpreviewitemeditingmode.md)
- [func previewController(QLPreviewController, didSaveEditedCopyOf: any QLPreviewItem, at: URL)](qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:).md)
  Tells the delegate that the preview item’s edited content was successfully saved to a copy at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontroller(_:didupdatecontentsof:))*