# invalidateItems(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the cells at the specified index paths to the list of invalid items.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func invalidateItems(at indexPaths: [IndexPath])
```

```objc
- (void) invalidateItemsAtIndexPaths:(NSArray<NSIndexPath *> *) indexPaths;
```

#### Discussion

Call this method to identify the specific cells of your layout that require updates. The cells you specify are added to the array in the [`invalidatedItemIndexPaths`](./invalidateditemindexpaths.md) property.

## Parameters

- `indexPaths`: An array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects. Each index path represents a cell whose layout needs to be recomputed.

## See Also

### Invalidating Specific Items
- [func invalidateSupplementaryElements(ofKind: String, at: [IndexPath])](./invalidatesupplementaryelements%28ofkind,at%29.md)
  Adds the supplementary views at the specified index paths to the list of invalid items.
- [func invalidateDecorationElements(ofKind: String, at: [IndexPath])](./invalidatedecorationelements%28ofkind,at%29.md)
  Adds the decoration views at the specified index paths to the list of invalid items.
- [var invalidatedItemIndexPaths: [IndexPath]?](./invalidateditemindexpaths.md)
  An array of index paths representing the cells that were invalidated.
- [var invalidatedSupplementaryIndexPaths: [String : [IndexPath]]?](./invalidatedsupplementaryindexpaths.md)
  A dictionary that identifies the supplementary views that were invalidated.
- [var invalidatedDecorationIndexPaths: [String : [IndexPath]]?](./invalidateddecorationindexpaths.md)
  A dictionary that identifies the decoration views that were invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateitems(at:))*