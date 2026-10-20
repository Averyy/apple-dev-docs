# autostarts

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the preview starts automatically.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var autostarts: Bool { get set }
```

```objc
@property BOOL autostarts;
```

#### Discussion

Set this property to allow previews of movie files to start playback automatically when displayed.

## See Also

### Displaying a Preview
- [var previewItem: (any QLPreviewItem)!](./previewitem.md)
  The item to preview.
- [func refreshPreviewItem()](./refreshpreviewitem%28%29.md)
  Updates the preview to display the currently previewed item.
- [var displayState: Any!](./displaystate.md)
  The current display state of the [`previewItem`](./previewitem.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/autostarts)*