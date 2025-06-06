# NSCollectionLayoutSectionVisibleItemsInvalidationHandler

**Framework**: AppKit  
**Kind**: typealias

A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias NSCollectionLayoutSectionVisibleItemsInvalidationHandler = ([any NSCollectionLayoutVisibleItem], NSPoint, any NSCollectionLayoutEnvironment) -> Void
```

#### Discussion

Each section of a collection view layout can have a visible items invalidation handler. You use this handler to perform custom animations on the items currently visible within the bounds of that section. The handler is called before each layout cycle, any time an animation occurs in that section due to changes such as adding or removing items, scrolling the section, or rotating the device.

## See Also

- [protocol NSCollectionLayoutVisibleItem](nscollectionlayoutvisibleitem.md)
  An item that’s currently visible within the bounds of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsectionvisibleitemsinvalidationhandler)*