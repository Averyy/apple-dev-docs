# numberOfPreviewItems(in:)

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the number of items that the preview panel should preview.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func numberOfPreviewItems(in panel: QLPreviewPanel!) -> Int
```

```objc
- (NSInteger) numberOfPreviewItemsInPreviewPanel:(QLPreviewPanel *) panel;
```

## Return Value

The number of items the preview panel should display.

## Parameters

- `panel`: The preview panel.

## See Also

### Required Methods
- [func previewPanel(QLPreviewPanel!, previewItemAt: Int) -> (any QLPreviewItem)!](./previewpanel%28_,previewitemat%29.md)
  Returns the item that the preview panel should preview at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldatasource/numberofpreviewitems(in:))*