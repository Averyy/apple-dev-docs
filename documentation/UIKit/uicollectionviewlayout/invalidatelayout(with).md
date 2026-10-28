# invalidateLayout(with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the current layout using the information in the provided context object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func invalidateLayout(with context: UICollectionViewLayoutInvalidationContext)
```

```objc
- (void) invalidateLayoutWithContext:(UICollectionViewLayoutInvalidationContext *) context;
```

## Discussion

The default implementation of this method optimizes the layout process using the base properties of the [`UICollectionViewLayoutInvalidationContext`](../uicollectionviewlayoutinvalidationcontext.md) class. If you define a custom context object for your layout, override this method and apply any custom properties of the context object to your layout computations.

If you override this method, you must call `super` at some point in your implementation.

## Parameters

- `context`: The context object indicating which parts of the layout to refresh.

## See Also

### Invalidating the layout
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates the current layout and triggers a layout update.
- [class var invalidationContextClass: AnyClass](./invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context for the layout.
- [func shouldInvalidateLayout(forBoundsChange: CGRect) -> Bool](./shouldinvalidatelayout%28forboundschange%29.md)
  Asks the layout object if the new bounds require a layout update.
- [func invalidationContext(forBoundsChange: CGRect) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forboundschange%29.md)
  Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> Bool](./shouldinvalidatelayout%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Asks the layout object if changes to a self-sizing cell require a layout update.
- [func invalidationContext(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forinteractivelymovingitems,withtargetposition,previousindexpaths,previousposition%29.md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](./invalidationcontextforendinginteractivemovementofitems%28tofinalindexpaths,previousindexpaths,movementcancelled%29.md)
  Retrieves a context object that identifies the items that were moved


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidatelayout(with:))*