# canPreview(_:)

**Framework**: Quick Look  
**Kind**: method

Returns a Boolean value that indicates whether the preview controller can display an item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func canPreview(_ item: any QLPreviewItem) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the Quick Look preview controller can display the specified preview item.

#### Discussion

If the system can’t display an item, but you still attempt to display it, a Quick Look preview controller displays a generic error. Always check whether you can display an item before choosing to do so.

For supported file types, see [`QLPreviewController`](qlpreviewcontroller.md).

## Parameters

- `item`: An item to preview.

## See Also

- [var currentPreviewItem: (any QLPreviewItem)?](qlpreviewcontroller/currentpreviewitem.md)
  The item displaying in the Quick Look preview controller.
- [var currentPreviewItemIndex: Int](qlpreviewcontroller/currentpreviewitemindex.md)
  The index within the preview item navigation list of the item displaying in the Quick Look preview controller.
- [func refreshCurrentPreviewItem()](qlpreviewcontroller/refreshcurrentpreviewitem.md)
  Asks the Quick Look preview controller to recompute the display of the current preview item.
- [func reloadData()](qlpreviewcontroller/reloaddata.md)
  Asks the preview controller to reload its data from its data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/canpreview(_:))*