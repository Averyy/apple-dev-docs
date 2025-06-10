# layoutAttributesForDecorationView(ofKind:at:)

**Framework**: UIKit  
**Kind**: method

Retrieves the layout attributes for the specified decoration view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func layoutAttributesForDecorationView(ofKind elementKind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

#### Return Value

A layout attributes object containing the information to apply to the decoration view.

#### Discussion

If your layout object defines any decoration views, you must override this method and use it to return layout information for those views.

## Parameters

- `elementKind`: A string that identifies the type of the decoration view.
- `indexPath`: The index path of the decoration view.

## See Also

- [class var layoutAttributesClass: AnyClass](uicollectionviewlayout/layoutattributesclass.md)
  The class to use when creating layout attributes objects.
- [func prepare()](uicollectionviewlayout/prepare.md)
  Tells the layout object to update the current layout.
- [func layoutAttributesForElements(in: CGRect) -> [UICollectionViewLayoutAttributes]?](uicollectionviewlayout/layoutattributesforelements(in:).md)
  Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [func layoutAttributesForItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesforitem(at:).md)
  Retrieves layout information for an item at the specified index path with a corresponding cell.
- [func layoutAttributesForInteractivelyMovingItem(at: IndexPath, withTargetPosition: CGPoint) -> UICollectionViewLayoutAttributes](uicollectionviewlayout/layoutattributesforinteractivelymovingitem(at:withtargetposition:).md)
  Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [func layoutAttributesForSupplementaryView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md)
  Retrieves the layout attributes for the specified supplementary view.
- [func targetContentOffset(forProposedContentOffset: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md)
  Retrieves the content offset to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: CGPoint, withScrollingVelocity: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Retrieves the point at which to stop scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesfordecorationview(ofkind:at:))*