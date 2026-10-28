# itemSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The default size to use for cells.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var itemSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize itemSize;
```

## Discussion

If the delegate does not implement the [`collectionView(_:layout:sizeForItemAt:)`](../uicollectionviewdelegateflowlayout/collectionview%28_,layout,sizeforitemat%29.md) method, the flow layout uses the value in this property to set the size of each cell. This results in cells that all have the same size.

The default size value is (50.0, 50.0).

## See Also

### Configuring item spacing
- [var minimumLineSpacing: CGFloat](./minimumlinespacing.md)
  The minimum spacing to use between lines of items in the grid.
- [var minimumInteritemSpacing: CGFloat](./minimuminteritemspacing.md)
  The minimum spacing to use between items in the same row.
- [var estimatedItemSize: CGSize](./estimateditemsize.md)
  The estimated size of cells in the collection view.
- [class let automaticSize: CGSize](./automaticsize.md)
  A placeholder size for self-sizing cells.
- [var sectionInset: UIEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.
- [var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.property.md)
  The boundary that section insets are defined in relation to.
- [UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.enum.md)
  Constants that describe the reference point of the section insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/itemsize)*