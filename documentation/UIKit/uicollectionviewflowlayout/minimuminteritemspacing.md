# minimumInteritemSpacing

**Framework**: UIKit  
**Kind**: property

The minimum spacing to use between items in the same row.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumInteritemSpacing: CGFloat { get set }
```

#### Discussion

If the delegate object does not implement the [`collectionView(_:layout:minimumInteritemSpacingForSectionAt:)`](uicollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:).md) method, the flow layout uses the value in this property to set the spacing between items in the same line.

For a vertically scrolling grid, this value represents the minimum spacing between items in the same row. For a horizontally scrolling grid, this value represents the minimum spacing between items in the same column. This spacing is used to compute how many items can fit in a single line, but after the number of items is determined, the actual spacing may possibly be adjusted upward.

The default value of this property is 10.0.

## See Also

- [var minimumLineSpacing: CGFloat](uicollectionviewflowlayout/minimumlinespacing.md)
  The minimum spacing to use between lines of items in the grid.
- [var itemSize: CGSize](uicollectionviewflowlayout/itemsize.md)
  The default size to use for cells.
- [var estimatedItemSize: CGSize](uicollectionviewflowlayout/estimateditemsize.md)
  The estimated size of cells in the collection view.
- [class let automaticSize: CGSize](uicollectionviewflowlayout/automaticsize.md)
  A placeholder size for self-sizing cells.
- [var sectionInset: UIEdgeInsets](uicollectionviewflowlayout/sectioninset.md)
  The margins used to lay out content in a section.
- [var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference](uicollectionviewflowlayout/sectioninsetreference-swift.property.md)
  The boundary that section insets are defined in relation to.
- [UICollectionViewFlowLayout.SectionInsetReference](uicollectionviewflowlayout/sectioninsetreference-swift.enum.md)
  Constants that describe the reference point of the section insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/minimuminteritemspacing)*