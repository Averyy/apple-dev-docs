# layoutAttributesClass

**Framework**: UIKit  
**Kind**: property

The class to use when creating layout attributes objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
class var layoutAttributesClass: AnyClass { get }
```

#### Return Value

The class to use for layout attributes objects.

#### Discussion

If you subclass [`UICollectionViewLayoutAttributes`](uicollectionviewlayoutattributes.md) in order to manage additional layout attributes, you should override this method and return your custom subclass. The methods for creating layout attributes use this class when creating new layout attributes objects.

This method is intended for subclassers only and does not need to be called by your code.

## See Also

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
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md)
  Retrieves the layout attributes for the specified decoration view.
- [func targetContentOffset(forProposedContentOffset: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md)
  Retrieves the content offset to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: CGPoint, withScrollingVelocity: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Retrieves the point at which to stop scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesclass)*