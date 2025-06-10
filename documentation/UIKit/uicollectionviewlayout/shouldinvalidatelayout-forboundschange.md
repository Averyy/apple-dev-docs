# shouldInvalidateLayout(forBoundsChange:)

**Framework**: UIKit  
**Kind**: method

Asks the layout object if the new bounds require a layout update.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func shouldInvalidateLayout(forBoundsChange newBounds: CGRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the collection view requires a layout update or [`false`](https://developer.apple.com/documentation/swift/false) if the layout does not need to change.

#### Discussion

The default implementation of this method returns [`false`](https://developer.apple.com/documentation/swift/false). Subclasses can override it and return an appropriate value based on whether changes in the bounds of the collection view require changes to the layout of cells and supplementary views.

If the bounds of the collection view change and this method returns [`true`](https://developer.apple.com/documentation/swift/true), the collection view invalidates the layout by calling the [`invalidateLayout(with:)`](uicollectionviewlayout/invalidatelayout(with:).md) method.

## Parameters

- `newBounds`: The new bounds of the collection view.

## See Also

- [func invalidateLayout()](uicollectionviewlayout/invalidatelayout.md)
  Invalidates the current layout and triggers a layout update.
- [func invalidateLayout(with: UICollectionViewLayoutInvalidationContext)](uicollectionviewlayout/invalidatelayout(with:).md)
  Invalidates the current layout using the information in the provided context object.
- [class var invalidationContextClass: AnyClass](uicollectionviewlayout/invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context for the layout.
- [func invalidationContext(forBoundsChange: CGRect) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forboundschange:).md)
  Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> Bool](uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:).md)
  Asks the layout object if changes to a self-sizing cell require a layout update.
- [func invalidationContext(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forinteractivelymovingitems:withtargetposition:previousindexpaths:previousposition:).md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths:previousindexpaths:movementcancelled:).md)
  Retrieves a context object that identifies the items that were moved


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forboundschange:))*