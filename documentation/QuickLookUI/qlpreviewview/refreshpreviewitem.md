# refreshPreviewItem()

**Framework**: Quick Look UI  
**Kind**: method

Updates the preview to display the currently previewed item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func refreshPreviewItem()
```

#### Discussion

When you modify the object that the [`previewItem`](qlpreviewview/previewitem.md) property points to, call this method to generate and display the new preview.

## See Also

- [var previewItem: (any QLPreviewItem)!](qlpreviewview/previewitem.md)
  The item to preview.
- [var displayState: Any!](qlpreviewview/displaystate.md)
  The current display state of the [`previewItem`](qlpreviewview/previewitem.md).
- [var autostarts: Bool](qlpreviewview/autostarts.md)
  A Boolean value that determines whether the preview starts automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/refreshpreviewitem())*