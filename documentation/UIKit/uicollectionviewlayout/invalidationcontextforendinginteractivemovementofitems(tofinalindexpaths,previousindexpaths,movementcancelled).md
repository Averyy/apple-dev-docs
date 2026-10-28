# invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths:previousIndexPaths:movementCancelled:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves a context object that identifies the items that were moved

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths indexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext
```

```objc
- (UICollectionViewLayoutInvalidationContext *) invalidationContextForEndingInteractiveMovementOfItemsToFinalIndexPaths:(NSArray<NSIndexPath *> *) indexPaths previousIndexPaths:(NSArray<NSIndexPath *> *) previousIndexPaths movementCancelled:(BOOL) movementCancelled;
```

## Return Value

An invalidation context that includes information about what changes need to be made to the layout.

## Discussion

The layout object uses this method to retrieve invalidation contexts when an interactive move of one or more items ends, either because the move was successful or because it was cancelled by the user. The default implementation creates an instance of the class provided by the [`invalidationContextClass`](./invalidationcontextclass.md) class method, fills it with the provided information, and returns it. If you want to use a custom invalidation context object with your layout, always override that method and return your custom class.

Subclasses can override this method and use it to perform additional configuration of the invalidation context before returning it. In your custom implementation, call `super` so that the parent class can perform the basic configuration of the object.

## Parameters

- `indexPaths`: The final locations of the items. For cancelled interactions, these index paths correspond to the original index paths of the items.
- `previousIndexPaths`: The previous locations of the items. This parameter contains the last set of index paths reported by the collection view during the movement sequence.
- `movementCancelled`: A Boolean value indicating whether the interactive movement ended successfully or was cancelled.

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
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> Bool](./shouldinvalidatelayout%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Asks the layout object if changes to a self-sizing cell require a layout update.
- [func invalidationContext(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forinteractivelymovingitems,withtargetposition,previousindexpaths,previousposition%29.md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths:previousindexpaths:movementcancelled:))*