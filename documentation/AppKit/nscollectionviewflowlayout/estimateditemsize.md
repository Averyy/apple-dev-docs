# estimatedItemSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The estimated size of items in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var estimatedItemSize: NSSize { get set }
```

```objc
@property NSSize estimatedItemSize;
```

#### Discussion

Providing an estimated item size lets the collection view defer some of the calculations needed to determine the size of its content, which can improve performance. Instead of explicitly computing the size of each item, the flow layout assumes that offscreen items have the estimated size. The estimated size is used only until an actual value is calculated. The default value of this property is [`NSZeroSize`](../../Foundation/nszerosize.md).

If the value of this property is not [`NSZeroSize`](../../Foundation/nszerosize.md), the flow layout uses the estimated size you specified. If all of your items actually have the same size, use the [`itemSize`](./itemsize.md) property to set their size and set this property to [`NSZeroSize`](../../Foundation/nszerosize.md). For more information about how item sizes are determined, see [Understanding How the Flow Layout is Generated](../nscollectionviewflowlayout.md#Understanding-How-the-Flow-Layout-is-Generated).

## See Also

### Configuring the Item Spacing
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var itemSize: NSSize](./itemsize.md)
  The default size to use for items.
- [var sectionInset: NSEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/estimateditemsize)*