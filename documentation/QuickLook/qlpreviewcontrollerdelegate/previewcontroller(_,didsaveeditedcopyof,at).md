# previewController(_:didSaveEditedCopyOf:at:)

**Framework**: Quick Look  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the preview item’s edited content was successfully saved to a copy at the given URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func previewController(_ controller: QLPreviewController, didSaveEditedCopyOf previewItem: any QLPreviewItem, at modifiedContentsURL: URL)
```

```objc
- (void) previewController:(QLPreviewController *) controller didSaveEditedCopyOfPreviewItem:(id<QLPreviewItem>) previewItem atURL:(NSURL *) modifiedContentsURL;
```

#### Discussion

The platform invokes this callback with an edited copy of the preview item at `modifiedContentsURL`. It invokes the callback in the following scenarios:

- The editing mode of the `previewItem` is [`QLPreviewItemEditingMode.createCopy`](../qlpreviewitemeditingmode/createcopy.md).
- The editing mode of the `previewItem` is [`QLPreviewItemEditingMode.updateContents`](../qlpreviewitemeditingmode/updatecontents.md) and the system can’t overwrite its [`previewItemURL`](../qlpreviewitem/previewitemurl.md). In this case, `modifiedContentsURL` points to a temporary file on disk containing the edited copy.
- The editing mode of the preview item is [`QLPreviewItemEditingMode.updateContents`](../qlpreviewitemeditingmode/updatecontents.md) and its content type doesn’t match the content type of the edited version. This mismatch means that the file type of the file at `modifiedContentsURL` may be different from the file type of the preview item.

The platform may invoke the callback multiple times consecutively with the successive edited versions of the preview item. It typically invokes the callback once for each time the user saves their edits.

## Parameters

- `controller`: The controller that displays the preview.
- `previewItem`: The preview item for a file.
- `modifiedContentsURL`: A URL pointing to a temporary file that contains the edited version of the previewed file.

## See Also

### Editing the content of a preview
- [func previewController(QLPreviewController, editingModeFor: any QLPreviewItem) -> QLPreviewItemEditingMode](./previewcontroller%28_,editingmodefor%29.md)
  Returns a value that indicates how the preview controller handles edits to the content of the previewed file.
- [enum QLPreviewItemEditingMode](../qlpreviewitemeditingmode.md)
- [func previewController(QLPreviewController, didUpdateContentsOf: any QLPreviewItem)](./previewcontroller%28_,didupdatecontentsof%29.md)
  Tells the delegate that the content of a preview was updated successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:))*