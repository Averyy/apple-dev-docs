# minimumInteritemSpacing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum spacing (in points) to use between items in the same row or column.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var minimumInteritemSpacing: CGFloat { get set }
```

```objc
@property CGFloat minimumInteritemSpacing;
```

#### Discussion

If the delegate does not implement the [`collectionView(_:layout:minimumInteritemSpacingForSectionAt:)`](../nscollectionviewdelegateflowlayout/collectionview%28_,layout,minimuminteritemspacingforsectionat%29.md) method, the flow layout object uses the value of this property to set the spacing between items in the same line.

For a vertically scrolling layout, the value represents the minimum spacing between items in the same row. For a horizontally scrolling layout, the value represents the minimum spacing between items in the same column. The layout object uses this spacing only to compute how many items can fit in a single row or column. The actual spacing may be increased after the number of items has been determined, as illustrated in [Figure 1](./api-1402872-minimuminteritemspacing.md#1965632).

![A diagram of a row of four items with a gap between each pair. In every gap, an upper arrow marks the actual interitem spacing, and a shorter lower arrow marks the minimum interitem spacing, so the actual spacing is wider than the minimum. A legend below the row labels the upper arrow Actual interitem spacing and the lower arrow Minimum interitem spacing.](https://developer.apple.com/tutorials/images/com.apple.appkit/media-1965632@2x.png)

The default value of this property is `10.0`.

## See Also

### Configuring the Item Spacing
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var estimatedItemSize: NSSize](./estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](./itemsize.md)
  The default size to use for items.
- [var sectionInset: NSEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/minimuminteritemspacing)*