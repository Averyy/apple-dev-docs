# currentPreviewItem

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property

The currently previewed item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var currentPreviewItem: (any QLPreviewItem)! { get }
```

```objc
@property (readonly) id<QLPreviewItem> currentPreviewItem;
```

#### Discussion

The value is `nil` if there’s no current preview item.

## See Also

### Managing the Preview Items
- [var dataSource: (any QLPreviewPanelDataSource)!](./datasource.md)
  The preview panel data source.
- [func reloadData()](./reloaddata%28%29.md)
  Asks the preview panel to reload its data from its data source.
- [func refreshCurrentPreviewItem()](./refreshcurrentpreviewitem%28%29.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](./currentpreviewitemindex.md)
  The index of the current preview item.
- [var displayState: Any!](./displaystate.md)
  The preview panel’s display state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel/currentpreviewitem)*