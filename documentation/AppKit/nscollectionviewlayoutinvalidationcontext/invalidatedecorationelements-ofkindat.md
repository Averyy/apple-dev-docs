# invalidateDecorationElements(ofKind:at:)

**Framework**: AppKit  
**Kind**: method

Marks the specified decoration views as invalid so that their layout information can be updated.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func invalidateDecorationElements(ofKind elementKind: NSCollectionView.DecorationElementKind, at indexPaths: Set<IndexPath>)
```

#### Discussion

Call this method when you want the layout object to recompute attributes for one or more decoration views. All of the views must be of the type specified by the `elementKind` parameter. The method adds the views you specify to the [`invalidatedDecorationIndexPaths`](nscollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md) property. You can call this method more than once for the specified `elementKind` value.

## Parameters

- `elementKind`: A string that identifies the type of the decoration views. This parameter must not be   or an empty string.
- `indexPaths`: A set of   objects. Each index path contains the section in which the decoration view appears.

## See Also

- [func invalidateItems(at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidateitems(at:).md)
  Marks the specified items as invalid so that their layout information can be updated.
- [func invalidateSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:).md)
  Marks the specified supplementary views as invalid so that their layout information can be updated.
- [var invalidatedItemIndexPaths: Set<IndexPath>?](nscollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md)
  The set of items whose layout attributes are invalid.
- [var invalidatedSupplementaryIndexPaths: [NSCollectionView.SupplementaryElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.md)
  A dictionary containing the supplementary views whose layout attributes are invalid.
- [var invalidatedDecorationIndexPaths: [NSCollectionView.DecorationElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary containing the decoration views whose layout attributes are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:))*