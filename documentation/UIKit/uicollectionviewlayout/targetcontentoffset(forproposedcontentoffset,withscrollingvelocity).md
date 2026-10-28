# targetContentOffset(forProposedContentOffset:withScrollingVelocity:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the point at which to stop scrolling.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func targetContentOffset(forProposedContentOffset proposedContentOffset: CGPoint, withScrollingVelocity velocity: CGPoint) -> CGPoint
```

```objc
- (CGPoint) targetContentOffsetForProposedContentOffset:(CGPoint) proposedContentOffset withScrollingVelocity:(CGPoint) velocity;
```

## Return Value

The content offset that you want to use instead. This value reflects the adjusted upper-left corner of the visible area. The default implementation of this method returns the value in the `proposedContentOffset` parameter.

## Discussion

If you want the scrolling behavior to snap to specific boundaries, you can override this method and use it to change the point at which to stop. For example, you might use this method to always stop scrolling on a boundary between items, as opposed to stopping in the middle of an item.

## Parameters

- `proposedContentOffset`: The proposed point (in the collection view’s content view) at which to stop scrolling. This is the value at which scrolling would naturally stop if no adjustments were made. The point reflects the upper-left corner of the visible content.
- `velocity`: The current scrolling velocity along both the horizontal and vertical axes. This value is measured in points per second.

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
- [func targetContentOffset(forProposedContentOffset: CGPoint) -> CGPoint](./targetcontentoffset%28forproposedcontentoffset%29.md)
  Retrieves the content offset to use after an animated layout update or change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:))*