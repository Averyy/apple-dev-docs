# previewItemURL

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The URL of the item to preview.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var previewItemURL: URL! { get }
```

```objc
@property (readonly) NSURL * previewItemURL;
```

#### Discussion

[`QLPreviewController`](../../QuickLook/qlpreviewcontroller.md) uses this property to get an item’s URL. In typical use, you’d implement a getter method in your preview item class to provide this value.

The value of this property must be a file-type URL.

If the item isn’t available for preview, this property’s getter method should return `nil`. In this case, the [`QLPreviewController`](../../QuickLook/qlpreviewcontroller.md) displays a “loading” view. Use [`refreshCurrentPreviewItem()`](../../QuickLook/qlpreviewcontroller/refreshcurrentpreviewitem%28%29.md) to reload the item once the URL content is available.

## See Also

### Instance Properties
- [var previewItemDisplayState: Any!](./previewitemdisplaystate.md)
  The display state for the preview item.
- [var previewItemTitle: String!](./previewitemtitle.md)
  The title to display for the preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewitem/previewitemurl)*