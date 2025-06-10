# invalidateItems(at:)

**Framework**: UIKit  
**Kind**: method

Adds the cells at the specified index paths to the list of invalid items.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func invalidateItems(at indexPaths: [IndexPath])
```

#### Discussion

Call this method to identify the specific cells of your layout that require updates. The cells you specify are added to the array in the [`invalidatedItemIndexPaths`](uicollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md) property.

## Parameters

- `indexPaths`: An array of   objects. Each index path represents a cell whose layout needs to be recomputed.

## See Also

- [func invalidateSupplementaryElements(ofKind: String, at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:).md)
  Adds the supplementary views at the specified index paths to the list of invalid items.
- [func invalidateDecorationElements(ofKind: String, at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:).md)
  Adds the decoration views at the specified index paths to the list of invalid items.
- [var invalidatedItemIndexPaths: [IndexPath]?](uicollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md)
  An array of index paths representing the cells that were invalidated.
- [var invalidatedSupplementaryIndexPaths: [String : [IndexPath]]?](uicollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.md)
  A dictionary that identifies the supplementary views that were invalidated.
- [var invalidatedDecorationIndexPaths: [String : [IndexPath]]?](uicollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary that identifies the decoration views that were invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateitems(at:))*