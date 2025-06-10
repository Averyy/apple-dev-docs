# invalidatedItemIndexPaths

**Framework**: UIKit  
**Kind**: property

An array of index paths representing the cells that were invalidated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var invalidatedItemIndexPaths: [IndexPath]? { get }
```

#### Discussion

The array contains zero or more [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects, each of which represents a cell whose layout changed.

## See Also

- [func invalidateItems(at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidateitems(at:).md)
  Adds the cells at the specified index paths to the list of invalid items.
- [func invalidateSupplementaryElements(ofKind: String, at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:).md)
  Adds the supplementary views at the specified index paths to the list of invalid items.
- [func invalidateDecorationElements(ofKind: String, at: [IndexPath])](uicollectionviewlayoutinvalidationcontext/invalidatedecorationelements(ofkind:at:).md)
  Adds the decoration views at the specified index paths to the list of invalid items.
- [var invalidatedSupplementaryIndexPaths: [String : [IndexPath]]?](uicollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.md)
  A dictionary that identifies the supplementary views that were invalidated.
- [var invalidatedDecorationIndexPaths: [String : [IndexPath]]?](uicollectionviewlayoutinvalidationcontext/invalidateddecorationindexpaths.md)
  A dictionary that identifies the decoration views that were invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateditemindexpaths)*