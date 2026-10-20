# dataSource

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property

The preview panel data source.

**Availability**:
- macOS 10.6+

## Declaration

```swift
unowned(unsafe) var dataSource: (any QLPreviewPanelDataSource)! { get set }
```

```objc
@property (assign) id<QLPreviewPanelDataSource> dataSource;
```

## See Also

### Managing the Preview Items
- [func reloadData()](./reloaddata%28%29.md)
  Asks the preview panel to reload its data from its data source.
- [func refreshCurrentPreviewItem()](./refreshcurrentpreviewitem%28%29.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](./currentpreviewitemindex.md)
  The index of the current preview item.
- [var currentPreviewItem: (any QLPreviewItem)!](./currentpreviewitem.md)
  The currently previewed item.
- [var displayState: Any!](./displaystate.md)
  The preview panel’s display state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/datasource)*