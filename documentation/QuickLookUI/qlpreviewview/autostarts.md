# autostarts

**Framework**: Quick Look UI  
**Kind**: property

A Boolean value that determines whether the preview starts automatically.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var autostarts: Bool { get set }
```

#### Discussion

Set this property to allow previews of movie files to start playback automatically when displayed.

## See Also

- [var previewItem: (any QLPreviewItem)!](qlpreviewview/previewitem.md)
  The item to preview.
- [func refreshPreviewItem()](qlpreviewview/refreshpreviewitem.md)
  Updates the preview to display the currently previewed item.
- [var displayState: Any!](qlpreviewview/displaystate.md)
  The current display state of the [`previewItem`](qlpreviewview/previewitem.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/autostarts)*