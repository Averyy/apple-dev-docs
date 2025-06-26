# reloadData()

**Framework**: Quick Look  
**Kind**: method

Asks the preview controller to reload its data from its data source.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reloadData()
```

#### Discussion

Quick Look recomputes the displayed data only if the current preview item changes.

## See Also

- [var currentPreviewItem: (any QLPreviewItem)?](qlpreviewcontroller/currentpreviewitem.md)
  The item displaying in the Quick Look preview controller.
- [var currentPreviewItemIndex: Int](qlpreviewcontroller/currentpreviewitemindex.md)
  The index within the preview item navigation list of the item displaying in the Quick Look preview controller.
- [func refreshCurrentPreviewItem()](qlpreviewcontroller/refreshcurrentpreviewitem.md)
  Asks the Quick Look preview controller to recompute the display of the current preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller/reloaddata())*