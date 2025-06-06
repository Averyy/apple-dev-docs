# Layouts

**Framework**: UIKit

Arrange your collection view content in a highly configurable layout.

#### Overview

A collection view  defines the visual arrangement of the content in your collection. Layouts are designed to be flexible to let you create any kind of arrangement you need for your content, from simple to complex. The simplest type of collection view layout displays its items in a grid, but you can define layouts to arrange items however you like. For example, you might create a layout where items are arranged in a circle or vary in size. You can also change layouts dynamically at runtime whenever you need to present items differently, such as when a user rotates the device.

Collection view layouts are customizable and highly visual. For example, the App Store app uses a single collection view with custom layouts per section to showcase different kinds of content.

![Schematic representation of the App Store app on iOS, showing a collection view with a compositional layout. The layout is composed of two horizontally-scrolling sections that have different layouts. The top section shows one group with one item visible onscreen, with other groups peeking in from the sides of the screen. The bottom section shows one group that’s a column of three cells, each of those cells being an item.](https://docs-assets.developer.apple.com/published/1bcae7456df55cf8e3407bb9324c0d33/media-3568662%402x.png)

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/views/collections/).

## Topics

### Essentials
- [Implementing modern collection views](implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [class UICollectionViewCompositionalLayout](uicollectionviewcompositionallayout.md)
  A layout object that lets you combine items in highly adaptive and flexible visual arrangements.
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
### Configuration
- [class UICollectionViewCompositionalLayoutConfiguration](uicollectionviewcompositionallayoutconfiguration.md)
  An object that defines scroll direction, section spacing, and headers or footers for the layout.
- [typealias UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.
- [protocol NSCollectionLayoutEnvironment](nscollectionlayoutenvironment.md)
  A protocol used to provide information about the layout’s container and environment traits, such as size classes and display scale factor.
### Interaction
- [enum UICollectionLayoutSectionOrthogonalScrollingBehavior](uicollectionlayoutsectionorthogonalscrollingbehavior.md)
  The scrolling behavior of the layout’s sections in relation to the main layout axis.
### Appearance
- [class NSCollectionLayoutAnchor](nscollectionlayoutanchor.md)
  An object that defines how to attach a supplementary item to an item in a collection view.
- [class NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)
  An object used to add an extra visual decoration to an item in a collection view.
- [class NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
  An object used to add headers or footers to a collection view.
- [class NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md)
  An object used to add a background to a section of a collection view.
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
- [class UICollectionViewUpdateItem](uicollectionviewupdateitem.md)
  An object that describes a single change to make to an item in a collection view.
- [class UICollectionViewFocusUpdateContext](uicollectionviewfocusupdatecontext.md)
  A context object that stores information specific to a focus update in a collection view.
- [class UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md)
  A context object that declares which parts of your layout need to be updated when the layout is invalidated.
### Manual layouts
- [Customizing collection view layouts](customizing-collection-view-layouts.md)
  Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [class UICollectionViewLayout](uicollectionviewlayout.md)
  An abstract base class for generating layout information for a collection view.
- [class UICollectionViewFlowLayout](uicollectionviewflowlayout.md)
  A layout object that organizes items into a grid with optional header and footer views for each section.
- [class UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md)
  A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.
- [class UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md)
  A layout object that manages the layout-related attributes for a given item in a collection view.
- [class UICollectionViewFlowLayoutInvalidationContext](uicollectionviewflowlayoutinvalidationcontext.md)
  A set of properties for determining whether to recompute the size of items or their position in the layout.
### Data
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.

## See Also

- [Implementing modern collection views](implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/layouts)*