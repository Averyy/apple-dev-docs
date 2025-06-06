# currentPreviewItem

**Framework**: Quick Look UI  
**Kind**: property

The currently previewed item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var currentPreviewItem: (any QLPreviewItem)! { get }
```

#### Discussion

The value is `nil` if there’s no current preview item.

## See Also

- [var dataSource: (any QLPreviewPanelDataSource)!](qlpreviewpanel/datasource.md)
  The preview panel data source.
- [func reloadData()](qlpreviewpanel/reloaddata.md)
  Asks the preview panel to reload its data from its data source.
- [func refreshCurrentPreviewItem()](qlpreviewpanel/refreshcurrentpreviewitem.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](qlpreviewpanel/currentpreviewitemindex.md)
  The index of the current preview item.
- [var displayState: Any!](qlpreviewpanel/displaystate.md)
  The preview panel’s display state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/currentpreviewitem)*