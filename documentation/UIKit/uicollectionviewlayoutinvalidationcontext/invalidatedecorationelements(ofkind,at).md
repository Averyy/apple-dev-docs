# invalidateDecorationElements(ofKind:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the decoration views at the specified index paths to the list of invalid items.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func invalidateDecorationElements(ofKind elementKind: String, at indexPaths: [IndexPath])
```

```objc
- (void) invalidateDecorationElementsOfKind:(NSString *) elementKind atIndexPaths:(NSArray<NSIndexPath *> *) indexPaths;
```

#### Discussion

Call this method to identify the specific decoration views whose layout attributes changed. The views you specify are added to the dictionary in the [`invalidatedDecorationIndexPaths`](./invalidateddecorationindexpaths.md) property. All of the views you specify should be of the type that you specified in the `elementKind` parameter. If you call this method two or more times with the same value for the `elementKind` parameter, this method merges the new index paths with the ones previously specified.

## Parameters

- `elementKind`: A string that identifies the type of the decoration views. This parameter must not be `nil`.
- `indexPaths`: An array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects. Each index path represents a supplementary view of the given kind whose layout needs to be recomputed.

## See Also

### Invalidating Specific Items
- [func invalidateItems(at: [IndexPath])](./invalidateitems%28at%29.md)
  Adds the cells at the specified index paths to the list of invalid items.
- [func invalidateSupplementaryElements(ofKind: String, at: [IndexPath])](./invalidatesupplementaryelements%28ofkind,at%29.md)
  Adds the supplementary views at the specified index paths to the list of invalid items.
- [var invalidatedItemIndexPaths: [IndexPath]?](./invalidateditemindexpaths.md)
  An array of index paths representing the cells that were invalidated.
- [var invalidatedSupplementaryIndexPaths: [String : [IndexPath]]?](./invalidatedsupplementaryindexpaths.md)
  A dictionary that identifies the supplementary views that were invalidated.
- [var invalidatedDecorationIndexPaths: [String : [IndexPath]]?](./invalidateddecorationindexpaths.md)
  A dictionary that identifies the decoration views that were invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:))*