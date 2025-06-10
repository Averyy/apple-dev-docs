# UICollectionView.ScrollPosition

**Framework**: UIKit  
**Kind**: struct

Constants that indicate how to scroll an item into the visible portion of the collection view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct ScrollPosition
```

## Topics

### Constants
- [static var top: UICollectionView.ScrollPosition](uicollectionview/scrollposition/top.md)
  Scroll so that the item is positioned at the top of the collection view’s bounds.
- [static var centeredVertically: UICollectionView.ScrollPosition](uicollectionview/scrollposition/centeredvertically.md)
  Scroll so that the item is centered vertically in the collection view.
- [static var bottom: UICollectionView.ScrollPosition](uicollectionview/scrollposition/bottom.md)
  Scroll so that the item is positioned at the bottom of the collection view’s bounds.
- [static var left: UICollectionView.ScrollPosition](uicollectionview/scrollposition/left.md)
  Scroll so that the item is positioned at the left edge of the collection view’s bounds.
- [static var centeredHorizontally: UICollectionView.ScrollPosition](uicollectionview/scrollposition/centeredhorizontally.md)
  Scroll so that the item is centered horizontally in the collection view.
- [static var right: UICollectionView.ScrollPosition](uicollectionview/scrollposition/right.md)
  Scroll so that the item is positioned at the right edge of the collection view’s bounds.
### Initializers
- [init(rawValue: UInt)](uicollectionview/scrollposition/init(rawvalue:).md)
  Creates a scroll-position structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func scrollToItem(at: IndexPath, at: UICollectionView.ScrollPosition, animated: Bool)](uicollectionview/scrolltoitem(at:at:animated:).md)
  Scrolls the collection view contents until the specified item is visible.
- [UICollectionView.ScrollDirection](uicollectionview/scrolldirection.md)
  Constants that indicate the direction of scrolling for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/scrollposition)*