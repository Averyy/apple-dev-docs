# UICollectionView.ScrollDirection

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the direction of scrolling for the layout.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum ScrollDirection
```

```c
enum UICollectionViewScrollDirection : NSInteger;
```

## Topics

### Constants
- [UICollectionView.ScrollDirection.vertical](./scrolldirection/vertical.md)
  The layout scrolls content vertically.
- [UICollectionView.ScrollDirection.horizontal](./scrolldirection/horizontal.md)
  The layout scrolls content horizontally.
### Initializers
- [init?(rawValue: Int)](./scrolldirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Scrolling an item into view
- [func scrollToItem(at: IndexPath, at: UICollectionView.ScrollPosition, animated: Bool)](./scrolltoitem%28at,at,animated%29.md)
  Scrolls the collection view contents until the specified item is visible.
- [UICollectionView.ScrollPosition](./scrollposition.md)
  Constants that indicate how to scroll an item into the visible portion of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/scrolldirection)*