# refreshCurrentPreviewItem()

**Framework**: Quick Look  
**Kind**: method

Asks the Quick Look preview controller to recompute the display of the current preview item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func refreshCurrentPreviewItem()
```

#### Discussion

Quick Look recomputes the display regardless of whether the current preview item changes.

## See Also

- [var currentPreviewItem: (any QLPreviewItem)?](qlpreviewcontroller/currentpreviewitem.md)
  The item displaying in the Quick Look preview controller.
- [var currentPreviewItemIndex: Int](qlpreviewcontroller/currentpreviewitemindex.md)
  The index within the preview item navigation list of the item displaying in the Quick Look preview controller.
- [func reloadData()](qlpreviewcontroller/reloaddata.md)
  Asks the preview controller to reload its data from its data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/refreshcurrentpreviewitem())*