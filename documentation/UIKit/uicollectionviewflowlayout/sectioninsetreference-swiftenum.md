# UICollectionViewFlowLayout.SectionInsetReference

**Framework**: UIKit  
**Kind**: enum

Constants that describe the reference point of the section insets.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum SectionInsetReference
```

## Topics

### Constants
- [UICollectionViewFlowLayout.SectionInsetReference.fromContentInset](uicollectionviewflowlayout/sectioninsetreference-swift.enum/fromcontentinset.md)
  Section insets are defined in relation to the collection view’s content inset.
- [UICollectionViewFlowLayout.SectionInsetReference.fromLayoutMargins](uicollectionviewflowlayout/sectioninsetreference-swift.enum/fromlayoutmargins.md)
  Section insets are defined in relation to the margins of the layout.
- [UICollectionViewFlowLayout.SectionInsetReference.fromSafeArea](uicollectionviewflowlayout/sectioninsetreference-swift.enum/fromsafearea.md)
  Section insets are defined in relation to the safe area of the layout.
### Initializers
- [init?(rawValue: Int)](uicollectionviewflowlayout/sectioninsetreference-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference](uicollectionviewflowlayout/sectioninsetreference-swift.property.md)
  The boundary that section insets are defined in relation to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.enum)*