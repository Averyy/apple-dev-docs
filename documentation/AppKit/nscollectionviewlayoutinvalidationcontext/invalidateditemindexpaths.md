# invalidatedItemIndexPaths

**Framework**: AppKit  
**Kind**: property

The set of items whose layout attributes are invalid.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var invalidatedItemIndexPaths: Set<IndexPath>? { get }
```

#### Discussion

The set contains zero or more [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects, each of which identifies an invalid item.

## See Also

- [func invalidateItems(at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidateitems(at:).md)
  Marks the specified items as invalid so that their layout information can be updated.
- [func invalidateSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:).md)
  Marks the specified supplementary views as invalid so that their layout information can be updated.
- [func invalidateDecorationElements(ofKind: NSCollectionView.DecorationElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:).md)
  Marks the specified decoration views as invalid so that their layout information can be updated.
- [var invalidatedSupplementaryIndexPaths: [NSCollectionView.SupplementaryElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.md)
  A dictionary containing the supplementary views whose layout attributes are invalid.
- [var invalidatedDecorationIndexPaths: [NSCollectionView.DecorationElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary containing the decoration views whose layout attributes are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidateditemindexpaths)*