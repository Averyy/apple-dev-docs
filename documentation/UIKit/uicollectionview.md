# UICollectionView

**Framework**: UIKit  
**Kind**: class

An object that manages an ordered collection of data items and presents them using customizable layouts.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionView
```

## Mentions

- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Overview

When you add a collection view to your user interface, your app’s main job is to manage the data associated with that collection view. The collection view gets its data from the data source object, stored in the collection view’s [`dataSource`](uicollectionview/datasource.md) property. For your data source, you can use a [`UICollectionViewDiffableDataSource`](uicollectionviewdiffabledatasource-9tqpa.md) object, which provides the behavior you need to simply and efficiently manage updates to your collection view’s data and user interface. Alternatively, you can create a custom data source object by adopting the [`UICollectionViewDataSource`](uicollectionviewdatasource.md) protocol.

Data in the collection view is organized into individual items, which you can group into sections for presentation. An item is the smallest unit of data you want to present. For example, in a photos app, an item might be a single image. The collection view presents items onscreen using a cell, which is an instance of the [`UICollectionViewCell`](uicollectionviewcell.md) class that your data source configures and provides.

![A collection view using the flow layout](https://docs-assets.developer.apple.com/published/6771c5b19977b706255e0fe4a5cefa04/media-2923198%402x.png)

In addition to its cells, a collection view can present data using other types of views. These supplementary views can be, for example, section headers and footers that are separate from the individual cells but still convey information. Support for supplementary views is optional and defined by the collection view’s layout object, which is also responsible for defining the placement of those views.

Besides embedding a [`UICollectionView`](uicollectionview.md) in your user interface, you use the methods of the collection view to ensure that the visual presentation of items matches the order in your data source object. A [`UICollectionViewDiffableDataSource`](uicollectionviewdiffabledatasource-9tqpa.md) object manages this process automatically. If you’re using a custom data source, then whenever you add, delete, or rearrange data in your collection, you use the methods of [`UICollectionView`](uicollectionview.md) to insert, delete, and rearrange the corresponding cells.

You also use the collection view object to manage the selected items, although for this behavior the collection view works with its associated [`delegate`](uicollectionview/delegate.md) object.

##### Layouts

A layout object defines the visual arrangement of the content in the collection view. A subclass of the [`UICollectionViewLayout`](uicollectionviewlayout.md) class, the layout object defines the organization and location of all cells and supplementary views inside the collection view. Although it defines their locations, the layout object doesn’t actually apply that information to the corresponding views. The collection view applies layout information to the corresponding views because the creation of cells and supplementary views involves coordination between the collection view and your data source object. The layout object is like another data source, except it provides visual information instead of item data.

You typically specify a layout object when you create a collection view, but you can also change the layout of a collection view dynamically. The layout object is stored in the [`collectionViewLayout`](uicollectionview/collectionviewlayout.md) property. Setting this property directly updates the layout immediately, without animating the changes. If you want to animate the changes, call the [`setCollectionViewLayout(_:animated:completion:)`](uicollectionview/setcollectionviewlayout(_:animated:completion:).md) method instead.

To create an interactive transition — one that is driven by a gesture recognizer or touch events — use the [`startInteractiveTransition(to:completion:)`](uicollectionview/startinteractivetransition(to:completion:).md) method to change the layout object. That method installs an intermediate layout object, which works with your gesture recognizer or event-handling code to track the transition progress. When your event-handling code determines that the transition is finished, it calls the [`finishInteractiveTransition()`](uicollectionview/finishinteractivetransition().md) or [`cancelInteractiveTransition()`](uicollectionview/cancelinteractivetransition().md) method to remove the intermediate layout object and install the intended target layout object.

For more information, see [`Layouts`](layouts.md).

##### Cells and Supplementary Views

The collection view’s data source object provides both the content for items and the views used to present that content. When the collection view first loads its content, it asks its data source to provide a view for each visible item. The collection view maintains a queue or list of view objects that the data source has marked for reuse. Instead of creating new views explicitly in your code, you always dequeue views.

There are two methods for dequeueing views. The one you use depends on which type of view has been requested:

- Use the [`dequeueReusableCell(withReuseIdentifier:for:)`](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md) to get a cell for an item in the collection view.
- Use the [`dequeueReusableSupplementaryView(ofKind:withReuseIdentifier:for:)`](uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:).md) method to get a supplementary view requested by the layout object.

Before you call either of these methods, you must tell the collection view how to create the corresponding view if one doesn’t already exist. For this, you must register either a class or a nib file with the collection view. For example, when registering cells, you use the [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md) method to register a class or the [`register(_:forCellWithReuseIdentifier:)`](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md) method to register a nib file. As part of the registration process, you specify the reuse identifier that identifies the purpose of the view. This is the same string you use when dequeueing the view later.

After dequeueing the appropriate view in your data source method, configure its content and return it to the collection view for use. After getting the layout information from the layout object, the collection view applies it to the view and displays it.

##### Data Prefetching

Collection views provide two prefetching techniques you can use to improve responsiveness:

-  prepares cells in advance of the time they’re required. When a collection view requires a large number of cells simultaneously — for example, a new row of cells in grid layout — the cells are requested earlier than the time required for display. Cell rendering is therefore spread across multiple layout passes, resulting in a smoother scrolling experience. Cell prefetching is enabled by default.
-  provides a mechanism whereby you’re notified of the data requirements of a collection view in advance of the requests for cells. This is useful if the content of your cells relies on an expensive data loading process, such as a network request. Assign an object that conforms to the [`UICollectionViewDataSourcePrefetching`](uicollectionviewdatasourceprefetching.md) protocol to the [`prefetchDataSource`](uicollectionview/prefetchdatasource.md) property to receive notifications of when to prefetch data for cells.

##### Reorder Items Interactively

Collection views allow you to move items around based on user interactions. Typically, the order of items in a collection view is defined by your data source. If you allow users to reorder items, you can configure a gesture recognizer to track the user’s interactions with a collection view item and update that item’s position.

To begin the interactive repositioning of an item, call the [`beginInteractiveMovementForItem(at:)`](uicollectionview/begininteractivemovementforitem(at:).md) method of the collection view. While your gesture recognizer is tracking touch events, call the [`updateInteractiveMovementTargetPosition(_:)`](uicollectionview/updateinteractivemovementtargetposition(_:).md) method to report changes in the touch location. When you’re done tracking the gesture, call the [`endInteractiveMovement()`](uicollectionview/endinteractivemovement().md) or [`cancelInteractiveMovement()`](uicollectionview/cancelinteractivemovement().md) method to conclude the interactions and update the collection view.

During user interactions, the collection view invalidates its layout dynamically to reflect the current position of the item. If you do nothing, the default layout behavior repositions the items for you, but you can customize the layout animations if you want. When interactions finish, the collection view updates its data source object with the new location of the item.

The [`UICollectionViewController`](uicollectionviewcontroller.md) class provides a default gesture recognizer that you can use to rearrange items in its managed collection view. To install this gesture recognizer, set the [`installsStandardGestureForInteractiveMovement`](uicollectionviewcontroller/installsstandardgestureforinteractivemovement.md) property of the collection view controller to [`true`](https://developer.apple.com/documentation/swift/true).

##### Interface Builder Attributes

The following table lists the attributes that you configure for collection views in Interface Builder.

| Attribute | Description |
| --- | --- |
| Items | The number of prototype cells. This property controls the specified number of prototype cells for you to configure in your storyboard. Collection views must always have at least one cell and may have multiple cells for displaying different types of content or for displaying the same content in different ways. |
| Layout | The layout object to use. Use this control to select between the [`UICollectionViewFlowLayout`](uicollectionviewflowlayout.md) object and a custom layout object that you define. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) When the flow layout is selected, you can also configure the scrolling direction for the collection view’s content and whether the flow layout has header and footer views. Enabling header and footer views adds reusable views to your storyboard that you can configure with your header and footer content. You can also create those views programmatically. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) When a custom layout is selected, you must specify the [`UICollectionViewLayout`](uicollectionviewlayout.md) subclass to use. |

When the Flow layout is selected, the Size inspector for the collection view contains additional attributes for configuring flow layout metrics. Use those attributes to configure the size of your cells, the size of headers and footers, the minimum spacing between cells, and any margins around each section of cells. For more information about the meaning of the flow layout metrics, see [`UICollectionViewFlowLayout`](uicollectionviewflowlayout.md).

##### Internationalization

A collection view has no direct content of its own to internationalize. Instead, you internationalize the cells and reusable views of the collection view. For more information about internationalization, see `Localization`.

##### Accessibility

A collection view has no content of its own to make accessible. If your cells and reusable views contain standard UIKit controls such as [`UILabel`](uilabel.md) and [`UITextField`](uitextfield.md), you can make those controls accessible. When a collection view changes its onscreen layout, it posts the [`layoutChanged`](uiaccessibility/notification/layoutchanged.md) notification.

For general information about making your interface accessible, see [`Accessibility for UIKit`](accessibility-for-uikit.md).

## Topics

### Creating a collection view
- [init(frame: CGRect, collectionViewLayout: UICollectionViewLayout)](uicollectionview/init(frame:collectionviewlayout:).md)
  Creates a collection view object with the specified frame and layout.
- [init?(coder: NSCoder)](uicollectionview/init(coder:).md)
  Creates a collection view object from data in a given unarchiver.
### Providing the collection view data
- [var dataSource: (any UICollectionViewDataSource)?](uicollectionview/datasource.md)
  The object that provides the data for the collection view.
- [class UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md)
  The object you use to manage data and provide cells for a collection view.
- [protocol UICollectionViewDataSource](uicollectionviewdatasource.md)
  The methods adopted by the object you use to manage data and provide cells for a collection view.
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
### Prefetching collection view cells and data
- [var isPrefetchingEnabled: Bool](uicollectionview/isprefetchingenabled.md)
  A Boolean value that indicates whether cell and data prefetching are enabled.
- [var prefetchDataSource: (any UICollectionViewDataSourcePrefetching)?](uicollectionview/prefetchdatasource.md)
  The object that acts as the prefetching data source for the collection view, receiving notifications of upcoming cell data requirements.
- [protocol UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
### Managing collection view interactions
- [var delegate: (any UICollectionViewDelegate)?](uicollectionview/delegate.md)
  The object that acts as the delegate of the collection view.
- [protocol UICollectionViewDelegate](uicollectionviewdelegate.md)
  The methods adopted by the object you use to manage user interactions with items in a collection view.
### Creating cells
- [UICollectionView.CellRegistration](uicollectionview/cellregistration.md)
  A registration for the collection view’s cells.
- [func dequeueConfiguredReusableCell<Cell, Item>(using: UICollectionView.CellRegistration<Cell, Item>, for: IndexPath, item: Item?) -> Cell](uicollectionview/dequeueconfiguredreusablecell(using:for:item:).md)
  Dequeues a configured reusable cell object.
- [func register(AnyClass?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-3vaho.md)
  Registers a class for use in creating new collection view cells.
- [func register(UINib?, forCellWithReuseIdentifier: String)](uicollectionview/register(_:forcellwithreuseidentifier:)-6z6t4.md)
  Registers a nib file for use in creating new collection view cells.
- [func dequeueReusableCell(withReuseIdentifier: String, for: IndexPath) -> UICollectionViewCell](uicollectionview/dequeuereusablecell(withreuseidentifier:for:).md)
  Dequeues a reusable cell object located by its identifier.
### Creating headers and footers
- [UICollectionView.SupplementaryRegistration](uicollectionview/supplementaryregistration.md)
  A registration for the collection view’s supplementary views.
- [func dequeueConfiguredReusableSupplementary<Supplementary>(using: UICollectionView.SupplementaryRegistration<Supplementary>, for: IndexPath) -> Supplementary](uicollectionview/dequeueconfiguredreusablesupplementary(using:for:).md)
  Dequeues a configured reusable supplementary view object.
- [func register(AnyClass?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-661io.md)
  Registers a class for use in creating supplementary views for the collection view.
- [func register(UINib?, forSupplementaryViewOfKind: String, withReuseIdentifier: String)](uicollectionview/register(_:forsupplementaryviewofkind:withreuseidentifier:)-9hn73.md)
  Registers a nib file for use in creating supplementary views for the collection view.
- [func dequeueReusableSupplementaryView(ofKind: String, withReuseIdentifier: String, for: IndexPath) -> UICollectionReusableView](uicollectionview/dequeuereusablesupplementaryview(ofkind:withreuseidentifier:for:).md)
  Dequeues a reusable supplementary view located by its identifier and kind.
### Configuring the background view
- [var backgroundView: UIView?](uicollectionview/backgroundview.md)
  The view that provides the background appearance.
### Changing the layout
- [var collectionViewLayout: UICollectionViewLayout](uicollectionview/collectionviewlayout.md)
  The layout used to organize the collected view’s items.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool)](uicollectionview/setcollectionviewlayout(_:animated:).md)
  Changes the collection view’s layout and optionally animates the change.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)?)](uicollectionview/setcollectionviewlayout(_:animated:completion:).md)
  Changes the collection view’s layout and notifies you when the animations complete.
- [func startInteractiveTransition(to: UICollectionViewLayout, completion: UICollectionView.LayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout](uicollectionview/startinteractivetransition(to:completion:).md)
  Changes the collection view’s current layout using an interactive transition effect.
- [func finishInteractiveTransition()](uicollectionview/finishinteractivetransition.md)
  Tells the collection view to finish an interactive transition by installing the intended target layout.
- [func cancelInteractiveTransition()](uicollectionview/cancelinteractivetransition.md)
  Tells the collection view to cancel an interactive transition and return to its original layout object.
- [UICollectionView.LayoutInteractiveTransitionCompletion](uicollectionview/layoutinteractivetransitioncompletion.md)
  The completion block called at the end of an interactive transition for a collection view.
### Getting the state of the collection view
- [var numberOfSections: Int](uicollectionview/numberofsections.md)
  The number of sections displayed by the collection view.
- [func numberOfItems(inSection: Int) -> Int](uicollectionview/numberofitems(insection:).md)
  Fetches the count of items in the specified section.
- [var visibleCells: [UICollectionViewCell]](uicollectionview/visiblecells.md)
  An array of visible cells currently displayed by the collection view.
### Inserting, moving, and deleting Items
- [func insertItems(at: [IndexPath])](uicollectionview/insertitems(at:).md)
  Inserts new items at the specified index paths.
- [func moveItem(at: IndexPath, to: IndexPath)](uicollectionview/moveitem(at:to:).md)
  Moves an item from one location to another in the collection view.
- [func deleteItems(at: [IndexPath])](uicollectionview/deleteitems(at:).md)
  Deletes the items at the specified index paths.
### Inserting, moving, and deleting sections
- [func insertSections(IndexSet)](uicollectionview/insertsections(_:).md)
  Inserts new sections at the specified indexes.
- [func moveSection(Int, toSection: Int)](uicollectionview/movesection(_:tosection:).md)
  Moves a section from one location to another in the collection view.
- [func deleteSections(IndexSet)](uicollectionview/deletesections(_:).md)
  Deletes the sections at the specified indexes.
### Reordering items interactively
- [func beginInteractiveMovementForItem(at: IndexPath) -> Bool](uicollectionview/begininteractivemovementforitem(at:).md)
  Initiates the interactive movement of the item at the specified index path.
- [func updateInteractiveMovementTargetPosition(CGPoint)](uicollectionview/updateinteractivemovementtargetposition(_:).md)
  Updates the position of the item within the collection view’s bounds.
- [func endInteractiveMovement()](uicollectionview/endinteractivemovement.md)
  Ends interactive movement tracking and moves the target item to its new location.
- [func cancelInteractiveMovement()](uicollectionview/cancelinteractivemovement.md)
  Ends interactive movement tracking and returns the target item to its original location.
### Managing drag interactions
- [var dragDelegate: (any UICollectionViewDragDelegate)?](uicollectionview/dragdelegate.md)
  The delegate object that manages the dragging of items from the collection view.
- [protocol UICollectionViewDragDelegate](uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [var hasActiveDrag: Bool](uicollectionview/hasactivedrag.md)
  A Boolean value that indicates whether items were lifted from the collection view and have not yet been dropped.
- [var dragInteractionEnabled: Bool](uicollectionview/draginteractionenabled.md)
  A Boolean value that indicates whether the collection view supports dragging content.
### Managing drop interactions
- [var dropDelegate: (any UICollectionViewDropDelegate)?](uicollectionview/dropdelegate.md)
  The delegate object that manages the dropping of items into the collection view.
- [protocol UICollectionViewDropDelegate](uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [var hasActiveDrop: Bool](uicollectionview/hasactivedrop.md)
  A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [var reorderingCadence: UICollectionView.ReorderingCadence](uicollectionview/reorderingcadence-swift.property.md)
  The speed at which items in the collection view are reordered to show potential drop locations.
- [UICollectionView.ReorderingCadence](uicollectionview/reorderingcadence-swift.enum.md)
  Constants indicating the speed at which collection view items are reorganized during a drop.
### Selecting cells
- [var indexPathsForSelectedItems: [IndexPath]?](uicollectionview/indexpathsforselecteditems.md)
  The index paths for the selected items.
- [func selectItem(at: IndexPath?, animated: Bool, scrollPosition: UICollectionView.ScrollPosition)](uicollectionview/selectitem(at:animated:scrollposition:).md)
  Selects the item at the specified index path and optionally scrolls it into view.
- [func deselectItem(at: IndexPath, animated: Bool)](uicollectionview/deselectitem(at:animated:).md)
  Deselects the item at the specified index.
- [var allowsSelection: Bool](uicollectionview/allowsselection.md)
  A Boolean value that indicates whether users can select items in the collection view.
- [var allowsMultipleSelection: Bool](uicollectionview/allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one item in the collection view.
- [var allowsSelectionDuringEditing: Bool](uicollectionview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the collection view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](uicollectionview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uicollectionview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
### Putting the collection view into edit mode
- [var isEditing: Bool](uicollectionview/isediting.md)
  A Boolean value that determines whether the collection view is in editing mode.
### Locating items and views in the collection view
- [func indexPathForItem(at: CGPoint) -> IndexPath?](uicollectionview/indexpathforitem(at:).md)
  Gets the index path of the item at the specified point in the collection view.
- [var indexPathsForVisibleItems: [IndexPath]](uicollectionview/indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [func indexPath(for: UICollectionViewCell) -> IndexPath?](uicollectionview/indexpath(for:).md)
  Gets the index path of the specified cell.
- [func cellForItem(at: IndexPath) -> UICollectionViewCell?](uicollectionview/cellforitem(at:).md)
  Gets the cell object at the index path you specify.
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:).md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](uicollectionview/supplementaryview(forelementkind:at:).md)
  Gets the supplementary view at the specified index path.
- [func visibleSupplementaryViews(ofKind: String) -> [UICollectionReusableView]](uicollectionview/visiblesupplementaryviews(ofkind:).md)
  Gets an array of the visible supplementary views of the specified kind.
### Getting layout information
- [func layoutAttributesForItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionview/layoutattributesforitem(at:).md)
  Gets the layout information for the item at the specified index path.
- [func layoutAttributesForSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionview/layoutattributesforsupplementaryelement(ofkind:at:).md)
  Gets the layout information for the specified supplementary view.
### Scrolling an item into view
- [func scrollToItem(at: IndexPath, at: UICollectionView.ScrollPosition, animated: Bool)](uicollectionview/scrolltoitem(at:at:animated:).md)
  Scrolls the collection view contents until the specified item is visible.
- [UICollectionView.ScrollPosition](uicollectionview/scrollposition.md)
  Constants that indicate how to scroll an item into the visible portion of the collection view.
- [UICollectionView.ScrollDirection](uicollectionview/scrolldirection.md)
  Constants that indicate the direction of scrolling for the layout.
### Animating multiple changes to the collection view
- [func performBatchUpdates((() -> Void)?, completion: ((Bool) -> Void)?)](uicollectionview/performbatchupdates(_:completion:).md)
  Animates multiple insert, delete, reload, and move operations as a group.
### Reloading content
- [var hasUncommittedUpdates: Bool](uicollectionview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [func reconfigureItems(at: [IndexPath])](uicollectionview/reconfigureitems(at:).md)
  Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [func reloadData()](uicollectionview/reloaddata.md)
  Reloads all of the data for the collection view.
- [func reloadSections(IndexSet)](uicollectionview/reloadsections(_:).md)
  Reloads the data in the specified sections of the collection view.
- [func reloadItems(at: [IndexPath])](uicollectionview/reloaditems(at:).md)
  Reloads just the items at the specified index paths.
### Identifying collection view elements
- [UICollectionView.ElementCategory](uicollectionview/elementcategory.md)
  Constants specifying the type of view.
- [class let elementKindSectionFooter: String](uicollectionview/elementkindsectionfooter.md)
  A supplementary view that identifies the footer for a given section.
- [class let elementKindSectionHeader: String](uicollectionview/elementkindsectionheader.md)
  A supplementary view that identifies the header for a given section.
### Working with focus
- [var allowsFocus: Bool](uicollectionview/allowsfocus.md)
  A Boolean value that determines whether the collection view allows its cells to become focused.
- [var allowsFocusDuringEditing: Bool](uicollectionview/allowsfocusduringediting.md)
  A Boolean value that determines whether the collection view allows its cells to become focused in edit mode.
- [var selectionFollowsFocus: Bool](uicollectionview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [var remembersLastFocusedIndexPath: Bool](uicollectionview/rememberslastfocusedindexpath.md)
  A Boolean value that indicates whether the collection view automatically assigns the focus to the item at the last focused index path.
### Managing context menus
- [var contextMenuInteraction: UIContextMenuInteraction?](uicollectionview/contextmenuinteraction.md)
  The collection view’s context menu interaction.
### Resizing self-sizing cells
- [var selfSizingInvalidation: UICollectionView.SelfSizingInvalidation](uicollectionview/selfsizinginvalidation-swift.property.md)
  The mode that the collection view uses for invalidating the size of self-sizing cells.
- [UICollectionView.SelfSizingInvalidation](uicollectionview/selfsizinginvalidation-swift.enum.md)
  Constants that describe modes for invalidating the size of self-sizing collection view cells.
### Instance Methods
- [func indexPath(forSupplementaryView: UICollectionReusableView) -> IndexPath?](uicollectionview/indexpath(forsupplementaryview:).md)

## Relationships

### Inherits From
- [UIScrollView](uiscrollview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDataSourceTranslating](uidatasourcetranslating.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UICollectionViewController](uicollectionviewcontroller.md)
  A view controller that specializes in managing a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview)*