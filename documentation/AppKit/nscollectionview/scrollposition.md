# NSCollectionView.ScrollPosition

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants indicating the options for scrolling the collection view’s content.

**Availability**:
- macOS

## Declaration

```swift
struct ScrollPosition
```

```c
enum NSCollectionViewScrollPosition : NSUInteger;
```

## Topics

### Constants
- [static var top: NSCollectionView.ScrollPosition](./scrollposition/top.md)
  Scroll so that the top edge of the selected items’ bounding box is adjacent to the top edge of the collection view’s bounds. This option must not be combined with the [`centeredVertically`](./scrollposition/centeredvertically.md), [`bottom`](./scrollposition/bottom.md), and [`nearestHorizontalEdge`](./scrollposition/nearesthorizontaledge.md) options, but may be combined with other options.
- [static var centeredVertically: NSCollectionView.ScrollPosition](./scrollposition/centeredvertically.md)
  Scroll so that the bounding box of the selected items is centered vertically in the collection view’s bounds. This option must not be combined with the [`top`](./scrollposition/top.md), [`bottom`](./scrollposition/bottom.md), or [`nearestHorizontalEdge`](./scrollposition/nearesthorizontaledge.md) options, but may be combined with other options.
- [static var bottom: NSCollectionView.ScrollPosition](./scrollposition/bottom.md)
  Scroll so that the bottom edge of the bounding box is adjacent to the bottom of the collection view’s bounds. This option must not be combined with the [`top`](./scrollposition/top.md), [`centeredVertically`](./scrollposition/centeredvertically.md), or [`nearestHorizontalEdge`](./scrollposition/nearesthorizontaledge.md) options, but may be combined with other options.
- [static var nearestHorizontalEdge: NSCollectionView.ScrollPosition](./scrollposition/nearesthorizontaledge.md)
  Scroll so that the bounding box is adjacent to the nearest edge (top or bottom) of the collection view. This option must not be combined with the [`top`](./scrollposition/top.md), [`centeredVertically`](./scrollposition/centeredvertically.md), or [`bottom`](./scrollposition/bottom.md) options, but may be combined with other options.
- [static var left: NSCollectionView.ScrollPosition](./scrollposition/left.md)
  Scroll so that the left edge of the selected items’ bounding box is adjacent to the left edge of the collection view’s bounds. This option must not be combined with the [`centeredHorizontally`](./scrollposition/centeredhorizontally.md), [`right`](./scrollposition/right.md), [`leadingEdge`](./scrollposition/leadingedge.md), [`trailingEdge`](./scrollposition/trailingedge.md), or [`nearestVerticalEdge`](./scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var centeredHorizontally: NSCollectionView.ScrollPosition](./scrollposition/centeredhorizontally.md)
  Scroll so that the selected items’ bounding box is centered horizontally in the collection view’s bounds. This option must not be combined with the [`left`](./scrollposition/left.md),  [`right`](./scrollposition/right.md), [`leadingEdge`](./scrollposition/leadingedge.md), [`trailingEdge`](./scrollposition/trailingedge.md), or [`nearestVerticalEdge`](./scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var right: NSCollectionView.ScrollPosition](./scrollposition/right.md)
  Scroll so that the right edge of the selected items’ bounding box is adjacent to the right edge of the collection view’s bounds. This option must not be combined with the [`left`](./scrollposition/left.md), [`centeredHorizontally`](./scrollposition/centeredhorizontally.md), [`leadingEdge`](./scrollposition/leadingedge.md), [`trailingEdge`](./scrollposition/trailingedge.md), or [`nearestVerticalEdge`](./scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var leadingEdge: NSCollectionView.ScrollPosition](./scrollposition/leadingedge.md)
  Scroll so that the leading edge of the selected items’ bounding box is adjacent to the leading edge of the collection view’s bounds. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](./scrollposition/left.md), [`centeredHorizontally`](./scrollposition/centeredhorizontally.md), [`right`](./scrollposition/right.md), [`trailingEdge`](./scrollposition/trailingedge.md), or [`nearestVerticalEdge`](./scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var trailingEdge: NSCollectionView.ScrollPosition](./scrollposition/trailingedge.md)
  Scroll so that the trailing edge of the selected items’ bounding box is adjacent to the trailing edge of the collection view’s bounds. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](./scrollposition/left.md), [`centeredHorizontally`](./scrollposition/centeredhorizontally.md), [`right`](./scrollposition/right.md), [`leadingEdge`](./scrollposition/leadingedge.md), or [`nearestVerticalEdge`](./scrollposition/nearestverticaledge.md) options, but may be combined with other options.
- [static var nearestVerticalEdge: NSCollectionView.ScrollPosition](./scrollposition/nearestverticaledge.md)
  Scroll so that the bounding box is adjacent to the nearest edge (leading or trailing) of the collection view. Use this option to support both left-to-right and right-to-left layouts appropriately. This option must not be combined with the [`left`](./scrollposition/left.md), [`centeredHorizontally`](./scrollposition/centeredhorizontally.md), [`right`](./scrollposition/right.md), [`leadingEdge`](./scrollposition/leadingedge.md), or [`trailingEdge`](./scrollposition/trailingedge.md) options, but may be combined with other options.
- [NSCollectionViewScrollPositionNone](../nscollectionviewscrollposition/nscollectionviewscrollpositionnone.md)
  Do not scroll.
### Initializers
- [init(rawValue: UInt)](./scrollposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NSCollectionView.DropOperation](./dropoperation.md)
  These constants specify if acceptance of a drop should be at the item it is dropped on or before the item. These constants are used by the  [`collectionView(_:acceptDrop:index:dropOperation:)`](../nscollectionviewdelegate/collectionview%28_,acceptdrop,index,dropoperation%29.md) and [`collectionView(_:validateDrop:proposedIndex:dropOperation:)`](../nscollectionviewdelegate/collectionview%28_,validatedrop,proposedindex,dropoperation%29.md) methods in [`NSCollectionViewDelegate`](../nscollectionviewdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/scrollposition)*