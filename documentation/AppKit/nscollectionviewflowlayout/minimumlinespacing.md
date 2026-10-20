# minimumLineSpacing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum spacing (in points) to use between rows or columns.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var minimumLineSpacing: CGFloat { get set }
```

```objc
@property CGFloat minimumLineSpacing;
```

#### Discussion

If the delegate does not implement the [`collectionView(_:layout:minimumLineSpacingForSectionAt:)`](../nscollectionviewdelegateflowlayout/collectionview%28_,layout,minimumlinespacingforsectionat%29.md) method, the flow layout object uses the value of this property to set the spacing between rows or columns.

For a vertically scrolling layout, the value represents the minimum spacing between successive rows. For a horizontally scrolling layout, the value represents the minimum spacing between successive columns. This spacing is not applied to the space between the header view and the first line or between the last line and the footer view. [Figure 1](./api-1402898-minimumlinespacing.md#1965631) shows how the line spacing is applied to rows of unevenly sized items, illustrating how the actual spacing between individual items may be greater than the minimum value.

![A diagram of two rows of unevenly sized items, three in each row, with a shaded band between them that marks the minimum line spacing. Double-headed arrows show the actual line spacing between the rows in each column, which is larger than the minimum wherever the items are shorter. A legend identifies the arrow style for Actual line spacing and the arrow style for Minimum line spacing.](https://developer.apple.com/tutorials/images/com.apple.appkit/media-1965631@2x.png)

The default value of this property is `10.0`.

## See Also

### Configuring the Item Spacing
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var estimatedItemSize: NSSize](./estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](./itemsize.md)
  The default size to use for items.
- [var sectionInset: NSEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout/minimumlinespacing)*