# scrollDirection

**Framework**: AppKit  
**Kind**: property

The scroll direction of the layout.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var scrollDirection: NSCollectionView.ScrollDirection { get set }
```

#### Discussion

The flow layout scrolls along one axis only, either horizontally or vertically. When the scroll direction is [`NSCollectionView.ScrollDirection.vertical`](nscollectionview/scrolldirection/vertical.md), the width of the content never exceeds the width of the collection view itself but the height grows as needed to accommodate the current items. When the scroll direction is [`NSCollectionView.ScrollDirection.horizontal`](nscollectionview/scrolldirection/horizontal.md), the height never exceeds the height of the collection view but the width grows as needed.

The default value of this property is [`NSCollectionView.ScrollDirection.vertical`](nscollectionview/scrolldirection/vertical.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/scrolldirection)*