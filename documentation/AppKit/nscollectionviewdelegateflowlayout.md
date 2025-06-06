# NSCollectionViewDelegateFlowLayout

**Framework**: AppKit  
**Kind**: protocol

A set of methods that a delegate implements to provide layout information to a flow layout object in a collection view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSCollectionViewDelegateFlowLayout : NSCollectionViewDelegate
```

#### Overview

Implement the methods of this protocol when you want to customize the layout behavior and perhaps return different values for different items or sections.

All of the methods in this protocol are optional, so you can implement only the methods you need to achieve the desired layout. If you do not implement a particular method, the flow layout object obtains default values from its own properties and applies them uniformly. Implement your methods in the object you assign to the [`delegate`](nscollectionview/delegate.md) property of the collection view itself.

## Topics

### Getting the Size of Items
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, sizeForItemAt: IndexPath) -> NSSize](nscollectionviewdelegateflowlayout/collectionview(_:layout:sizeforitemat:).md)
  Asks the delegate for the size of the specified item.
### Getting the Section Spacing
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, insetForSectionAt: Int) -> NSEdgeInsets](nscollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:).md)
  Asks the delegate for the margins to apply to content in the specified section.
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, minimumLineSpacingForSectionAt: Int) -> CGFloat](nscollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:).md)
  Asks the delegate for the spacing between successive rows or columns of a section.
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, minimumInteritemSpacingForSectionAt: Int) -> CGFloat](nscollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:).md)
  Asks the delegate for the spacing between successive items of a single row or column.
### Getting the Header and Footer Sizes
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, referenceSizeForHeaderInSection: Int) -> NSSize](nscollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforheaderinsection:).md)
  Asks the delegate for the size of the header view in the specified section.
- [func collectionView(NSCollectionView, layout: NSCollectionViewLayout, referenceSizeForFooterInSection: Int) -> NSSize](nscollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforfooterinsection:).md)
  Asks the delegate for the size of the footer view in the specified section.

## Relationships

### Inherits From
- [NSCollectionViewDelegate](nscollectionviewdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Implementing modern collection views](../UIKit/implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [class NSCollectionViewFlowLayout](nscollectionviewflowlayout.md)
  A layout that organizes items into a flexible and configurable arrangement.
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
- [enum NSCollectionLayoutSectionOrthogonalScrollingBehavior](nscollectionlayoutsectionorthogonalscrollingbehavior.md)
  The scrolling behavior of the layout’s sections in relation to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegateflowlayout)*