# invalidateItems(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks the specified items as invalid so that their layout information can be updated.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func invalidateItems(at indexPaths: Set<IndexPath>)
```

```objc
- (void) invalidateItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths;
```

## Discussion

Call this method when you want the layout object to recompute attributes for a specific set of items. The items you provide are added to the [`invalidatedItemIndexPaths`](./invalidateditemindexpaths.md) property. You can call this method more than once to create a merged set of items.

## Parameters

- `indexPaths`: A set of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects. Each index path represents an item whose layout needs to be recomputed.

## See Also

### Invalidating Specific Items
- [func invalidateSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind, at: Set<IndexPath>)](./invalidatesupplementaryelements%28ofkind,at%29.md)
  Marks the specified supplementary views as invalid so that their layout information can be updated.
- [func invalidateDecorationElements(ofKind: NSCollectionView.DecorationElementKind, at: Set<IndexPath>)](./invalidatedecorationelements%28ofkind,at%29.md)
  Marks the specified decoration views as invalid so that their layout information can be updated.
- [var invalidatedItemIndexPaths: Set<IndexPath>?](./invalidateditemindexpaths.md)
  The set of items whose layout attributes are invalid.
- [var invalidatedSupplementaryIndexPaths: [NSCollectionView.SupplementaryElementKind : Set<IndexPath>]?](./invalidatedsupplementaryindexpaths.md)
  A dictionary containing the supplementary views whose layout attributes are invalid.
- [var invalidatedDecorationIndexPaths: [NSCollectionView.DecorationElementKind : Set<IndexPath>]?](./invalidateddecorationindexpaths.md)
  A dictionary containing the decoration views whose layout attributes are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidateitems(at:))*