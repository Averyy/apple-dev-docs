# reloadData()

**Framework**: Quick Look UI  
**Kind**: method

Asks the preview panel to reload its data from its data source.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func reloadData()
```

#### Discussion

This method doesn’t refresh the visible item if it hasn’t changed.

## See Also

- [var dataSource: (any QLPreviewPanelDataSource)!](qlpreviewpanel/datasource.md)
  The preview panel data source.
- [func refreshCurrentPreviewItem()](qlpreviewpanel/refreshcurrentpreviewitem.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](qlpreviewpanel/currentpreviewitemindex.md)
  The index of the current preview item.
- [var currentPreviewItem: (any QLPreviewItem)!](qlpreviewpanel/currentpreviewitem.md)
  The currently previewed item.
- [var displayState: Any!](qlpreviewpanel/displaystate.md)
  The preview panel’s display state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/reloaddata())*