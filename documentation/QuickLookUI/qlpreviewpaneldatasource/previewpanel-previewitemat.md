# previewPanel(_:previewItemAt:)

**Framework**: Quick Look UI  
**Kind**: method  
**Required**: Yes

Returns the item that the preview panel should preview at a given index.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func previewPanel(_ panel: QLPreviewPanel!, previewItemAt index: Int) -> (any QLPreviewItem)!
```

#### Return Value

The item that the preview panel should preview at index `index`.

## Parameters

- `panel`: The preview panel.
- `index`: The index of the item to preview.

## See Also

- [func numberOfPreviewItems(in: QLPreviewPanel!) -> Int](qlpreviewpaneldatasource/numberofpreviewitems(in:).md)
  Returns the number of items that the preview panel should preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldatasource/previewpanel(_:previewitemat:))*