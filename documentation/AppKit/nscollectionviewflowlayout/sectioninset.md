# sectionInset

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The margins used to lay out content in a section.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var sectionInset: NSEdgeInsets { get set }
```

```objc
@property NSEdgeInsets sectionInset;
```

#### Discussion

If the delegate does not implement the [`collectionView(_:layout:insetForSectionAt:)`](../nscollectionviewdelegateflowlayout/collectionview%28_,layout,insetforsectionat%29.md) method, the flow layout object uses the value of this property to set the margins for each section.

Section insets reflect the spacing at the outer edges of the section. The margins affect the positioning of the header view, the minimum space on either side of each line of items, and the distance from the last line to the footer view, as shown in [Figure 1](./api-1402862-sectioninset.md#1965633). The margin insets do not affect the size of the header and footer views in the nonscrolling direction.

![A diagram of a collection view section layout showing the section insets. A header labeled Header 1 sits at the top and a footer labeled Footer 1 sits at the bottom. Between them, a dashed outline marks the section, with nine items of varying sizes arranged in three rows inside it. Double-headed arrows labeled Top, Bottom, Left, and Right show the margins between the section’s outer edge and the items.](https://developer.apple.com/tutorials/images/com.apple.appkit/media-1965633@2x.png)

The default insets are all set to `0`.

## See Also

### Configuring the Item Spacing
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var estimatedItemSize: NSSize](./estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](./itemsize.md)
  The default size to use for items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/sectioninset)*