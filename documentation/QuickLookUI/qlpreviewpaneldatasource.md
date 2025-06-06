# QLPreviewPanelDataSource

**Framework**: Quick Look UI  
**Kind**: protocol

A protocol that the Quick Look preview panel uses to access the contents of its data source object.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol QLPreviewPanelDataSource
```

## Topics

### Required Methods
- [func numberOfPreviewItems(in: QLPreviewPanel!) -> Int](qlpreviewpaneldatasource/numberofpreviewitems(in:).md)
  Returns the number of items that the preview panel should preview.
- [func previewPanel(QLPreviewPanel!, previewItemAt: Int) -> (any QLPreviewItem)!](qlpreviewpaneldatasource/previewpanel(_:previewitemat:).md)
  Returns the item that the preview panel should preview at a given index.

## See Also

- [class QLPreviewPanel](qlpreviewpanel.md)
  A class that implements the Quick Look preview panel to display a preview of a list of items.
- [class QLPreviewView](qlpreviewview.md)
  A Quick Look preview of an item that you can embed into your view hierarchy.
- [protocol QLPreviewItem](qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [protocol QLPreviewPanelDelegate](qlpreviewpaneldelegate.md)
  A protocol for the delegate of the Quick Look preview panel.
- [typealias QLPreviewItemLoadingBlock](qlpreviewitemloadingblock.md)
  A type that defines a block used to load a Quick Look preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldatasource)*