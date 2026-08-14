# scrollToItem(at:at:animated:)

**Framework**: UIKit  
**Kind**: method

Scrolls the collection view contents until the specified item is visible.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func scrollToItem(at indexPath: IndexPath, at scrollPosition: UICollectionView.ScrollPosition, animated: Bool)
```

## Parameters

- `indexPath`: The index path of the item to scroll into view.
- `scrollPosition`: An option that specifies where the item should be positioned when scrolling finishes. For a list of possible values, see [`UICollectionView.ScrollPosition`](uicollectionview/scrollposition.md).
- `animated`: Specify [`true`](https://developer.apple.com/documentation/swift/true) to animate the scrolling behavior or [`false`](https://developer.apple.com/documentation/swift/false) to adjust the scroll view’s visible content immediately.

## See Also

- [UICollectionView.ScrollPosition](uicollectionview/scrollposition.md)
  Constants that indicate how to scroll an item into the visible portion of the collection view.
- [UICollectionView.ScrollDirection](uicollectionview/scrolldirection.md)
  Constants that indicate the direction of scrolling for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/scrolltoitem(at:at:animated:))*