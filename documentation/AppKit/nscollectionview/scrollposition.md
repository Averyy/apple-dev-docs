# NSCollectionView.ScrollPosition

**Framework**: AppKit  
**Kind**: struct

Constants indicating the options for scrolling the collection view’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ScrollPosition
```

## Topics

### Constants
- [static var top: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/top.md)
  Scroll so that the top edge of the selected items’ bounding box is adjacent to the top edge of the collection view’s bounds. This option must not be combined with the [`centeredVertically`](nscollectionview/scrollposition/centeredvertically.md), [`bottom`](nscollectionview/scrollposition/bottom.md), and [`nearestHorizontalEdge`](nscollectionview/scrollposition/nearesthorizontaledge.md) options, but may be combined with other options.
- [static var centeredVertically: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/centeredvertically.md)
  Scroll so that the bounding box of the selected items is centered vertically in the collection view’s bounds. This option must not be combined with the [`top`](nscollectionview/scrollposition/top.md), [`bottom`](nscollectionview/scrollposition/bottom.md), or [`nearestHorizontalEdge`](nscollectionview/scrollposition/nearesthorizontaledge.md) options, but may be combined with other options.
- [static var bottom: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/bottom.md)
  Scroll so that the bottom edge of the bounding box is adjacent to the bottom of the collection view’s bounds. This option must not be combined with the [`top`](nscollectionview/scrollposition/top.md), [`centeredVertically`](nscollectionview/scrollposition/centeredvertically.md), or [`nearestHorizontalEdge`](nscollectionview/scrollposition/nearesthorizontaledge.md) options, but may be combined with other options.
- [static var nearestHorizontalEdge: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/nearesthorizontaledge.md)
  Scroll so that the bounding box is adjacent to the nearest edge (top or bottom) of the collection view. This option must not be combined with the [`top`](nscollectionview/scrollposition/top.md), [`centeredVertically`](nscollectionview/scrollposition/centeredvertically.md), or [`bottom`](nscollectionview/scrollposition/bottom.md) options, but may be combined with other options.
- [static var left: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/left.md)
  Scroll so that the left edge of the selected items’ bounding box is adjacent to the left edge of the collection view’s bounds. This option must not be combined with the [`centeredHorizontally`](nscollectionview/scrollposition/centeredhorizontally.md), [`right`](nscollectionview/scrollposition/right.md), [`leadingEdge`](nscollectionview/scrollposition/leadingedge.md), [`trailingEdge`](nscollectionview/scrollposition/trailingedge.md), or [`nearestVerticalEdge`](nscollectionview/scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var centeredHorizontally: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/centeredhorizontally.md)
  Scroll so that the selected items’ bounding box is centered horizontally in the collection view’s bounds. This option must not be combined with the [`left`](nscollectionview/scrollposition/left.md),  [`right`](nscollectionview/scrollposition/right.md), [`leadingEdge`](nscollectionview/scrollposition/leadingedge.md), [`trailingEdge`](nscollectionview/scrollposition/trailingedge.md), or [`nearestVerticalEdge`](nscollectionview/scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var right: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/right.md)
  Scroll so that the right edge of the selected items’ bounding box is adjacent to the right edge of the collection view’s bounds. This option must not be combined with the [`left`](nscollectionview/scrollposition/left.md), [`centeredHorizontally`](nscollectionview/scrollposition/centeredhorizontally.md), [`leadingEdge`](nscollectionview/scrollposition/leadingedge.md), [`trailingEdge`](nscollectionview/scrollposition/trailingedge.md), or [`nearestVerticalEdge`](nscollectionview/scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var leadingEdge: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/leadingedge.md)
  Scroll so that the leading edge of the selected items’ bounding box is adjacent to the leading edge of the collection view’s bounds. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](nscollectionview/scrollposition/left.md), [`centeredHorizontally`](nscollectionview/scrollposition/centeredhorizontally.md), [`right`](nscollectionview/scrollposition/right.md), [`trailingEdge`](nscollectionview/scrollposition/trailingedge.md), or [`nearestVerticalEdge`](nscollectionview/scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var trailingEdge: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/trailingedge.md)
  Scroll so that the trailing edge of the selected items’ bounding box is adjacent to the trailing edge of the collection view’s bounds. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](nscollectionview/scrollposition/left.md), [`centeredHorizontally`](nscollectionview/scrollposition/centeredhorizontally.md), [`right`](nscollectionview/scrollposition/right.md), [`leadingEdge`](nscollectionview/scrollposition/leadingedge.md), or [`nearestVerticalEdge`](nscollectionview/scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var nearestVerticalEdge: NSCollectionView.ScrollPosition](nscollectionview/scrollposition/nearestverticaledge.md)
  Scroll so that the bounding box is adjacent to the nearest edge (leading or trailing) of the collection view. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](nscollectionview/scrollposition/left.md), [`centeredHorizontally`](nscollectionview/scrollposition/centeredhorizontally.md), [`right`](nscollectionview/scrollposition/right.md), [`leadingEdge`](nscollectionview/scrollposition/leadingedge.md), or [`trailingEdge`](nscollectionview/scrollposition/trailingedge.md) options, but may be combined with other options.
### Initializers
- [init(rawValue: UInt)](nscollectionview/scrollposition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSCollectionView.DropOperation](nscollectionview/dropoperation.md)
  These constants specify if acceptance of a drop should be at the item it is dropped on or before the item. These constants are used by the  [`collectionView(_:acceptDrop:index:dropOperation:)`](nscollectionviewdelegate/collectionview(_:acceptdrop:index:dropoperation:).md) and [`collectionView(_:validateDrop:proposedIndex:dropOperation:)`](nscollectionviewdelegate/collectionview(_:validatedrop:proposedindex:dropoperation:).md) methods in [`NSCollectionViewDelegate`](nscollectionviewdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/scrollposition)*