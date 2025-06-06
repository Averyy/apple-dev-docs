# previewItem

**Framework**: Quick Look UI  
**Kind**: property

The item to preview.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var previewItem: (any QLPreviewItem)! { get set }
```

#### Discussion

Quick Look requires Items you wish to conform to the [`QLPreviewItem`](qlpreviewitem.md) protocol. When you set this property, the [`QLPreviewView`](qlpreviewview.md) loads the preview asynchronously. Due to this asynchronous behavior, don’t assume that the preview is ready immediately after assigning it to this property.

## See Also

- [func refreshPreviewItem()](qlpreviewview/refreshpreviewitem.md)
  Updates the preview to display the currently previewed item.
- [var displayState: Any!](qlpreviewview/displaystate.md)
  The current display state of the [`previewItem`](qlpreviewview/previewitem.md).
- [var autostarts: Bool](qlpreviewview/autostarts.md)
  A Boolean value that determines whether the preview starts automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/previewitem)*