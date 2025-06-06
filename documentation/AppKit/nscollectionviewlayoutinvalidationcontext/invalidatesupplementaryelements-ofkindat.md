# invalidateSupplementaryElements(ofKind:at:)

**Framework**: AppKit  
**Kind**: method

Marks the specified supplementary views as invalid so that their layout information can be updated.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func invalidateSupplementaryElements(ofKind elementKind: NSCollectionView.SupplementaryElementKind, at indexPaths: Set<IndexPath>)
```

#### Discussion

Call this method when you want the layout object to recompute attributes for one or more supplementary views. All of the views must be of the type specified by the `elementKind` parameter. The method adds the views you specify to the [`invalidatedSupplementaryIndexPaths`](nscollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.md) property. You can call this method more than once for the specified `elementKind` value.

## Parameters

- `elementKind`: A string that identifies the type of the supplementary views. This parameter must not be   or an empty string.
- `indexPaths`: A set of   objects. Each index path contains the section in which the supplementary view appears.

## See Also

- [func invalidateItems(at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidateitems(at:).md)
  Marks the specified items as invalid so that their layout information can be updated.
- [func invalidateDecorationElements(ofKind: NSCollectionView.DecorationElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:).md)
  Marks the specified decoration views as invalid so that their layout information can be updated.
- [var invalidatedItemIndexPaths: Set<IndexPath>?](nscollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md)
  The set of items whose layout attributes are invalid.
- [var invalidatedSupplementaryIndexPaths: [NSCollectionView.SupplementaryElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.md)
  A dictionary containing the supplementary views whose layout attributes are invalid.
- [var invalidatedDecorationIndexPaths: [NSCollectionView.DecorationElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary containing the decoration views whose layout attributes are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:))*