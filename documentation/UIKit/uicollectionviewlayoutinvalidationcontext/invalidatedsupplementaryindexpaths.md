# invalidatedSupplementaryIndexPaths

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A dictionary that identifies the supplementary views that were invalidated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var invalidatedSupplementaryIndexPaths: [String : [IndexPath]]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,NSArray<NSIndexPath *> *> * invalidatedSupplementaryIndexPaths;
```

## Discussion

The keys in this dictionary are the element kind strings of the invalid supplementary views. The value for each key is an array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects indicating which specific supplementary views have layout changes.

## See Also

### Invalidating Specific Items
- [func invalidateItems(at: [IndexPath])](./invalidateitems%28at%29.md)
  Adds the cells at the specified index paths to the list of invalid items.
- [func invalidateSupplementaryElements(ofKind: String, at: [IndexPath])](./invalidatesupplementaryelements%28ofkind,at%29.md)
  Adds the supplementary views at the specified index paths to the list of invalid items.
- [func invalidateDecorationElements(ofKind: String, at: [IndexPath])](./invalidatedecorationelements%28ofkind,at%29.md)
  Adds the decoration views at the specified index paths to the list of invalid items.
- [var invalidatedItemIndexPaths: [IndexPath]?](./invalidateditemindexpaths.md)
  An array of index paths representing the cells that were invalidated.
- [var invalidatedDecorationIndexPaths: [String : [IndexPath]]?](./invalidateddecorationindexpaths.md)
  A dictionary that identifies the decoration views that were invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths)*