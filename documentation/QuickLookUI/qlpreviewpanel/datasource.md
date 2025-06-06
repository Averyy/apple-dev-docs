# dataSource

**Framework**: Quick Look UI  
**Kind**: property

The preview panel data source.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
unowned(unsafe) var dataSource: (any QLPreviewPanelDataSource)! { get set }
```

## See Also

- [func reloadData()](qlpreviewpanel/reloaddata.md)
  Asks the preview panel to reload its data from its data source.
- [func refreshCurrentPreviewItem()](qlpreviewpanel/refreshcurrentpreviewitem.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](qlpreviewpanel/currentpreviewitemindex.md)
  The index of the current preview item.
- [var currentPreviewItem: (any QLPreviewItem)!](qlpreviewpanel/currentpreviewitem.md)
  The currently previewed item.
- [var displayState: Any!](qlpreviewpanel/displaystate.md)
  The preview panel’s display state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/datasource)*