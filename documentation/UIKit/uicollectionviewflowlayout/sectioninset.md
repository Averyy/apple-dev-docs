# sectionInset

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The margins used to lay out content in a section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var sectionInset: UIEdgeInsets { get set }
```

```objc
@property (nonatomic) UIEdgeInsets sectionInset;
```

## Discussion

If the delegate object does not implement the [`collectionView(_:layout:insetForSectionAt:)`](../uicollectionviewdelegateflowlayout/collectionview%28_,layout,insetforsectionat%29.md) method, the flow layout uses the value in this property to set the margins for each section.

Section insets reflect the spacing at the outer edges of the section. The margins affect the initial position of the header view, the minimum space on either side of each line of items, and the distance from the last line to the footer view. The margin insets do not affect the size of the header and footer views in the non scrolling direction.

The default edge insets are all set to `0`.

## See Also

### Configuring item spacing
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing to use between lines of items in the grid.
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing to use between items in the same row.
- [var itemSize: CGSize](./itemsize.md)
  The default size to use for cells.
- [var estimatedItemSize: CGSize](./estimateditemsize.md)
  The estimated size of cells in the collection view.
- [class let automaticSize: CGSize](./automaticsize.md)
  A placeholder size for self-sizing cells.
- [var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.property.md)
  The boundary that section insets are defined in relation to.
- [UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.enum.md)
  Constants that describe the reference point of the section insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectioninset)*