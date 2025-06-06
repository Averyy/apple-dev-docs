# QLPreviewItemLoadingBlock

**Framework**: Quick Look UI  
**Kind**: typealias

A type that defines a block used to load a Quick Look preview item.

**Availability**:
- macOS 10.13+

## Declaration

```swift
typealias QLPreviewItemLoadingBlock = ((any Error)?) -> Void
```

#### Discussion

A type that defines a block used to load a Quick Look preview item.

## See Also

- [class QLPreviewPanel](qlpreviewpanel.md)
  A class that implements the Quick Look preview panel to display a preview of a list of items.
- [class QLPreviewView](qlpreviewview.md)
  A Quick Look preview of an item that you can embed into your view hierarchy.
- [protocol QLPreviewItem](qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [protocol QLPreviewPanelDataSource](qlpreviewpaneldatasource.md)
  A protocol that the Quick Look preview panel uses to access the contents of its data source object.
- [protocol QLPreviewPanelDelegate](qlpreviewpaneldelegate.md)
  A protocol for the delegate of the Quick Look preview panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewitemloadingblock)*