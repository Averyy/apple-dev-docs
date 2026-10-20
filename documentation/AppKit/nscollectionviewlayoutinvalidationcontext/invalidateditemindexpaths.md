# invalidatedItemIndexPaths

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The set of items whose layout attributes are invalid.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var invalidatedItemIndexPaths: Set<IndexPath>? { get }
```

```objc
@property (readonly, nullable) NSSet<NSIndexPath *> * invalidatedItemIndexPaths;
```

#### Discussion

The set contains zero or more [`NSIndexPath`](../../Foundation/nsindexpath.md) objects, each of which identifies an invalid item.

## See Also

### Invalidating Specific Items
- [func invalidateItems(at: Set<IndexPath>)](./invalidateitems%28at%29.md)
  Marks the specified items as invalid so that their layout information can be updated.
- [func invalidateSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind, at: Set<IndexPath>)](./invalidatesupplementaryelements%28ofkind,at%29.md)
  Marks the specified supplementary views as invalid so that their layout information can be updated.
- [func invalidateDecorationElements(ofKind: NSCollectionView.DecorationElementKind, at: Set<IndexPath>)](./invalidatedecorationelements%28ofkind,at%29.md)
  Marks the specified decoration views as invalid so that their layout information can be updated.
- [var invalidatedSupplementaryIndexPaths: [NSCollectionView.SupplementaryElementKind : Set<IndexPath>]?](./invalidatedsupplementaryindexpaths.md)
  A dictionary containing the supplementary views whose layout attributes are invalid.
- [var invalidatedDecorationIndexPaths: [NSCollectionView.DecorationElementKind : Set<IndexPath>]?](./invalidateddecorationindexpaths.md)
  A dictionary containing the decoration views whose layout attributes are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidateditemindexpaths)*