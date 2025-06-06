# estimatedItemSize

**Framework**: AppKit  
**Kind**: property

The estimated size of items in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var estimatedItemSize: NSSize { get set }
```

#### Discussion

Providing an estimated item size lets the collection view defer some of the calculations needed to determine the size of its content, which can improve performance. Instead of explicitly computing the size of each item, the flow layout assumes that offscreen items have the estimated size. The estimated size is used only until an actual value is calculated. The default value of this property is [`NSZeroSize`](https://developer.apple.com/documentation/Foundation/NSZeroSize).

If the value of this property is not [`NSZeroSize`](https://developer.apple.com/documentation/Foundation/NSZeroSize), the flow layout uses the estimated size you specified. If all of your items actually have the same size, use the [`itemSize`](nscollectionviewflowlayout/itemsize.md) property to set their size and set this property to [`NSZeroSize`](https://developer.apple.com/documentation/Foundation/NSZeroSize). For more information about how item sizes are determined, see [`Understanding How the Flow Layout is Generated`](nscollectionviewflowlayout#Understanding-How-the-Flow-Layout-is-Generated.md).

## See Also

- [var minimumLineSpacing: CGFloat](nscollectionviewflowlayout/minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var minimumInteritemSpacing: CGFloat](nscollectionviewflowlayout/minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var itemSize: NSSize](nscollectionviewflowlayout/itemsize.md)
  The default size to use for items.
- [var sectionInset: NSEdgeInsets](nscollectionviewflowlayout/sectioninset.md)
  The margins used to lay out content in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/estimateditemsize)*