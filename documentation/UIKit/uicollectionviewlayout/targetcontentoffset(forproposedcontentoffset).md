# targetContentOffset(forProposedContentOffset:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the content offset to use after an animated layout update or change.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func targetContentOffset(forProposedContentOffset proposedContentOffset: CGPoint) -> CGPoint
```

```objc
- (CGPoint) targetContentOffsetForProposedContentOffset:(CGPoint) proposedContentOffset;
```

## Return Value

The content offset that you want to use instead. The default implementation of this method returns the value in the `proposedContentOffset` parameter.

## Discussion

During layout updates, or when transitioning between layouts, the collection view calls this method to give you the opportunity to change the proposed content offset to use at the end of the animation. You might override this method if the animations or transition might cause items to be positioned in a way that is not optimal for your design.

The collection view calls this method after calling the [`prepare()`](./prepare%28%29.md) and [`collectionViewContentSize`](./collectionviewcontentsize.md) methods.

## Parameters

- `proposedContentOffset`: The proposed point (in the coordinate space of the collection view’s content view) for the upper-left corner of the visible content. This represents the point that the collection view has calculated as the most likely value to use at the end of the animation.

## See Also

### Providing layout attributes
- [class var layoutAttributesClass: AnyClass](./layoutattributesclass.md)
  The class to use when creating layout attributes objects.
- [func prepare()](./prepare%28%29.md)
  Tells the layout object to update the current layout.
- [func layoutAttributesForElements(in: CGRect) -> [UICollectionViewLayoutAttributes]?](./layoutattributesforelements%28in%29.md)
  Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [func layoutAttributesForItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesforitem%28at%29.md)
  Retrieves layout information for an item at the specified index path with a corresponding cell.
- [func layoutAttributesForInteractivelyMovingItem(at: IndexPath, withTargetPosition: CGPoint) -> UICollectionViewLayoutAttributes](./layoutattributesforinteractivelymovingitem%28at,withtargetposition%29.md)
  Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [func layoutAttributesForSupplementaryView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesforsupplementaryview%28ofkind,at%29.md)
  Retrieves the layout attributes for the specified supplementary view.
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesfordecorationview%28ofkind,at%29.md)
  Retrieves the layout attributes for the specified decoration view.
- [func targetContentOffset(forProposedContentOffset: CGPoint, withScrollingVelocity: CGPoint) -> CGPoint](./targetcontentoffset%28forproposedcontentoffset,withscrollingvelocity%29.md)
  Retrieves the point at which to stop scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:))*