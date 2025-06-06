# displayState

**Framework**: Quick Look UI  
**Kind**: property

The preview panel’s display state.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var displayState: Any! { get set }
```

#### Discussion

This property is an opaque object that Quick Look uses to get and set the current display state of the preview. The display state could be, for example, the currently displayed page, the zoom factor on an image, or the position in a movie.

You can use this property to get and save the current display state of the preview before switching to another. This saving allows you to restore a preview later on when the user switches back to it.

## See Also

- [var dataSource: (any QLPreviewPanelDataSource)!](qlpreviewpanel/datasource.md)
  The preview panel data source.
- [func reloadData()](qlpreviewpanel/reloaddata.md)
  Asks the preview panel to reload its data from its data source.
- [func refreshCurrentPreviewItem()](qlpreviewpanel/refreshcurrentpreviewitem.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](qlpreviewpanel/currentpreviewitemindex.md)
  The index of the current preview item.
- [var currentPreviewItem: (any QLPreviewItem)!](qlpreviewpanel/currentpreviewitem.md)
  The currently previewed item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/displaystate)*