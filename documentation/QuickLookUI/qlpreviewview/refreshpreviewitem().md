# refreshPreviewItem()

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

Updates the preview to display the currently previewed item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func refreshPreviewItem()
```

```objc
- (void) refreshPreviewItem;
```

## Discussion

When you modify the object that the [`previewItem`](./previewitem.md) property points to, call this method to generate and display the new preview.

## See Also

### Displaying a Preview
- [var previewItem: (any QLPreviewItem)!](./previewitem.md)
  The item to preview.
- [var displayState: Any!](./displaystate.md)
  The current display state of the [`previewItem`](./previewitem.md).
- [var autostarts: Bool](./autostarts.md)
  A Boolean value that determines whether the preview starts automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/refreshpreviewitem())*