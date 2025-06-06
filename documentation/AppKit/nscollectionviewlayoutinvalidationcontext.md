# NSCollectionViewLayoutInvalidationContext

**Framework**: AppKit  
**Kind**: class

An object that identifies the portions of your layout that need to be updated.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewLayoutInvalidationContext
```

#### Overview

Invalidation contexts are a way to improve the efficiency of layout operations and must be supported explicitly by the layout object. Instead of invalidating the entire layout, you can create an invalidation layout object that specifies only the portions of the layout that changed. You then pass that invalidation context to the [`invalidateLayout(with:)`](nscollectionviewlayout/invalidatelayout(with:).md) method of the layout object.

Typically, you ask the layout object to create an invalidation context for you. The [`NSCollectionViewLayout`](nscollectionviewlayout.md) class defines methods for creating a supported invalidation context. If you define a custom layout, you can define additional methods for creating invalidation contexts with custom information. Layout objects may also create invalidation contexts in response to specific changes. For example, layout objects automatically create invalidation contexts when you change the collection view’s data source, when you insert or delete items, and when you reload the collection view’s data.

##### Subclassing Notes

If you define a custom layout object, you can also subclass `NSCollectionViewLayoutInvalidationContext` and add properties that are specific to your layout object. Creating a custom invalidation context is not required and should only be done when your layout object has additional ways to optimize the layout process.

Fore more information about how to support custom invalidation contexts in your layout objects, see [`NSCollectionViewLayout`](nscollectionviewlayout.md).

## Topics

### Invalidating the Collection View Data
- [var invalidateEverything: Bool](nscollectionviewlayoutinvalidationcontext/invalidateeverything.md)
  A Boolean that indicates whether all layout data should be marked as invalid.
- [var invalidateDataSourceCounts: Bool](nscollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts.md)
  A Boolean that indicates whether the layout object should ask for new section and item counts.
### Invalidating the Content Area
- [var contentOffsetAdjustment: NSPoint](nscollectionviewlayoutinvalidationcontext/contentoffsetadjustment.md)
  The delta value to add to the collection view’s content offset.
- [var contentSizeAdjustment: NSSize](nscollectionviewlayoutinvalidationcontext/contentsizeadjustment.md)
  The delta value to add to the collection view’s content size.
### Invalidating Specific Items
- [func invalidateItems(at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidateitems(at:).md)
  Marks the specified items as invalid so that their layout information can be updated.
- [func invalidateSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:).md)
  Marks the specified supplementary views as invalid so that their layout information can be updated.
- [func invalidateDecorationElements(ofKind: NSCollectionView.DecorationElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:).md)
  Marks the specified decoration views as invalid so that their layout information can be updated.
- [var invalidatedItemIndexPaths: Set<IndexPath>?](nscollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md)
  The set of items whose layout attributes are invalid.
- [var invalidatedSupplementaryIndexPaths: [NSCollectionView.SupplementaryElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.md)
  A dictionary containing the supplementary views whose layout attributes are invalid.
- [var invalidatedDecorationIndexPaths: [NSCollectionView.DecorationElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary containing the decoration views whose layout attributes are invalid.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSCollectionViewFlowLayoutInvalidationContext](nscollectionviewflowlayoutinvalidationcontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSCollectionViewUpdateItem](nscollectionviewupdateitem.md)
  A description of a single change to make to an item in a collection view.
- [class NSCollectionViewFlowLayoutInvalidationContext](nscollectionviewflowlayoutinvalidationcontext.md)
  An object that identifies the portions of a flow layout object that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext)*