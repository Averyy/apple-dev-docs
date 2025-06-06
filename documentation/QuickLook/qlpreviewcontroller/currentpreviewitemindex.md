# currentPreviewItemIndex

**Framework**: Quick Look  
**Kind**: property

The index within the preview item navigation list of the item displaying in the Quick Look preview controller.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var currentPreviewItemIndex: Int { get set }
```

#### Discussion

You can change which item the preview controller displays, among those in a navigation list, by setting this property’s value. If the preview controller isn’t displaying an item, this property’s value is `NSNotFound`.

## See Also

- [class func canPreview(any QLPreviewItem) -> Bool](qlpreviewcontroller/canpreview(_:).md)
  Returns a Boolean value that indicates whether the preview controller can display an item.
- [var currentPreviewItem: (any QLPreviewItem)?](qlpreviewcontroller/currentpreviewitem.md)
  The item displaying in the Quick Look preview controller.
- [func refreshCurrentPreviewItem()](qlpreviewcontroller/refreshcurrentpreviewitem.md)
  Asks the Quick Look preview controller to recompute the display of the current preview item.
- [func reloadData()](qlpreviewcontroller/reloaddata.md)
  Asks the preview controller to reload its data from its data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/currentpreviewitemindex)*