# UICollectionView.ScrollPosition

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate how to scroll an item into the visible portion of the collection view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct ScrollPosition
```

```c
enum UICollectionViewScrollPosition : NSUInteger;
```

## Topics

### Constants
- [static var top: UICollectionView.ScrollPosition](./scrollposition/top.md)
  Scroll so that the item is positioned at the top of the collection view’s bounds.
- [static var centeredVertically: UICollectionView.ScrollPosition](./scrollposition/centeredvertically.md)
  Scroll so that the item is centered vertically in the collection view.
- [static var bottom: UICollectionView.ScrollPosition](./scrollposition/bottom.md)
  Scroll so that the item is positioned at the bottom of the collection view’s bounds.
- [static var left: UICollectionView.ScrollPosition](./scrollposition/left.md)
  Scroll so that the item is positioned at the left edge of the collection view’s bounds.
- [static var centeredHorizontally: UICollectionView.ScrollPosition](./scrollposition/centeredhorizontally.md)
  Scroll so that the item is centered horizontally in the collection view.
- [static var right: UICollectionView.ScrollPosition](./scrollposition/right.md)
  Scroll so that the item is positioned at the right edge of the collection view’s bounds.
- [UICollectionViewScrollPositionNone](../uicollectionviewscrollposition/uicollectionviewscrollpositionnone.md)
  Don’t scroll the item into view.
### Initializers
- [init(rawValue: UInt)](./scrollposition/init%28rawvalue%29.md)
  Creates a scroll-position structure with the specified raw value.

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

### Scrolling an item into view
- [func scrollToItem(at: IndexPath, at: UICollectionView.ScrollPosition, animated: Bool)](./scrolltoitem%28at,at,animated%29.md)
  Scrolls the collection view contents until the specified item is visible.
- [UICollectionView.ScrollDirection](./scrolldirection.md)
  Constants that indicate the direction of scrolling for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/scrollposition)*