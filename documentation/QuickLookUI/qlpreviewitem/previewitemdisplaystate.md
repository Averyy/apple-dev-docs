# previewItemDisplayState

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property

The display state for the preview item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional var previewItemDisplayState: Any! { get }
```

```objc
@property (readonly) id previewItemDisplayState;
```

## Discussion

The display state is an opaque object used by the preview panel. You typically use the [`QLPreviewPanel`](../qlpreviewpanel.md) method [`displayState`](../qlpreviewpanel/displaystate.md) to retrieve the display state which you save for later use in the preview item. This way you can preserve the display state when the panel moves from or to another controller.

This property is optional.

## See Also

### Instance Properties
- [var previewItemTitle: String!](./previewitemtitle.md)
  The title to display for the preview item.
- [var previewItemURL: URL!](./previewitemurl.md)
  The URL of the item to preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewitem/previewitemdisplaystate)*