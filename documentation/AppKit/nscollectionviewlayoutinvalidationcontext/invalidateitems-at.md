# invalidateItems(at:)

**Framework**: AppKit  
**Kind**: method

Marks the specified items as invalid so that their layout information can be updated.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func invalidateItems(at indexPaths: Set<IndexPath>)
```

#### Discussion

Call this method when you want the layout object to recompute attributes for a specific set of items. The items you provide are added to the [`invalidatedItemIndexPaths`](nscollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md) property. You can call this method more than once to create a merged set of items.

## Parameters

- `indexPaths`: A set of   objects. Each index path represents an item whose layout needs to be recomputed.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidateitems(at:))*