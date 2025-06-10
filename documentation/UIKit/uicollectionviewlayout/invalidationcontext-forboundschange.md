# invalidationContext(forBoundsChange:)

**Framework**: UIKit  
**Kind**: method

Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func invalidationContext(forBoundsChange newBounds: CGRect) -> UICollectionViewLayoutInvalidationContext
```

#### Return Value

An invalidation context that describes the changes that need to be made. Do not return nil.

#### Discussion

The default implementation of this method creates an instance of the class provided by the [`invalidationContextClass`](uicollectionviewlayout/invalidationcontextclass.md) class method and returns it. If you want to use a custom invalidation context object with your layout, always override that method and return your custom class.

You can override this method if you want to create and configure your custom invalidation context in response to a bounds change. If you override this method, you must call `super` first to get the invalidation context object to return. After getting this object, set any custom properties and return it.

## Parameters

- `newBounds`: The new bounds for the collection view.

## See Also

- [func invalidateLayout()](uicollectionviewlayout/invalidatelayout.md)
  Invalidates the current layout and triggers a layout update.
- [func invalidateLayout(with: UICollectionViewLayoutInvalidationContext)](uicollectionviewlayout/invalidatelayout(with:).md)
  Invalidates the current layout using the information in the provided context object.
- [class var invalidationContextClass: AnyClass](uicollectionviewlayout/invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context for the layout.
- [func shouldInvalidateLayout(forBoundsChange: CGRect) -> Bool](uicollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Asks the layout object if the new bounds require a layout update.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> Bool](uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:).md)
  Asks the layout object if changes to a self-sizing cell require a layout update.
- [func invalidationContext(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forinteractivelymovingitems:withtargetposition:previousindexpaths:previousposition:).md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths:previousindexpaths:movementcancelled:).md)
  Retrieves a context object that identifies the items that were moved


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidationcontext(forboundschange:))*