# minimumLineSpacing

**Framework**: AppKit  
**Kind**: property

The minimum spacing (in points) to use between rows or columns.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var minimumLineSpacing: CGFloat { get set }
```

#### Discussion

If the delegate does not implement the [`collectionView(_:layout:minimumLineSpacingForSectionAt:)`](nscollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:).md) method, the flow layout object uses the value of this property to set the spacing between rows or columns.

For a vertically scrolling layout, the value represents the minimum spacing between successive rows. For a horizontally scrolling layout, the value represents the minimum spacing between successive columns. This spacing is not applied to the space between the header view and the first line or between the last line and the footer view. [`Figure 1`](nscollectionviewflowlayout/1402898-minimumlinespacing#1965631.md) shows how the line spacing is applied to rows of unevenly sized items, illustrating how the actual spacing between individual items may be greater than the minimum value.

![None](https://docs-assets.developer.apple.com/published/a03da83569fa7fe070ddd1d3bfdcbf34/media-1965631%402x.png)

The default value of this property is `10.0`.

## See Also

- [var minimumInteritemSpacing: CGFloat](nscollectionviewflowlayout/minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var estimatedItemSize: NSSize](nscollectionviewflowlayout/estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](nscollectionviewflowlayout/itemsize.md)
  The default size to use for items.
- [var sectionInset: NSEdgeInsets](nscollectionviewflowlayout/sectioninset.md)
  The margins used to lay out content in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/minimumlinespacing)*