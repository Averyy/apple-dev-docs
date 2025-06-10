# UICollectionViewFlowLayoutInvalidationContext

**Framework**: UIKit  
**Kind**: class

A set of properties for determining whether to recompute the size of items or their position in the layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewFlowLayoutInvalidationContext
```

#### Overview

The flow layout object creates instances of this class when it needs to invalidate its contents in response to changes. You can also create instances when invalidating the flow layout manually.

## Topics

### Specifying what to invalidate
- [var invalidateFlowLayoutDelegateMetrics: Bool](uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics.md)
  A Boolean indicating whether to recompute the size of items and views in the layout.
- [var invalidateFlowLayoutAttributes: Bool](uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes.md)
  A Boolean indicating whether to recompute the layout attributes for items and views in the layout.

## Relationships

### Inherits From
- [UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Customizing collection view layouts](customizing-collection-view-layouts.md)
  Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [class UICollectionViewLayout](uicollectionviewlayout.md)
  An abstract base class for generating layout information for a collection view.
- [class UICollectionViewFlowLayout](uicollectionviewflowlayout.md)
  A layout object that organizes items into a grid with optional header and footer views for each section.
- [class UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md)
  A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.
- [class UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md)
  A layout object that manages the layout-related attributes for a given item in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext)*