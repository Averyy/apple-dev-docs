# edgeSpacing

**Framework**: UIKit  
**Kind**: property

The amount of space added around the boundaries of the item between other items and this item’s container.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var edgeSpacing: NSCollectionLayoutEdgeSpacing? { get set }
```

#### Discussion

Use this property to adjust the position of the item in relation to its container and other items. For example, you can use this property to apply extra space to the trailing edge of each item. Edge spacing is applied before applying [`contentInsets`](nscollectionlayoutitem/contentinsets.md).

The following diagram shows the result of applying 2 points of trailing edge spacing to the items in a group:

![Two diagrams that show the result of edge spacing applied to a group of items. The first diagram shows a group of three square items in a row, each item measuring 20 by 20 points. The second diagram shows a trailing edge spacing of 2 points applied to each item. Each item remains the same size, but moves 2 points if it’s on the trailing edge of the previous item in the group.](https://docs-assets.developer.apple.com/published/949b98d76415a0273cc29cd850d64611/media-3572326%402x.png)

## See Also

- [var contentInsets: NSDirectionalEdgeInsets](nscollectionlayoutitem/contentinsets.md)
  The amount of space added around the content of the item to adjust its final size after its position is computed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutitem/edgespacing)*