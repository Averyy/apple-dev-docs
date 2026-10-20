# UICollectionViewFlowLayout.SectionInsetReference

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UICollectionViewFlowLayoutSectionInsetReference : NSInteger;
```

## Topics

### Constants
- [UICollectionViewFlowLayout.SectionInsetReference.fromContentInset](./sectioninsetreference-swift.enum/fromcontentinset.md)
  Section insets are defined in relation to the collection view’s content inset.
- [UICollectionViewFlowLayout.SectionInsetReference.fromLayoutMargins](./sectioninsetreference-swift.enum/fromlayoutmargins.md)
  Section insets are defined in relation to the margins of the layout.
- [UICollectionViewFlowLayout.SectionInsetReference.fromSafeArea](./sectioninsetreference-swift.enum/fromsafearea.md)
  Section insets are defined in relation to the safe area of the layout.
### Initializers
- [init?(rawValue: Int)](./sectioninsetreference-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var sectionInset: UIEdgeInsets](./sectioninset.md)
  The margins used to lay out content in a section.
- [var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference](./sectioninsetreference-swift.property.md)
  The boundary that section insets are defined in relation to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.enum)*