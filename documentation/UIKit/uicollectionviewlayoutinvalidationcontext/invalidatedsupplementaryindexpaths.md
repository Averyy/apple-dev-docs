# invalidatedSupplementaryIndexPaths

**Framework**: UIKit  
**Kind**: property

A dictionary that identifies the supplementary views that were invalidated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var invalidatedSupplementaryIndexPaths: [String : [IndexPath]]? { get }
```

#### Discussion

The keys in this dictionary are the element kind strings of the invalid supplementary views. The value for each key is an array of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects indicating which specific supplementary views have layout changes.

## See Also

- [func invalidateItems(at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidateitems(at:).md)
  Adds the cells at the specified index paths to the list of invalid items.
- [func invalidateSupplementaryElements(ofKind: String, at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:).md)
  Adds the supplementary views at the specified index paths to the list of invalid items.
- [func invalidateDecorationElements(ofKind: String, at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:).md)
  Adds the decoration views at the specified index paths to the list of invalid items.
- [var invalidatedItemIndexPaths: [IndexPath]?](uicollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.md)
  An array of index paths representing the cells that were invalidated.
- [var invalidatedDecorationIndexPaths: [String : [IndexPath]]?](uicollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary that identifies the decoration views that were invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths)*