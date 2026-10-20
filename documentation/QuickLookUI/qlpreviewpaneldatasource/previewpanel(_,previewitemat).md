# previewPanel(_:previewItemAt:)

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the item that the preview panel should preview at a given index.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func previewPanel(_ panel: QLPreviewPanel!, previewItemAt index: Int) -> (any QLPreviewItem)!
```

```objc
- (id<QLPreviewItem>) previewPanel:(QLPreviewPanel *) panel previewItemAtIndex:(NSInteger) index;
```

#### Return Value

The item that the preview panel should preview at index `index`.

## Parameters

- `panel`: The preview panel.
- `index`: The index of the item to preview.

## See Also

### Required Methods
- [func numberOfPreviewItems(in: QLPreviewPanel!) -> Int](./numberofpreviewitems%28in%29.md)
  Returns the number of items that the preview panel should preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldatasource/previewpanel(_:previewitemat:))*