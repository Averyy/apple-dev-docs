# NSCollectionViewFlowLayoutInvalidationContext

**Framework**: AppKit  
**Kind**: class

An object that identifies the portions of a flow layout object that need to be updated.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewFlowLayoutInvalidationContext
```

#### Overview

Layout objects use invalidation contexts to optimize the layout process and avoid unnecessary work. You use this class to specify whether the [`NSCollectionViewFlowLayout`](nscollectionviewflowlayout.md) object should fetch new size information from its delegate. You can also prevent the flow layout object from updating its layout information altogether.

When you want to invalidate your flow layout object, call the [`invalidationContextClass`](nscollectionviewlayout/invalidationcontextclass.md) method of your layout object and instantiate the resulting class. (The implementation of that method in [`NSCollectionViewFlowLayout`](nscollectionviewflowlayout.md) returns this class.) After instantiating this class, set the properties to appropriate values and pass the object to the [`invalidateLayout(with:)`](nscollectionviewlayout/invalidatelayout(with:).md) method of the layout object.

## Topics

### Invalidating the Flow Layout
- [var invalidateFlowLayoutAttributes: Bool](nscollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes.md)
  A Boolean value indicating whether the flow layout object should invalidate its current attributes.
- [var invalidateFlowLayoutDelegateMetrics: Bool](nscollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics.md)
  A Boolean value indicating whether the flow layout object should fetch new size information from its delegate.

## Relationships

### Inherits From
- [NSCollectionViewLayoutInvalidationContext](nscollectionviewlayoutinvalidationcontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCollectionViewUpdateItem](nscollectionviewupdateitem.md)
  A description of a single change to make to an item in a collection view.
- [class NSCollectionViewLayoutInvalidationContext](nscollectionviewlayoutinvalidationcontext.md)
  An object that identifies the portions of your layout that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayoutinvalidationcontext)*