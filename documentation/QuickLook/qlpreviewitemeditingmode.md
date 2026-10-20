# QLPreviewItemEditingMode

**Framework**: Quick Look  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum QLPreviewItemEditingMode
```

```c
enum QLPreviewItemEditingMode : NSInteger;
```

## Topics

### Enumeration Cases
- [QLPreviewItemEditingMode.createCopy](./qlpreviewitemeditingmode/createcopy.md)
- [QLPreviewItemEditingMode.disabled](./qlpreviewitemeditingmode/disabled.md)
- [QLPreviewItemEditingMode.updateContents](./qlpreviewitemeditingmode/updatecontents.md)
### Initializers
- [init?(rawValue: Int)](./qlpreviewitemeditingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Editing the content of a preview
- [func previewController(QLPreviewController, editingModeFor: any QLPreviewItem) -> QLPreviewItemEditingMode](./qlpreviewcontrollerdelegate/previewcontroller%28_,editingmodefor%29.md)
  Returns a value that indicates how the preview controller handles edits to the content of the previewed file.
- [func previewController(QLPreviewController, didUpdateContentsOf: any QLPreviewItem)](./qlpreviewcontrollerdelegate/previewcontroller%28_,didupdatecontentsof%29.md)
  Tells the delegate that the content of a preview was updated successfully.
- [func previewController(QLPreviewController, didSaveEditedCopyOf: any QLPreviewItem, at: URL)](./qlpreviewcontrollerdelegate/previewcontroller%28_,didsaveeditedcopyof,at%29.md)
  Tells the delegate that the preview item’s edited content was successfully saved to a copy at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewitemeditingmode)*