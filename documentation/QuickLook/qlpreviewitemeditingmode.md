# QLPreviewItemEditingMode

**Framework**: Quick Look  
**Kind**: enum

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum QLPreviewItemEditingMode
```

## Topics

### Enumeration Cases
- [QLPreviewItemEditingMode.createCopy](qlpreviewitemeditingmode/createcopy.md)
- [QLPreviewItemEditingMode.disabled](qlpreviewitemeditingmode/disabled.md)
- [QLPreviewItemEditingMode.updateContents](qlpreviewitemeditingmode/updatecontents.md)
### Initializers
- [init?(rawValue: Int)](qlpreviewitemeditingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func previewController(QLPreviewController, editingModeFor: any QLPreviewItem) -> QLPreviewItemEditingMode](qlpreviewcontrollerdelegate/previewcontroller(_:editingmodefor:).md)
  Returns a value that indicates how the preview controller handles edits to the content of the previewed file.
- [func previewController(QLPreviewController, didUpdateContentsOf: any QLPreviewItem)](qlpreviewcontrollerdelegate/previewcontroller(_:didupdatecontentsof:).md)
  Tells the delegate that the content of a preview was updated successfully.
- [func previewController(QLPreviewController, didSaveEditedCopyOf: any QLPreviewItem, at: URL)](qlpreviewcontrollerdelegate/previewcontroller(_:didsaveeditedcopyof:at:).md)
  Tells the delegate that the preview item’s edited content was successfully saved to a copy at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewitemeditingmode)*