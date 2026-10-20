# canPreview(_:)

**Framework**: Quick Look  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the preview controller can display an item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
class func canPreview(_ item: any QLPreviewItem) -> Bool
```

*Mac Catalyst*

```swift
class func canPreviewItem(_ item: any QLPreviewItem) -> Bool
```

```objc
+ (BOOL) canPreviewItem:(id<QLPreviewItem>) item;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if the Quick Look preview controller can display the specified preview item.

#### Discussion

If the system can’t display an item, but you still attempt to display it, a Quick Look preview controller displays a generic error. Always check whether you can display an item before choosing to do so.

For supported file types, see [`QLPreviewController`](../qlpreviewcontroller.md).

## Parameters

- `item`: An item to preview.

## See Also

### Managing item previews
- [var currentPreviewItem: (any QLPreviewItem)?](./currentpreviewitem.md)
  The item displaying in the Quick Look preview controller.
- [var currentPreviewItemIndex: Int](./currentpreviewitemindex.md)
  The index within the preview item navigation list of the item displaying in the Quick Look preview controller.
- [func refreshCurrentPreviewItem()](./refreshcurrentpreviewitem%28%29.md)
  Asks the Quick Look preview controller to recompute the display of the current preview item.
- [func reloadData()](./reloaddata%28%29.md)
  Asks the preview controller to reload its data from its data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/canpreview(_:))*