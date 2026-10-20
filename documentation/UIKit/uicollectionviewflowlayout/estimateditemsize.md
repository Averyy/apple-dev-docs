# estimatedItemSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The estimated size of cells in the collection view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var estimatedItemSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize estimatedItemSize;
```

#### Discussion

Providing an estimated cell size can improve the performance of the collection view when the cells adjust their size dynamically. The estimated value lets the collection view defer some calculations to determine the actual size of its content. Cells that aren’t onscreen are assumed to be the estimated height.

The default value of this property is [`CGSizeZero`](../../CoreGraphics/cgsizezero.md). Setting it to any other value, like [`automaticSize`](./automaticsize.md), causes the collection view to query each cell for its actual size using the cell’s [`preferredLayoutAttributesFitting(_:)`](../uicollectionreusableview/preferredlayoutattributesfitting%28_%29.md) method.

If all of your cells are the same size, use the [`itemSize`](./itemsize.md) property, instead of this property, to specify the cell size instead.

## See Also

### Configuring item spacing
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing to use between lines of items in the grid.
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing to use between items in the same row.
- [var itemSize: CGSize](./itemsize.md)
  The default size to use for cells.
- [class let automaticSize: CGSize](./automaticsize.md)
  A placeholder size for self-sizing cells.
- [var sectionInset: UIEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.
- [var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.property.md)
  The boundary that section insets are defined in relation to.
- [UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.enum.md)
  Constants that describe the reference point of the section insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/estimateditemsize)*