# layoutAttributesForInteractivelyMovingItem(at:withTargetPosition:)

**Framework**: UIKit  
**Kind**: method

Retrieves the layout attributes of an item when it is being moved interactively by the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func layoutAttributesForInteractivelyMovingItem(at indexPath: IndexPath, withTargetPosition position: CGPoint) -> UICollectionViewLayoutAttributes
```

#### Return Value

The layout attributes of the item while it is at the specified position.

#### Discussion

When an item is moving because of user interactivity, the layout object uses this method to retrieve layout attributes to use for the item while it is at the specified position. The default implementation of this method returns a copy of the item’s existing attributes with two changes: the [`center`](uicollectionviewlayoutattributes/center.md) point is set to the value in `position` and the [`zIndex`](uicollectionviewlayoutattributes/zindex.md) value is set to [`NSIntegerMax`](https://developer.apple.com/documentation/ObjectiveC/NSIntegerMax) so that the item floats above other items in the collection view.

Subclasses can override this method and modify additional layout attributes as needed. If you override this method, call `super` first to retrieve the item’s existing attributes and then make your changes to the returned structure.

## Parameters

- `indexPath`: The index path of the item being moved.
- `position`: The current position of the item in the collection view’s coordinate system.

## See Also

- [class var layoutAttributesClass: AnyClass](uicollectionviewlayout/layoutattributesclass.md)
  The class to use when creating layout attributes objects.
- [func prepare()](uicollectionviewlayout/prepare.md)
  Tells the layout object to update the current layout.
- [func layoutAttributesForElements(in: CGRect) -> [UICollectionViewLayoutAttributes]?](uicollectionviewlayout/layoutattributesforelements(in:).md)
  Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [func layoutAttributesForItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesforitem(at:).md)
  Retrieves layout information for an item at the specified index path with a corresponding cell.
- [func layoutAttributesForSupplementaryView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md)
  Retrieves the layout attributes for the specified supplementary view.
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md)
  Retrieves the layout attributes for the specified decoration view.
- [func targetContentOffset(forProposedContentOffset: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md)
  Retrieves the content offset to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: CGPoint, withScrollingVelocity: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Retrieves the point at which to stop scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesforinteractivelymovingitem(at:withtargetposition:))*