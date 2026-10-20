# automaticSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A placeholder size for self-sizing cells.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class let automaticSize: CGSize
```

```c
extern const CGSize UICollectionViewFlowLayoutAutomaticSize;
```

#### Discussion

Set this constant as the value for the [`estimatedItemSize`](./estimateditemsize.md) property to enable self-sizing cells for your collection view. This is a non-zero, placeholder value that tells the collection view to query each cell for its actual size using the cell’s [`preferredLayoutAttributesFitting(_:)`](../uicollectionreusableview/preferredlayoutattributesfitting%28_%29.md) method.

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
- [var sectionInset: UIEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.
- [var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.property.md)
  The boundary that section insets are defined in relation to.
- [UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.enum.md)
  Constants that describe the reference point of the section insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/automaticsize)*