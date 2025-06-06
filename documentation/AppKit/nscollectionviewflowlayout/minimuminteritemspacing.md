# minimumInteritemSpacing

**Framework**: AppKit  
**Kind**: property

The minimum spacing (in points) to use between items in the same row or column.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var minimumInteritemSpacing: CGFloat { get set }
```

#### Discussion

If the delegate does not implement the [`collectionView(_:layout:minimumInteritemSpacingForSectionAt:)`](nscollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:).md) method, the flow layout object uses the value of this property to set the spacing between items in the same line.

For a vertically scrolling layout, the value represents the minimum spacing between items in the same row. For a horizontally scrolling layout, the value represents the minimum spacing between items in the same column. The layout object uses this spacing only to compute how many items can fit in a single row or column. The actual spacing may be increased after the number of items has been determined, as illustrated in [`Figure 1`](nscollectionviewflowlayout/1402872-minimuminteritemspacing#1965632.md).

![None](https://docs-assets.developer.apple.com/published/0258a78b9ea6a2d437055740ba073c0d/media-1965632%402x.png)

The default value of this property is `10.0`.

## See Also

- [var minimumLineSpacing: CGFloat](nscollectionviewflowlayout/minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var estimatedItemSize: NSSize](nscollectionviewflowlayout/estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](nscollectionviewflowlayout/itemsize.md)
  The default size to use for items.
- [var sectionInset: NSEdgeInsets](nscollectionviewflowlayout/sectioninset.md)
  The margins used to lay out content in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/minimuminteritemspacing)*