# IKImageBrowserView

**Framework**: Quartz  
**Kind**: class

A view for displaying and browsing a large collection of images and movies.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class IKImageBrowserView
```

#### Overview

The [`IKImageBrowserView`](ikimagebrowserview.md) class is a view for displaying and browsing a large amount of images and movies efficiently. This class will be deprecated in a future release. Please switch to [`NSCollectionView`](https://developer.apple.com/documentation/AppKit/NSCollectionView) instead.

You must set a datasource for the view and implement, at a minimum, the [`numberOfItems(inImageBrowser:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/numberOfItems(inImageBrowser:)) and [`imageBrowser(_:itemAt:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/imageBrowser(_:itemAt:)) described in [`IKImageBrowserDataSource Protocol`](ikimagebrowserdatasource-protocol.md). The items must conform to the IKImageBrowserItem Protocol protocol.

The class’s delegate object must conform to IKImageBrowserDelegate Protocol protocol. It receives notification of changes in selection, as well as mouse events in the cells.

> **Note**:  The image browser supports either being hosted in a layer-backed view or using custom layers for its own appearance. Custom layers on the image browser are not supported when the image browser is itself backed by a layer.

## Topics

### Updating the Display of the Content
- [func reloadData()](ikimagebrowserview/reloaddata.md)
  Marks the receiver as needing its data reloaded.
### Getting and Setting the Delegate
- [var delegate: AnyObject!](ikimagebrowserview/delegate.md)
  Returns the delegate of the receiver.
### Getting and Setting the Data Source
- [var dataSource: AnyObject!](ikimagebrowserview/datasource.md)
  Returns the data source of the receiver.
### Setting the Appearance
- [func setCellsStyleMask(Int)](ikimagebrowserview/setcellsstylemask(_:).md)
  Defines the appearance style of the cells.
- [func cellsStyleMask() -> Int](ikimagebrowserview/cellsstylemask.md)
  Returns the appearance style mask for the cell.
- [func setConstrainsToOriginalSize(Bool)](ikimagebrowserview/setconstrainstooriginalsize(_:).md)
  Sets whether the receiver constrains the cell’s image to its original size.
- [func constrainsToOriginalSize() -> Bool](ikimagebrowserview/constrainstooriginalsize.md)
  Returns whether the receiver constrains the cell’s image to its original size.
- [func setIntercellSpacing(NSSize)](ikimagebrowserview/setintercellspacing(_:).md)
  Sets the spacing between cells in the view.
- [func intercellSpacing() -> NSSize](ikimagebrowserview/intercellspacing.md)
  Returns the spacing between cells in the view.
### Creating a Custom Cell for an Item
- [func newCell(forRepresentedItem: Any!) -> IKImageBrowserCell!](ikimagebrowserview/newcell(forrepresenteditem:).md)
  Returns the cell to use for the specified item.
### Zooming and Resizing
- [func setZoomValue(Float)](ikimagebrowserview/setzoomvalue(_:).md)
  Sets the zoom value.
- [func zoomValue() -> Float](ikimagebrowserview/zoomvalue.md)
  Returns the current zoom value.
- [func setContentResizingMask(Int)](ikimagebrowserview/setcontentresizingmask(_:).md)
  Determines how the receiver resizes its content when zooming.
- [func contentResizingMask() -> Int](ikimagebrowserview/contentresizingmask.md)
  Returns the receiver’s content resizing mask, which determines how its content is resized while zooming.
### Scrolling
- [func scrollIndexToVisible(Int)](ikimagebrowserview/scrollindextovisible(_:).md)
  Scrolls the receiver to the item at the specified index.
### Setting and Getting Cell Size
- [func setCellSize(NSSize)](ikimagebrowserview/setcellsize(_:).md)
  Sets the cell  size.
- [func cellSize() -> NSSize](ikimagebrowserview/cellsize.md)
  Returns the cell size.
### Getting Item Information
- [func indexOfItem(at: NSPoint) -> Int](ikimagebrowserview/indexofitem(at:).md)
  Returns the index of the item at the specified location.
- [func itemFrame(at: Int) -> NSRect](ikimagebrowserview/itemframe(at:).md)
  Returns the frame rectangle for the item located at the specified index.
- [func visibleItemIndexes() -> IndexSet!](ikimagebrowserview/visibleitemindexes.md)
  Returns the indexes of the view’s currently visible items.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](ikimagebrowserview/cellforitem(at:).md)
  Returns the browser cell for the item at the specified index.
### Reordering and Groups Items
- [func selectionIndexes() -> IndexSet!](ikimagebrowserview/selectionindexes.md)
  Returns the indexes of the selected cells.
- [func setSelectionIndexes(IndexSet!, byExtendingSelection: Bool)](ikimagebrowserview/setselectionindexes(_:byextendingselection:).md)
  Selects cells at the specified indexes.
- [func setAllowsMultipleSelection(Bool)](ikimagebrowserview/setallowsmultipleselection(_:).md)
  Controls whether the user can select more than one cell at a time.
- [func allowsMultipleSelection() -> Bool](ikimagebrowserview/allowsmultipleselection.md)
  Returns whether multiple selections are allowed.
- [func setAllowsEmptySelection(Bool)](ikimagebrowserview/setallowsemptyselection(_:).md)
  Controls whether an empty selection is allowed.
- [func allowsEmptySelection() -> Bool](ikimagebrowserview/allowsemptyselection.md)
  Returns whether an empty selection is allowed.
- [func setAllowsReordering(Bool)](ikimagebrowserview/setallowsreordering(_:).md)
  Controls whether the user can reorder items.
- [func allowsReordering() -> Bool](ikimagebrowserview/allowsreordering.md)
  Returns whether the user can reorder items.
- [func setAnimates(Bool)](ikimagebrowserview/setanimates(_:).md)
  Controls whether the receiver animates reordering and changes of the data source.
- [func animates() -> Bool](ikimagebrowserview/animates.md)
  Returns whether the receiver animates reordering and changes of the data source.
- [func expandGroup(at: Int)](ikimagebrowserview/expandgroup(at:).md)
  Expands a group at the specified index.
- [func collapseGroup(at: Int)](ikimagebrowserview/collapsegroup(at:).md)
  Collapses a group at the specified index.
- [func isGroupExpanded(at: Int) -> Bool](ikimagebrowserview/isgroupexpanded(at:).md)
  Returns whether the group at the provided index is expanded.
### Supporting Drag and Drop
- [func setDraggingDestinationDelegate(Any!)](ikimagebrowserview/setdraggingdestinationdelegate(_:).md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](ikimagebrowserview/draggingdestinationdelegate.md)
  Returns the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](ikimagebrowserview/setdrop(_:dropoperation:).md)
  Allows the class to retarget the drop action.
- [func indexAtLocationOfDroppedItem() -> Int](ikimagebrowserview/indexatlocationofdroppeditem.md)
  Returns the index of the cell where the drop operation occurred.
- [func setAllowsDroppingOnItems(Bool)](ikimagebrowserview/setallowsdroppingonitems(_:).md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](ikimagebrowserview/allowsdroppingonitems.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](ikimagebrowserview/dropoperation.md)
  Returns the current drop operation.
### Core Animation Layer Integration
- [func setForegroundLayer(CALayer!)](ikimagebrowserview/setforegroundlayer(_:).md)
  The Core Animation layer used as the foreground overlay.
- [func foregroundLayer() -> CALayer!](ikimagebrowserview/foregroundlayer.md)
  Returns the foreground Core Animation layer
- [func setBackgroundLayer(CALayer!)](ikimagebrowserview/setbackgroundlayer(_:).md)
  The Core Animation layer used as the view’s background.
- [func backgroundLayer() -> CALayer!](ikimagebrowserview/backgroundlayer.md)
  Returns the foreground Core Animation layer
### QuickLook Support
- [func setCanControlQuickLookPanel(Bool)](ikimagebrowserview/setcancontrolquicklookpanel(_:).md)
  Specifies whether the view can automatically take control of the QuickLook panel.
- [func canControlQuickLookPanel() -> Bool](ikimagebrowserview/cancontrolquicklookpanel.md)
  Returns whether the view can automatically take control of the QuickLook panel.
### Getting Columns and Rows Information
- [func numberOfColumns() -> Int](ikimagebrowserview/numberofcolumns.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](ikimagebrowserview/numberofrows.md)
  Returns the current number of rows.
- [func rect(ofColumn: Int) -> NSRect](ikimagebrowserview/rect(ofcolumn:).md)
  Returns the rectangle containing the specified column.
- [func columnIndexes(in: NSRect) -> IndexSet!](ikimagebrowserview/columnindexes(in:).md)
  Returns the column indexes in the specified rectangle.
- [func rect(ofRow: Int) -> NSRect](ikimagebrowserview/rect(ofrow:).md)
  Returns the rectangle containing the specified row.
- [func rowIndexes(in: NSRect) -> IndexSet!](ikimagebrowserview/rowindexes(in:).md)
  Returns the row indexes in the specified rectangle.
### Constants
- [Cell Appearance Style Masks](1564248-cell-appearance-style-masks.md)
  Masks for the appearance style bit field.
- [Group Style Attributes](1564247-group-style-attributes.md)
  Attributes for the group style. Used by the
- [View Options Keys](view-options-keys.md)
  Keys for image browser view options. You set and retrieve values for these keys by sending the view `setValue:forKey` and `valueForKey:` messages.
- [Group Keys](group-keys.md)
  Keys for group attributes.
- [struct IKImageBrowserDropOperation](ikimagebrowserdropoperation.md)
  These constants specify the locations for dropping items onto the browser view. Used by the method [`setDrop(_:dropOperation:)`](ikimagebrowserview/setdrop(_:dropoperation:).md).

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSDraggingSource](../AppKit/NSDraggingSource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Quartz/ikimagebrowserview)*