# UICollectionLayoutSectionOrthogonalScrollingBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The scrolling behavior of the layout’s sections in relation to the main layout axis.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum UICollectionLayoutSectionOrthogonalScrollingBehavior
```

```c
enum UICollectionLayoutSectionOrthogonalScrollingBehavior : NSInteger;
```

#### Overview

By default, each section lays out its content along the main axis of its layout, defined by the layout configuration’s [`scrollDirection`](./uicollectionviewcompositionallayoutconfiguration/scrolldirection.md) property. You can change this behavior for a particular section by setting its [`orthogonalScrollingBehavior`](./nscollectionlayoutsection/orthogonalscrollingbehavior.md) property to a different value than its default [`UICollectionLayoutSectionOrthogonalScrollingBehavior.none`](./uicollectionlayoutsectionorthogonalscrollingbehavior/none.md). Setting any other value for this property makes the section lay out its content orthogonally to the main layout axis.

![Diagram of a collection view layout with multiple sections. The collection view sections are laid out vertically, so the collection view scrolls on the vertical axis to reveal more content. The content in the top section of the collection view scrolls on the horizontal axis, orthogonally to the main layout axis of the collection view’s layout.](https://developer.apple.com/tutorials/images/com.apple.uikit/media-3570451@2x.png)

## Topics

### Constants
- [UICollectionLayoutSectionOrthogonalScrollingBehavior.none](./uicollectionlayoutsectionorthogonalscrollingbehavior/none.md)
  The section does not allow users to scroll its content orthogonally.
- [UICollectionLayoutSectionOrthogonalScrollingBehavior.continuous](./uicollectionlayoutsectionorthogonalscrollingbehavior/continuous.md)
  The section allows users to scroll its content orthogonally with continuous scrolling.
- [UICollectionLayoutSectionOrthogonalScrollingBehavior.continuousGroupLeadingBoundary](./uicollectionlayoutsectionorthogonalscrollingbehavior/continuousgroupleadingboundary.md)
  The section allows users to scroll its content orthogonally, coming to a natural stop at the leading boundary of the visible group.
- [UICollectionLayoutSectionOrthogonalScrollingBehavior.paging](./uicollectionlayoutsectionorthogonalscrollingbehavior/paging.md)
  The section allows users to page its content orthogonally.
- [UICollectionLayoutSectionOrthogonalScrollingBehavior.groupPaging](./uicollectionlayoutsectionorthogonalscrollingbehavior/grouppaging.md)
  The section allows users to page its content orthogonally one group at a time.
- [UICollectionLayoutSectionOrthogonalScrollingBehavior.groupPagingCentered](./uicollectionlayoutsectionorthogonalscrollingbehavior/grouppagingcentered.md)
  The section allows users to page its content orthogonally one group at a time, centering each group.
### Initializers
- [init?(rawValue: Int)](./uicollectionlayoutsectionorthogonalscrollingbehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingbehavior)*