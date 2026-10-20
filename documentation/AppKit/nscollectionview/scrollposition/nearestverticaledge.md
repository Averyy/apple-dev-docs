# nearestVerticalEdge

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Scroll so that the bounding box is adjacent to the nearest edge (leading or trailing) of the collection view. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](./left.md), [`centeredHorizontally`](./centeredhorizontally.md), [`right`](./right.md), [`leadingEdge`](./leadingedge.md), or [`trailingEdge`](./trailingedge.md) options, but may be combined with other options.

**Availability**:
- macOS

## Declaration

```swift
static var nearestVerticalEdge: NSCollectionView.ScrollPosition { get }
```

```c
NSCollectionViewScrollPositionNearestVerticalEdge
```

## See Also

### Constants
- [static var top: NSCollectionView.ScrollPosition](./top.md)
  Scroll so that the top edge of the selected items’ bounding box is adjacent to the top edge of the collection view’s bounds. This option must not be combined with the [`centeredVertically`](./centeredvertically.md), [`bottom`](./bottom.md), and [`nearestHorizontalEdge`](./nearesthorizontaledge.md) options, but may be combined with other options.
- [static var centeredVertically: NSCollectionView.ScrollPosition](./centeredvertically.md)
  Scroll so that the bounding box of the selected items is centered vertically in the collection view’s bounds. This option must not be combined with the [`top`](./top.md), [`bottom`](./bottom.md), or [`nearestHorizontalEdge`](./nearesthorizontaledge.md) options, but may be combined with other options.
- [static var bottom: NSCollectionView.ScrollPosition](./bottom.md)
  Scroll so that the bottom edge of the bounding box is adjacent to the bottom of the collection view’s bounds. This option must not be combined with the [`top`](./top.md), [`centeredVertically`](./centeredvertically.md), or [`nearestHorizontalEdge`](./nearesthorizontaledge.md) options, but may be combined with other options.
- [static var nearestHorizontalEdge: NSCollectionView.ScrollPosition](./nearesthorizontaledge.md)
  Scroll so that the bounding box is adjacent to the nearest edge (top or bottom) of the collection view. This option must not be combined with the [`top`](./top.md), [`centeredVertically`](./centeredvertically.md), or [`bottom`](./bottom.md) options, but may be combined with other options.
- [static var left: NSCollectionView.ScrollPosition](./left.md)
  Scroll so that the left edge of the selected items’ bounding box is adjacent to the left edge of the collection view’s bounds. This option must not be combined with the [`centeredHorizontally`](./centeredhorizontally.md), [`right`](./right.md), [`leadingEdge`](./leadingedge.md), [`trailingEdge`](./trailingedge.md), or [`nearestVerticalEdge`](./nearestverticaledge.md) options, but may be combined with other options.
- [static var centeredHorizontally: NSCollectionView.ScrollPosition](./centeredhorizontally.md)
  Scroll so that the selected items’ bounding box is centered horizontally in the collection view’s bounds. This option must not be combined with the [`left`](./left.md),  [`right`](./right.md), [`leadingEdge`](./leadingedge.md), [`trailingEdge`](./trailingedge.md), or [`nearestVerticalEdge`](./nearestverticaledge.md) options, but may be combined with other options.
- [static var right: NSCollectionView.ScrollPosition](./right.md)
  Scroll so that the right edge of the selected items’ bounding box is adjacent to the right edge of the collection view’s bounds. This option must not be combined with the [`left`](./left.md), [`centeredHorizontally`](./centeredhorizontally.md), [`leadingEdge`](./leadingedge.md), [`trailingEdge`](./trailingedge.md), or [`nearestVerticalEdge`](./nearestverticaledge.md) options, but may be combined with other options.
- [static var leadingEdge: NSCollectionView.ScrollPosition](./leadingedge.md)
  Scroll so that the leading edge of the selected items’ bounding box is adjacent to the leading edge of the collection view’s bounds. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](./left.md), [`centeredHorizontally`](./centeredhorizontally.md), [`right`](./right.md), [`trailingEdge`](./trailingedge.md), or [`nearestVerticalEdge`](./nearestverticaledge.md) options, but may be combined with other options.
- [static var trailingEdge: NSCollectionView.ScrollPosition](./trailingedge.md)
  Scroll so that the trailing edge of the selected items’ bounding box is adjacent to the trailing edge of the collection view’s bounds. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](./left.md), [`centeredHorizontally`](./centeredhorizontally.md), [`right`](./right.md), [`leadingEdge`](./leadingedge.md), or [`nearestVerticalEdge`](./nearestverticaledge.md) options, but may be combined with other options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/scrollposition/nearestverticaledge)*