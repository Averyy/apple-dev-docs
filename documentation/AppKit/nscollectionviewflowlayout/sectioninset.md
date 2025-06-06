# sectionInset

**Framework**: AppKit  
**Kind**: property

The margins used to lay out content in a section.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var sectionInset: NSEdgeInsets { get set }
```

#### Discussion

If the delegate does not implement the [`collectionView(_:layout:insetForSectionAt:)`](nscollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:).md) method, the flow layout object uses the value of this property to set the margins for each section.

Section insets reflect the spacing at the outer edges of the section. The margins affect the positioning of the header view, the minimum space on either side of each line of items, and the distance from the last line to the footer view, as shown in [`Figure 1`](nscollectionviewflowlayout/1402862-sectioninset#1965633.md). The margin insets do not affect the size of the header and footer views in the nonscrolling direction.

![None](https://docs-assets.developer.apple.com/published/e550263d1f3e21134b62450a79f9b768/media-1965633%402x.png)

The default insets are all set to `0`.

## See Also

- [var minimumLineSpacing: CGFloat](nscollectionviewflowlayout/minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var minimumInteritemSpacing: CGFloat](nscollectionviewflowlayout/minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var estimatedItemSize: NSSize](nscollectionviewflowlayout/estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](nscollectionviewflowlayout/itemsize.md)
  The default size to use for items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/sectioninset)*