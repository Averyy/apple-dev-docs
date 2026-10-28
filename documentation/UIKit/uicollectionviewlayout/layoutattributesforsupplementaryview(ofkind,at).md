# layoutAttributesForSupplementaryView(ofKind:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the layout attributes for the specified supplementary view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func layoutAttributesForSupplementaryView(ofKind elementKind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

```objc
- (UICollectionViewLayoutAttributes *) layoutAttributesForSupplementaryViewOfKind:(NSString *) elementKind atIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

A layout attributes object containing the information to apply to the supplementary view.

## Discussion

If your layout object defines any supplementary views, you must override this method and use it to return layout information for those views.

## Parameters

- `elementKind`: A string that identifies the type of the supplementary view.
- `indexPath`: The index path of the view.

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
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](./layoutattributesfordecorationview%28ofkind,at%29.md)
  Retrieves the layout attributes for the specified decoration view.
- [func targetContentOffset(forProposedContentOffset: CGPoint) -> CGPoint](./targetcontentoffset%28forproposedcontentoffset%29.md)
  Retrieves the content offset to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: CGPoint, withScrollingVelocity: CGPoint) -> CGPoint](./targetcontentoffset%28forproposedcontentoffset,withscrollingvelocity%29.md)
  Retrieves the point at which to stop scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:))*