# NSCollectionViewGridLayout

**Framework**: AppKit  
**Kind**: class

A layout that displays a single section of items in a row and column grid.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewGridLayout
```

#### Overview

The [`NSCollectionViewGridLayout`](nscollectionviewgridlayout.md) object provides the same layout behavior offered by the [`NSCollectionView`](nscollectionview.md) class prior to macOS 10.11, and you can use it in cases where you want to maintain the old appearance while still taking advantage of newer collection view features.

##### Configuring a Collection View to Use a Grid Layout

You can configure a collection view to use a grid layout object programmatically or at design time:

- At design time, set the Layout attribute of your collection view to Grid.
- Create an `NSCollectionViewGridLayout` object programmatically and assign it to the collection view’s [`collectionViewLayout`](nscollectionview/collectionviewlayout.md) property.

A grid layout displays only items and does not display supplementary views or decoration views. Use the properties of this class to configure the number of rows and columns in the grid. You can also use these properties to configure the spacing between items and the minimum sizes.

## Topics

### Specifying the Grid Parameters
- [var maximumNumberOfRows: Int](nscollectionviewgridlayout/maximumnumberofrows.md)
  The maximum number of rows to display in the collection view’s visible area.
- [var maximumNumberOfColumns: Int](nscollectionviewgridlayout/maximumnumberofcolumns.md)
  The maximum number of columns to display in the collection view’s visible area.
- [var minimumItemSize: NSSize](nscollectionviewgridlayout/minimumitemsize.md)
  The smallest allowable size for an item’s view.
- [var maximumItemSize: NSSize](nscollectionviewgridlayout/maximumitemsize.md)
  The largest allowable size for an item’s view.
### Specifying the Grid Layout Attributes
- [var minimumInteritemSpacing: CGFloat](nscollectionviewgridlayout/minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var minimumLineSpacing: CGFloat](nscollectionviewgridlayout/minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var margins: NSEdgeInsets](nscollectionviewgridlayout/margins.md)
  The amount of empty space (in points) around the grid’s content.
### Specifying the Grid Background Color
- [var backgroundColors: [NSColor]!](nscollectionviewgridlayout/backgroundcolors.md)
  The array of background colors to use when drawing the grid.

## Relationships

### Inherits From
- [NSCollectionViewLayout](nscollectionviewlayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Implementing modern collection views](../UIKit/implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [class NSCollectionViewFlowLayout](nscollectionviewflowlayout.md)
  A layout that organizes items into a flexible and configurable arrangement.
- [protocol NSCollectionViewDelegateFlowLayout](nscollectionviewdelegateflowlayout.md)
  A set of methods that a delegate implements to provide layout information to a flow layout object in a collection view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewgridlayout)*