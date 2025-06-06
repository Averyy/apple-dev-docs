# invalidatedSupplementaryIndexPaths

**Framework**: AppKit  
**Kind**: property

A dictionary containing the supplementary views whose layout attributes are invalid.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var invalidatedSupplementaryIndexPaths: [NSCollectionView.SupplementaryElementKind : Set<IndexPath>]? { get }
```

#### Discussion

The keys in this dictionary are the element kind strings of the supplementary views. The value for each key is an [`NSSet`](https://developer.apple.com/documentation/Foundation/NSSet) object containing one or more [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects, each of which identifies the section containing the supplementary view.

## See Also

- [func invalidateItems(at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidateitems(at:).md)
  Marks the specified items as invalid so that their layout information can be updated.
- [func invalidateSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:).md)
  Marks the specified supplementary views as invalid so that their layout information can be updated.
- [func invalidateDecorationElements(ofKind: NSCollectionView.DecorationElementKind, at: Set<IndexPath>)](nscollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:).md)
  Marks the specified decoration views as invalid so that their layout information can be updated.
- [var invalidatedItemIndexPaths: Set<IndexPath>?](nscollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md)
  The set of items whose layout attributes are invalid.
- [var invalidatedDecorationIndexPaths: [NSCollectionView.DecorationElementKind : Set<IndexPath>]?](nscollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary containing the decoration views whose layout attributes are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths)*