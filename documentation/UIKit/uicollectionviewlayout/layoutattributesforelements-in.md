# layoutAttributesForElements(in:)

**Framework**: UIKit  
**Kind**: method

Retrieves the layout attributes for all of the cells and views in the specified rectangle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func layoutAttributesForElements(in rect: CGRect) -> [UICollectionViewLayoutAttributes]?
```

#### Return Value

An array of [`UICollectionViewLayoutAttributes`](uicollectionviewlayoutattributes.md) objects representing the layout information for the cells and views. The default implementation returns `nil`.

#### Discussion

Subclasses must override this method and use it to return layout information for all items whose view intersects the specified rectangle. Your implementation should return attributes for all visual elements, including cells, supplementary views, and decoration views.

When creating the layout attributes, always create an attributes object that represents the correct element type (cell, supplementary, or decoration). The collection view differentiates between attributes for each type and uses that information to make decisions about which views to create and how to manage them.

## Parameters

- `rect`: The rectangle (specified in the collection view’s coordinate system) containing the target views.

## See Also

- [class var layoutAttributesClass: AnyClass](uicollectionviewlayout/layoutattributesclass.md)
  The class to use when creating layout attributes objects.
- [func prepare()](uicollectionviewlayout/prepare.md)
  Tells the layout object to update the current layout.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesforelements(in:))*