# previewItemURL

**Framework**: Quick Look UI  
**Kind**: property  
**Required**: Yes

The URL of the item to preview.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var previewItemURL: URL! { get }
```

#### Discussion

[`QLPreviewController`](https://developer.apple.com/documentation/QuickLook/QLPreviewController) uses this property to get an item’s URL. In typical use, you’d implement a getter method in your preview item class to provide this value.

The value of this property must be a file-type URL.

If the item isn’t available for preview, this property’s getter method should return `nil`. In this case, the [`QLPreviewController`](https://developer.apple.com/documentation/QuickLook/QLPreviewController) displays a “loading” view. Use [`refreshCurrentPreviewItem()`](https://developer.apple.com/documentation/QuickLook/QLPreviewController/refreshCurrentPreviewItem()) to reload the item once the URL content is available.

## See Also

- [var previewItemDisplayState: Any!](qlpreviewitem/previewitemdisplaystate.md)
  The display state for the preview item.
- [var previewItemTitle: String!](qlpreviewitem/previewitemtitle.md)
  The title to display for the preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewitem/previewitemurl)*