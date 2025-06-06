# previewController(_:previewItemAt:)

**Framework**: Quick Look  
**Kind**: method  
**Required**: Yes

Returns the preview item that the controller displays for the specified index.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func previewController(_ controller: QLPreviewController, previewItemAt index: Int) -> any QLPreviewItem
```

#### Return Value

The preview item to display. The item must be an `NSURL` object, or a custom object that conforms to the [`QLPreviewItem`](qlpreviewitem.md) protocol.

#### Discussion

The system invokes this method when the preview controller needs the preview item for a specified index position.

## Parameters

- `controller`: The Quick Look preview controller that’s requesting a preview item.
- `index`: The index position, within the preview navigation list, of the item to preview.

## See Also

- [func numberOfPreviewItems(in: QLPreviewController) -> Int](qlpreviewcontrollerdatasource/numberofpreviewitems(in:).md)
  Returns the number of preview items to include in the preview navigation list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdatasource/previewcontroller(_:previewitemat:))*