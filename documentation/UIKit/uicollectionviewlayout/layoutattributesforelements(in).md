# layoutAttributesForElements(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the layout attributes for all of the cells and views in the specified rectangle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func layoutAttributesForElements(in rect: CGRect) -> [UICollectionViewLayoutAttributes]?
```

```objc
- (NSArray<__kindof UICollectionViewLayoutAttributes *> *) layoutAttributesForElementsInRect:(CGRect) rect;
```

## Return Value

An array of [`UICollectionViewLayoutAttributes`](../uicollectionviewlayoutattributes.md) objects representing the layout information for the cells and views. The default implementation returns `nil`.

## Discussion

Subclasses must override this method and use it to return layout information for all items whose view intersects the specified rectangle. Your implementation should return attributes for all visual elements, including cells, supplementary views, and decoration views.

When creating the layout attributes, always create an attributes object that represents the correct element type (cell, supplementary, or decoration). The collection view differentiates between attributes for each type and uses that information to make decisions about which views to create and how to manage them.

## Parameters

- `rect`: The rectangle (specified in the collection view’s coordinate system) containing the target views.

## See Also

### Providing layout attributes
- [class var layoutAttributesClass: AnyClass](./layoutattributesclass.md)
  The class to use when creating layout attributes objects.
- [func prepare()](./prepare%28%29.md)
  Tells the layout object to update the current layout.
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
- [func targetContentOffset(forProposedContentOffset: CGPoint, withScrollingVelocity: CGPoint) -> CGPoint](./targetcontentoffset%28forproposedcontentoffset,withscrollingvelocity%29.md)
  Retrieves the point at which to stop scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesforelements(in:))*