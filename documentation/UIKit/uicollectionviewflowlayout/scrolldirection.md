# scrollDirection

**Framework**: UIKit  
**Kind**: property

The scroll direction of the grid.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scrollDirection: UICollectionView.ScrollDirection { get set }
```

#### Discussion

The grid layout scrolls along one axis only, either horizontally or vertically. For the non scrolling axis, the width of the collection view in that dimension serves as starting width of the content.

The default value of this property is [`UICollectionView.ScrollDirection.vertical`](uicollectionview/scrolldirection/vertical.md).

## See Also

- [UICollectionView.ScrollDirection](uicollectionview/scrolldirection.md)
  Constants that indicate the direction of scrolling for the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/scrolldirection)*