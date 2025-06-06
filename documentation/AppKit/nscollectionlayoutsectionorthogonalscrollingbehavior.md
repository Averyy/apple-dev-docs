# NSCollectionLayoutSectionOrthogonalScrollingBehavior

**Framework**: AppKit  
**Kind**: enum

The scrolling behavior of the layout’s sections in relation to the main layout axis.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum NSCollectionLayoutSectionOrthogonalScrollingBehavior
```

#### Overview

By default, each section lays out its content along the main axis of its layout, defined by the layout configuration’s [`scrollDirection`](nscollectionviewcompositionallayoutconfiguration/scrolldirection.md) property. You can change this behavior for a particular section by setting its [`orthogonalScrollingBehavior`](nscollectionlayoutsection/orthogonalscrollingbehavior.md) property to a different value than its default [`NSCollectionLayoutSectionOrthogonalScrollingBehavior.none`](nscollectionlayoutsectionorthogonalscrollingbehavior/none.md). Setting any other value for this property makes the section lay out its content orthogonally to the main layout axis.

## Topics

### Enumeration Cases
- [NSCollectionLayoutSectionOrthogonalScrollingBehavior.none](nscollectionlayoutsectionorthogonalscrollingbehavior/none.md)
  The section does not allow users to scroll its content orthogonally.
- [NSCollectionLayoutSectionOrthogonalScrollingBehavior.continuous](nscollectionlayoutsectionorthogonalscrollingbehavior/continuous.md)
  The section allows users to scroll its content orthogonally with continuous scrolling.
- [NSCollectionLayoutSectionOrthogonalScrollingBehavior.continuousGroupLeadingBoundary](nscollectionlayoutsectionorthogonalscrollingbehavior/continuousgroupleadingboundary.md)
  The section allows users to scroll its content orthogonally, coming to a natural stop at the leading boundary of the visible group.
- [NSCollectionLayoutSectionOrthogonalScrollingBehavior.paging](nscollectionlayoutsectionorthogonalscrollingbehavior/paging.md)
  The section allows users to page its content orthogonally.
- [NSCollectionLayoutSectionOrthogonalScrollingBehavior.groupPaging](nscollectionlayoutsectionorthogonalscrollingbehavior/grouppaging.md)
  The section allows users to page its content orthogonally one group at a time.
- [NSCollectionLayoutSectionOrthogonalScrollingBehavior.groupPagingCentered](nscollectionlayoutsectionorthogonalscrollingbehavior/grouppagingcentered.md)
  The section allows users to page its content orthogonally one group at a time, centering each group.
### Initializers
- [init?(rawValue: Int)](nscollectionlayoutsectionorthogonalscrollingbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing modern collection views](../UIKit/implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [class NSCollectionViewFlowLayout](nscollectionviewflowlayout.md)
  A layout that organizes items into a flexible and configurable arrangement.
- [protocol NSCollectionViewDelegateFlowLayout](nscollectionviewdelegateflowlayout.md)
  A set of methods that a delegate implements to provide layout information to a flow layout object in a collection view.
- [class NSCollectionViewGridLayout](nscollectionviewgridlayout.md)
  A layout that displays a single section of items in a row and column grid.
- [class NSCollectionViewTransitionLayout](nscollectionviewtransitionlayout.md)
  An object that implements custom behaviors when changing from one layout to another in a collection view.
- [class NSCollectionViewLayoutAttributes](nscollectionviewlayoutattributes.md)
  An object that contains layout-related attributes for an element in a collection view.
- [class NSCollectionViewLayout](nscollectionviewlayout.md)
  An abstract base class that you subclass and use to generate layout information for a collection view.
- [class NSCollectionViewCompositionalLayout](nscollectionviewcompositionallayout.md)
  A layout object that lets you combine items in highly adaptive and flexible visual arrangements.
- [class NSCollectionViewCompositionalLayoutConfiguration](nscollectionviewcompositionallayoutconfiguration.md)
  An object that defines scroll direction, section spacing, and headers or footers for the layout.
- [typealias NSCollectionViewCompositionalLayoutSectionProvider](nscollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsectionorthogonalscrollingbehavior)*