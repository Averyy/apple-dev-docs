# displayState

**Framework**: Quick Look UI  
**Kind**: property

The current display state of the [`previewItem`](qlpreviewview/previewitem.md).

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

- [var previewItem: (any QLPreviewItem)!](qlpreviewview/previewitem.md)
  The item to preview.
- [func refreshPreviewItem()](qlpreviewview/refreshpreviewitem.md)
  Updates the preview to display the currently previewed item.
- [var autostarts: Bool](qlpreviewview/autostarts.md)
  A Boolean value that determines whether the preview starts automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/displaystate)*