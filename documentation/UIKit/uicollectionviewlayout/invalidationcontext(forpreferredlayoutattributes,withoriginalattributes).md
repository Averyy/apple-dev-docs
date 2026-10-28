# invalidationContext(forPreferredLayoutAttributes:withOriginalAttributes:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func invalidationContext(forPreferredLayoutAttributes preferredAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes originalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext
```

```objc
- (UICollectionViewLayoutInvalidationContext *) invalidationContextForPreferredLayoutAttributes:(UICollectionViewLayoutAttributes *) preferredAttributes withOriginalAttributes:(UICollectionViewLayoutAttributes *) originalAttributes;
```

## Return Value

An invalidation context that includes information about what changes need to be made to the layout.

## Discussion

The default implementation of this method creates an instance of the class provided by the [`invalidationContextClass`](./invalidationcontextclass.md) class method and returns it. If you want to use a custom invalidation context object with your layout, always override that method and return your custom class.

Subclasses can override this method and use it to perform additional configuration of the invalidation context before returning it. In your custom implementation, call `super` so that the parent class can perform the basic configuration of the object.

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
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> Bool](./shouldinvalidatelayout%28forpreferredlayoutattributes,withoriginalattributes%29.md)
  Asks the layout object if changes to a self-sizing cell require a layout update.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](./invalidationcontext%28forinteractivelymovingitems,withtargetposition,previousindexpaths,previousposition%29.md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](./invalidationcontextforendinginteractivemovementofitems%28tofinalindexpaths,previousindexpaths,movementcancelled%29.md)
  Retrieves a context object that identifies the items that were moved


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:))*