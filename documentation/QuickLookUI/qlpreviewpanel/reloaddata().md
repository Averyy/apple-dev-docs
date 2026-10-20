# reloadData()

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Asks the preview panel to reload its data from its data source.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func reloadData()
```

```objc
- (void) reloadData;
```

#### Discussion

This method doesn’t refresh the visible item if it hasn’t changed.

## See Also

### Managing the Preview Items
- [var dataSource: (any QLPreviewPanelDataSource)!](./datasource.md)
  The preview panel data source.
- [func refreshCurrentPreviewItem()](./refreshcurrentpreviewitem%28%29.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](./currentpreviewitemindex.md)
  The index of the current preview item.
- [var currentPreviewItem: (any QLPreviewItem)!](./currentpreviewitem.md)
  The currently previewed item.
- [var displayState: Any!](./displaystate.md)
  The preview panel’s display state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/reloaddata())*