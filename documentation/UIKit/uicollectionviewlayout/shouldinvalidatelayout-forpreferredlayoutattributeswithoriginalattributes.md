# shouldInvalidateLayout(forPreferredLayoutAttributes:withOriginalAttributes:)

**Framework**: UIKit  
**Kind**: method

Asks the layout object if changes to a self-sizing cell require a layout update.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func shouldInvalidateLayout(forPreferredLayoutAttributes preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the layout should be invalidated or [`false`](https://developer.apple.com/documentation/Swift/false) if it should not.

#### Discussion

When a collection view includes self-sizing cells, the cells are given the opportunity to modify their own layout attributes before those attributes are applied. A self-sizing cell might do this to specify a different cell size than the one the layout object provides. When the cell provides a different set of attributes, the collection view calls this method to determine if the cell’s change requires a larger layout refresh.

If you are implementing a custom layout, you can override this method and use it to determine if your layout should be invalidated based on the specified attributes. The default implementation of this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `preferredAttributes`: The layout attributes returned by the cell’s   method.
- `originalAttributes`: The attributes that the layout object originally suggested for the cell.

## See Also

- [func invalidateLayout()](uicollectionviewlayout/invalidatelayout.md)
  Invalidates the current layout and triggers a layout update.
- [func invalidateLayout(with: UICollectionViewLayoutInvalidationContext)](uicollectionviewlayout/invalidatelayout(with:).md)
  Invalidates the current layout using the information in the provided context object.
- [class var invalidationContextClass: AnyClass](uicollectionviewlayout/invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context for the layout.
- [func shouldInvalidateLayout(forBoundsChange: CGRect) -> Bool](uicollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Asks the layout object if the new bounds require a layout update.
- [func invalidationContext(forBoundsChange: CGRect) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forboundschange:).md)
  Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [func invalidationContext(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forinteractivelymovingitems:withtargetposition:previousindexpaths:previousposition:).md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths:previousindexpaths:movementcancelled:).md)
  Retrieves a context object that identifies the items that were moved


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:))*