# itemSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The default size to use for items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var itemSize: NSSize { get set }
```

```objc
@property NSSize itemSize;
```

#### Discussion

This property contains the default size of items. If you do not provide an estimated size or implement the [`collectionView(_:layout:sizeForItemAt:)`](../nscollectionviewdelegateflowlayout/collectionview%28_,layout,sizeforitemat%29.md) method in your delegate, the flow layout uses this value for the size of each item. All items are set to the same size. This value applies only to items and not to supplementary views.

The default value of this property is (`50.0`, `50.0`). For more information about how item sizes are determined, see [Understanding How the Flow Layout is Generated](../nscollectionviewflowlayout.md#Understanding-How-the-Flow-Layout-is-Generated).

## See Also

### Configuring the Item Spacing
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var estimatedItemSize: NSSize](./estimateditemsize.md)
  The estimated size of items in the collection view.
- [var sectionInset: NSEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/itemsize)*