# sectionInsetReference

**Framework**: UIKit  
**Kind**: property

The boundary that section insets are defined in relation to.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference { get set }
```

#### Discussion

The default value of this property is [`UICollectionViewFlowLayout.SectionInsetReference.fromContentInset`](uicollectionviewflowlayout/sectioninsetreference-swift.enum/fromcontentinset.md).

The minimum value of this property is always the collection view’s [`contentInset`](uiscrollview/contentinset.md). For example, if the value of this property is [`UICollectionViewFlowLayout.SectionInsetReference.fromSafeArea`](uicollectionviewflowlayout/sectioninsetreference-swift.enum/fromsafearea.md), but the adjusted content inset is greater than the combination of the safe area and section insets, then the section’s content is aligned with the content inset instead.

## See Also

- [var minimumLineSpacing: CGFloat](uicollectionviewflowlayout/minimumlinespacing.md)
  The minimum spacing to use between lines of items in the grid.
- [var minimumInteritemSpacing: CGFloat](uicollectionviewflowlayout/minimuminteritemspacing.md)
  The minimum spacing to use between items in the same row.
- [var itemSize: CGSize](uicollectionviewflowlayout/itemsize.md)
  The default size to use for cells.
- [var estimatedItemSize: CGSize](uicollectionviewflowlayout/estimateditemsize.md)
  The estimated size of cells in the collection view.
- [class let automaticSize: CGSize](uicollectionviewflowlayout/automaticsize.md)
  A placeholder size for self-sizing cells.
- [var sectionInset: UIEdgeInsets](uicollectionviewflowlayout/sectioninset.md)
  The margins used to lay out content in a section.
- [UICollectionViewFlowLayout.SectionInsetReference](uicollectionviewflowlayout/sectioninsetreference-swift.enum.md)
  Constants that describe the reference point of the section insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.property)*