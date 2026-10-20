# scrollToItem(at:at:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the collection view contents until the specified item is visible.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func scrollToItem(at indexPath: IndexPath, at scrollPosition: UICollectionView.ScrollPosition, animated: Bool)
```

```objc
- (void) scrollToItemAtIndexPath:(NSIndexPath *) indexPath atScrollPosition:(UICollectionViewScrollPosition) scrollPosition animated:(BOOL) animated;
```

## Parameters

- `indexPath`: The index path of the item to scroll into view.
- `scrollPosition`: An option that specifies where the item should be positioned when scrolling finishes. For a list of possible values, see [`UICollectionView.ScrollPosition`](./scrollposition.md).
- `animated`: Specify [`true`](../../Swift/true.md) to animate the scrolling behavior or [`false`](../../Swift/false.md) to adjust the scroll view’s visible content immediately.

## See Also

### Scrolling an item into view
- [UICollectionView.ScrollPosition](./scrollposition.md)
  Constants that indicate how to scroll an item into the visible portion of the collection view.
- [UICollectionView.ScrollDirection](./scrolldirection.md)
  Constants that indicate the direction of scrolling for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/scrolltoitem(at:at:animated:))*