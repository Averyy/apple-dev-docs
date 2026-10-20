# numberOfPreviewItems(in:)

**Framework**: Quick Look UI  
**Kind**: method  
**Required**: Yes

Returns the number of items that the preview panel should preview.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func numberOfPreviewItems(in panel: QLPreviewPanel!) -> Int
```

#### Return Value

The number of items the preview panel should display.

## Parameters

- `panel`: The preview panel.

## See Also

- [func previewPanel(QLPreviewPanel!, previewItemAt: Int) -> (any QLPreviewItem)!](qlpreviewpaneldatasource/previewpanel(_:previewitemat:).md)
  Returns the item that the preview panel should preview at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldatasource/numberofpreviewitems(in:))*