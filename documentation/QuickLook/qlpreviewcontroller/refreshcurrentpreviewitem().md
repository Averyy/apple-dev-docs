# refreshCurrentPreviewItem()

**Framework**: Quick Look  
**Kind**: method  
**Role**: Instance Method

Asks the Quick Look preview controller to recompute the display of the current preview item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func refreshCurrentPreviewItem()
```

```objc
- (void) refreshCurrentPreviewItem;
```

## Discussion

Quick Look recomputes the display regardless of whether the current preview item changes.

## See Also

### Managing item previews
- [class func canPreview(any QLPreviewItem) -> Bool](./canpreview%28_%29.md)
  Returns a Boolean value that indicates whether the preview controller can display an item.
- [var currentPreviewItem: (any QLPreviewItem)?](./currentpreviewitem.md)
  The item displaying in the Quick Look preview controller.
- [var currentPreviewItemIndex: Int](./currentpreviewitemindex.md)
  The index within the preview item navigation list of the item displaying in the Quick Look preview controller.
- [func reloadData()](./reloaddata%28%29.md)
  Asks the preview controller to reload its data from its data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/refreshcurrentpreviewitem())*