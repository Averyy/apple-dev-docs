# shouldInvalidateLayout(forBoundsChange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the layout object if the new bounds require a layout update.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func shouldInvalidateLayout(forBoundsChange newBounds: CGRect) -> Bool
```

```objc
- (BOOL) shouldInvalidateLayoutForBoundsChange:(CGRect) newBounds;
```

#### Return Value

[`true`](../../Swift/true.md) if the collection view requires a layout update or [`false`](../../Swift/false.md) if the layout does not need to change.

#### Discussion

The default implementation of this method returns [`false`](../../Swift/false.md). Subclasses can override it and return an appropriate value based on whether changes in the bounds of the collection view require changes to the layout of cells and supplementary views.

If the bounds of the collection view change and this method returns [`true`](../../Swift/true.md), the collection view invalidates the layout by calling the [`invalidateLayout(with:)`](./invalidatelayout%28with%29.md) method.

## Parameters

- `newBounds`: The new bounds of the collection view.

## See Also

### Invalidating the layout
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates the current layout and triggers a layout update.
- [func invalidateLayout(with: UICollectionViewLayoutInvalidationContext)](./invalidatelayout%28with%29.md)
  Invalidates the current layout using the information in the provided context object.
- [class var invalidationContextClass: AnyClass](./invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context for the layout.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forboundschange:))*