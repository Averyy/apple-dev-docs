# Collection View

**Framework**: AppKit

Display one or more subviews in a highly configurable arrangement.

## Topics

### View
- [class NSCollectionView](nscollectionview.md)
  An ordered collection of data items displayed in a customizable layout.
- [protocol NSCollectionViewSectionHeaderView](nscollectionviewsectionheaderview.md)
  A protocol that defines a button to control the collapse of a collection view’s section.
### Components
- [class NSCollectionLayoutItem](nscollectionlayoutitem.md)
  The most basic component of a collection view’s layout.
- [class NSCollectionLayoutGroup](nscollectionlayoutgroup.md)
  A container for a set of items that lays out the items along a path.
- [class NSCollectionLayoutSection](nscollectionlayoutsection.md)
  A container that combines a set of groups into distinct visual groupings.
### Size and spacing
- [class NSCollectionLayoutDimension](nscollectionlayoutdimension.md)
  An individual dimension representing an item’s width or height in a collection view.
- [class NSCollectionLayoutSize](nscollectionlayoutsize.md)
  The width and the height of an item in a collection view.
- [class NSCollectionLayoutSpacing](nscollectionlayoutspacing.md)
  An object that defines the space between or around items in a collection view.
- [class NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md)
  An object that defines the space around the edges of items in a collection view.
- [protocol NSCollectionLayoutContainer](nscollectionlayoutcontainer.md)
  A protocol used to provide information about the size and content insets of a layout’s container.
### Data
- [protocol NSCollectionViewDataSource](nscollectionviewdatasource.md)
  A set of methods that a data source object implements to provide the information and view objects that a collection view requires to present content.
- [protocol NSCollectionViewDelegate](nscollectionviewdelegate.md)
  A set of methods that you use to manage the behavior of a collection view.
- [class NSCollectionViewDiffableDataSource](nscollectionviewdiffabledatasource-axww.md)
  The object you use to manage data and provide items for a collection view.
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.
### Items
- [class NSCollectionViewItem](nscollectionviewitem.md)
  The visual representation for a single data element in a collection view.
- [protocol NSCollectionViewElement](nscollectionviewelement.md)
  A set of methods that you use to manage the content in a collection view.
### Layouts
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
- [enum NSCollectionLayoutSectionOrthogonalScrollingBehavior](nscollectionlayoutsectionorthogonalscrollingbehavior.md)
  The scrolling behavior of the layout’s sections in relation to the main layout axis.
### Appearance
- [class NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
  An object used to add headers or footers to a collection view.
- [class NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)
  An object used to add an extra visual decoration to an item in a collection view.
- [class NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md)
  An object used to add a background to a section of a collection view.
- [class NSCollectionLayoutAnchor](nscollectionlayoutanchor.md)
  An object that defines how to attach a supplementary item to an item in a collection view.
### Advanced layouts
- [class NSCollectionLayoutGroupCustomItem](nscollectionlayoutgroupcustomitem.md)
  An item used in a group with a custom layout arrangement.
- [typealias NSCollectionLayoutGroupCustomItemProvider](nscollectionlayoutgroupcustomitemprovider.md)
  A closure that creates and returns each of the custom group’s items.
### Layout updates
- [protocol NSCollectionLayoutVisibleItem](nscollectionlayoutvisibleitem.md)
  An item that’s currently visible within the bounds of a section.
- [typealias NSCollectionLayoutSectionVisibleItemsInvalidationHandler](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md)
  A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.
### Configuration
- [protocol NSCollectionLayoutEnvironment](nscollectionlayoutenvironment.md)
  A protocol used to provide information about the layout’s container and environment traits, such as size classes and display scale factor.
### Updates
- [class NSCollectionViewUpdateItem](nscollectionviewupdateitem.md)
  A description of a single change to make to an item in a collection view.
- [class NSCollectionViewLayoutInvalidationContext](nscollectionviewlayoutinvalidationcontext.md)
  An object that identifies the portions of your layout that need to be updated.
- [class NSCollectionViewFlowLayoutInvalidationContext](nscollectionviewflowlayoutinvalidationcontext.md)
  An object that identifies the portions of a flow layout object that need to be updated.

## See Also

- [Browser View](browser-view.md)
  Provide a column-based interface for viewing and navigating hierarchical information.
- [Outline View](outline-view.md)
  Display a list-based interface for hierarchical data, where each level of hierarchy is indented from the previous one.
- [Table View](table-view.md)
  Display custom data in rows and columns.
- [class NSTextView](nstextview.md)
  A view that draws text and handles user interactions with that text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/collection-view)*