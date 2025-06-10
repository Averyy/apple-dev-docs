# invalidationContextClass

**Framework**: UIKit  
**Kind**: property

Returns the class to use when creating an invalidation context for the layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var invalidationContextClass: AnyClass { get }
```

#### Discussion

If you subclass `UICollectionViewLayout` and use a custom invalidation context object to improve the performance of your layout updates, override this method and return your [`UICollectionViewLayoutInvalidationContext`](uicollectionviewlayoutinvalidationcontext.md) subclass. When the collection view needs to invalidate your layout, it uses the class you provide to create an appropriate invalidation context object.

## See Also

- [func invalidateLayout()](uicollectionviewlayout/invalidatelayout.md)
  Invalidates the current layout and triggers a layout update.
- [func invalidateLayout(with: UICollectionViewLayoutInvalidationContext)](uicollectionviewlayout/invalidatelayout(with:).md)
  Invalidates the current layout using the information in the provided context object.
- [func shouldInvalidateLayout(forBoundsChange: CGRect) -> Bool](uicollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Asks the layout object if the new bounds require a layout update.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidationcontextclass)*