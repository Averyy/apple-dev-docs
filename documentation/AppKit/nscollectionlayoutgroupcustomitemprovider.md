# NSCollectionLayoutGroupCustomItemProvider

**Framework**: AppKit  
**Kind**: typealias

A closure that creates and returns each of the custom group’s items.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias NSCollectionLayoutGroupCustomItemProvider = (any NSCollectionLayoutEnvironment) -> [NSCollectionLayoutGroupCustomItem]
```

#### Discussion

You use a custom item provider to supply the item arrangement when creating a group using the [`custom(layoutSize:itemProvider:)`](nscollectionlayoutgroup/custom(layoutsize:itemprovider:).md) initializer.

## See Also

- [class NSCollectionLayoutGroupCustomItem](nscollectionlayoutgroupcustomitem.md)
  An item used in a group with a custom layout arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroupcustomitemprovider)*