# shouldInvalidateLayout(forPreferredLayoutAttributes:withOriginalAttributes:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the layout object if changes to a self-sizing cell require a layout update.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func shouldInvalidateLayout(forPreferredLayoutAttributes preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> Bool
```

```objc
- (BOOL) shouldInvalidateLayoutForPreferredLayoutAttributes:(UICollectionViewLayoutAttributes *) preferredAttributes withOriginalAttributes:(UICollectionViewLayoutAttributes *) originalAttributes;
```

#### Return Value

[`true`](../../Swift/true.md) if the layout should be invalidated or [`false`](../../Swift/false.md) if it should not.

#### Discussion

When a collection view includes self-sizing cells, the cells are given the opportunity to modify their own layout attributes before those attributes are applied. A self-sizing cell might do this to specify a different cell size than the one the layout object provides. When the cell provides a different set of attributes, the collection view calls this method to determine if the cell’s change requires a larger layout refresh.

If you are implementing a custom layout, you can override this method and use it to determine if your layout should be invalidated based on the specified attributes. The default implementation of this method returns [`false`](../../Swift/false.md).

## Parameters

- `preferredAttributes`: The layout attributes returned by the cell’s [`preferredLayoutAttributesFitting(_:)`](../uicollectionreusableview/preferredlayoutattributesfitting%28_%29.md) method.
- `originalAttributes`: The attributes that the layout object originally suggested for the cell.

## See Also

### Invalidating the layout
- [func invalidateLayout()](./invalidatelayout%28%29.md)
  Invalidates the current layout and triggers a layout update.
- [func invalidateLayout(with: UICollectionViewLayoutInvalidationContext)](./invalidatelayout%28with%29.md)
  Invalidates the current layout using the information in the provided context object.
- [class var invalidationContextClass: AnyClass](./invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context for the layout.
- [func shouldInvalidateLayout(forBoundsChange: CGRect) -> Bool](./shouldinvalidatelayout%28forboundschange%29.md)
  Asks the layout object if the new bounds require a layout update.
- [func invalidationContext(forBoundsChange: CGRect) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forboundschange%29.md)
  Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [func invalidationContext(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forinteractivelymovingitems,withtargetposition,previousindexpaths,previousposition%29.md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](./invalidationcontextforendinginteractivemovementofitems%28tofinalindexpaths,previousindexpaths,movementcancelled%29.md)
  Retrieves a context object that identifies the items that were moved


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:))*