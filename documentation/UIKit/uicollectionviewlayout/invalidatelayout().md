# invalidateLayout()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the current layout and triggers a layout update.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func invalidateLayout()
```

```objc
- (void) invalidateLayout;
```

## Discussion

You can call this method at any time to update the layout information. This method invalidates the layout of the collection view itself and returns right away. Thus, you can call this method multiple times from the same block of code without triggering multiple layout updates. The actual layout update occurs during the next view layout update cycle.

If you override this method, you must call `super` at some point in your implementation.

## See Also

### Invalidating the layout
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
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](./invalidationcontextforendinginteractivemovementofitems%28tofinalindexpaths,previousindexpaths,movementcancelled%29.md)
  Retrieves a context object that identifies the items that were moved


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidatelayout())*