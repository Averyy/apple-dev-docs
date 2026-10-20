# IKImageBrowserView

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

A view for displaying and browsing a large collection of images and movies.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Deprecated - Please use NSCollectionView instead

## Declaration

```swift
class IKImageBrowserView
```

```objc
@interface IKImageBrowserView : NSView
```

#### Overview

The [`IKImageBrowserView`](./ikimagebrowserview.md) class is a view for displaying and browsing a large amount of images and movies efficiently. This class will be deprecated in a future release. Please switch to [`NSCollectionView`](../AppKit/nscollectionview.md) instead.

You must set a datasource for the view and implement, at a minimum, the [`numberOfItems(inImageBrowser:)`](../ObjectiveC/nsobject-swift.class/numberofitems%28inimagebrowser%29.md) and [`imageBrowser(_:itemAt:)`](../ObjectiveC/nsobject-swift.class/imagebrowser%28_,itemat%29.md) described in [IKImageBrowserDataSource Protocol](./ikimagebrowserdatasource-protocol.md). The items must conform to the IKImageBrowserItem Protocol protocol.

The class’s delegate object must conform to IKImageBrowserDelegate Protocol protocol. It receives notification of changes in selection, as well as mouse events in the cells.

> **Core Animation Integration**:  The image browser supports either being hosted in a layer-backed view or using custom layers for its own appearance. Custom layers on the image browser are not supported when the image browser is itself backed by a layer.

## Topics

### Updating the Display of the Content
- [func reloadData()](./ikimagebrowserview/reloaddata%28%29.md)
  Marks the receiver as needing its data reloaded.
### Getting and Setting the Delegate
- [var delegate: AnyObject!](./ikimagebrowserview/delegate.md)
  Returns the delegate of the receiver.
### Getting and Setting the Data Source
- [var dataSource: AnyObject!](./ikimagebrowserview/datasource.md)
  Returns the data source of the receiver.
### Setting the Appearance
- [func setCellsStyleMask(Int)](./ikimagebrowserview/setcellsstylemask%28_%29.md)
  Defines the appearance style of the cells.
- [func cellsStyleMask() -> Int](./ikimagebrowserview/cellsstylemask%28%29.md)
  Returns the appearance style mask for the cell.
- [func setConstrainsToOriginalSize(Bool)](./ikimagebrowserview/setconstrainstooriginalsize%28_%29.md)
  Sets whether the receiver constrains the cell’s image to its original size.
- [func constrainsToOriginalSize() -> Bool](./ikimagebrowserview/constrainstooriginalsize%28%29.md)
  Returns whether the receiver constrains the cell’s image to its original size.
- [func setIntercellSpacing(NSSize)](./ikimagebrowserview/setintercellspacing%28_%29.md)
  Sets the spacing between cells in the view.
- [func intercellSpacing() -> NSSize](./ikimagebrowserview/intercellspacing%28%29.md)
  Returns the spacing between cells in the view.
### Creating a Custom Cell for an Item
- [func newCell(forRepresentedItem: Any!) -> IKImageBrowserCell!](./ikimagebrowserview/newcell%28forrepresenteditem%29.md)
  Returns the cell to use for the specified item.
### Zooming and Resizing
- [func setZoomValue(Float)](./ikimagebrowserview/setzoomvalue%28_%29.md)
  Sets the zoom value.
- [func zoomValue() -> Float](./ikimagebrowserview/zoomvalue%28%29.md)
  Returns the current zoom value.
- [func setContentResizingMask(Int)](./ikimagebrowserview/setcontentresizingmask%28_%29.md)
  Determines how the receiver resizes its content when zooming.
- [func contentResizingMask() -> Int](./ikimagebrowserview/contentresizingmask%28%29.md)
  Returns the receiver’s content resizing mask, which determines how its content is resized while zooming.
### Scrolling
- [func scrollIndexToVisible(Int)](./ikimagebrowserview/scrollindextovisible%28_%29.md)
  Scrolls the receiver to the item at the specified index.
### Setting and Getting Cell Size
- [func setCellSize(NSSize)](./ikimagebrowserview/setcellsize%28_%29.md)
  Sets the cell  size.
- [func cellSize() -> NSSize](./ikimagebrowserview/cellsize%28%29.md)
  Returns the cell size.
### Getting Item Information
- [func indexOfItem(at: NSPoint) -> Int](./ikimagebrowserview/indexofitem%28at%29.md)
  Returns the index of the item at the specified location.
- [func itemFrame(at: Int) -> NSRect](./ikimagebrowserview/itemframe%28at%29.md)
  Returns the frame rectangle for the item located at the specified index.
- [func visibleItemIndexes() -> IndexSet!](./ikimagebrowserview/visibleitemindexes%28%29.md)
  Returns the indexes of the view’s currently visible items.
- [func cellForItem(at: Int) -> IKImageBrowserCell!](./ikimagebrowserview/cellforitem%28at%29.md)
  Returns the browser cell for the item at the specified index.
### Reordering and Groups Items
- [func selectionIndexes() -> IndexSet!](./ikimagebrowserview/selectionindexes%28%29.md)
  Returns the indexes of the selected cells.
- [func setSelectionIndexes(IndexSet!, byExtendingSelection: Bool)](./ikimagebrowserview/setselectionindexes%28_,byextendingselection%29.md)
  Selects cells at the specified indexes.
- [func setAllowsMultipleSelection(Bool)](./ikimagebrowserview/setallowsmultipleselection%28_%29.md)
  Controls whether the user can select more than one cell at a time.
- [func allowsMultipleSelection() -> Bool](./ikimagebrowserview/allowsmultipleselection%28%29.md)
  Returns whether multiple selections are allowed.
- [func setAllowsEmptySelection(Bool)](./ikimagebrowserview/setallowsemptyselection%28_%29.md)
  Controls whether an empty selection is allowed.
- [func allowsEmptySelection() -> Bool](./ikimagebrowserview/allowsemptyselection%28%29.md)
  Returns whether an empty selection is allowed.
- [func setAllowsReordering(Bool)](./ikimagebrowserview/setallowsreordering%28_%29.md)
  Controls whether the user can reorder items.
- [func allowsReordering() -> Bool](./ikimagebrowserview/allowsreordering%28%29.md)
  Returns whether the user can reorder items.
- [func setAnimates(Bool)](./ikimagebrowserview/setanimates%28_%29.md)
  Controls whether the receiver animates reordering and changes of the data source.
- [func animates() -> Bool](./ikimagebrowserview/animates%28%29.md)
  Returns whether the receiver animates reordering and changes of the data source.
- [func expandGroup(at: Int)](./ikimagebrowserview/expandgroup%28at%29.md)
  Expands a group at the specified index.
- [func collapseGroup(at: Int)](./ikimagebrowserview/collapsegroup%28at%29.md)
  Collapses a group at the specified index.
- [func isGroupExpanded(at: Int) -> Bool](./ikimagebrowserview/isgroupexpanded%28at%29.md)
  Returns whether the group at the provided index is expanded.
### Supporting Drag and Drop
- [func setDraggingDestinationDelegate(Any!)](./ikimagebrowserview/setdraggingdestinationdelegate%28_%29.md)
  Sets the dragging destination delegate of the receiver.
- [func draggingDestinationDelegate() -> Any!](./ikimagebrowserview/draggingdestinationdelegate%28%29.md)
  Returns the dragging destination delegate of the receiver.
- [func setDrop(Int, dropOperation: IKImageBrowserDropOperation)](./ikimagebrowserview/setdrop%28_,dropoperation%29.md)
  Allows the class to retarget the drop action.
- [func indexAtLocationOfDroppedItem() -> Int](./ikimagebrowserview/indexatlocationofdroppeditem%28%29.md)
  Returns the index of the cell where the drop operation occurred.
- [func setAllowsDroppingOnItems(Bool)](./ikimagebrowserview/setallowsdroppingonitems%28_%29.md)
  Specifies whether the user can drop on items.
- [func allowsDroppingOnItems() -> Bool](./ikimagebrowserview/allowsdroppingonitems%28%29.md)
  Returns whether the user can drop on items.
- [func dropOperation() -> IKImageBrowserDropOperation](./ikimagebrowserview/dropoperation%28%29.md)
  Returns the current drop operation.
### Core Animation Layer Integration
- [func setForegroundLayer(CALayer!)](./ikimagebrowserview/setforegroundlayer%28_%29.md)
  The Core Animation layer used as the foreground overlay.
- [func foregroundLayer() -> CALayer!](./ikimagebrowserview/foregroundlayer%28%29.md)
  Returns the foreground Core Animation layer
- [func setBackgroundLayer(CALayer!)](./ikimagebrowserview/setbackgroundlayer%28_%29.md)
  The Core Animation layer used as the view’s background.
- [func backgroundLayer() -> CALayer!](./ikimagebrowserview/backgroundlayer%28%29.md)
  Returns the foreground Core Animation layer
### QuickLook Support
- [func setCanControlQuickLookPanel(Bool)](./ikimagebrowserview/setcancontrolquicklookpanel%28_%29.md)
  Specifies whether the view can automatically take control of the QuickLook panel.
- [func canControlQuickLookPanel() -> Bool](./ikimagebrowserview/cancontrolquicklookpanel%28%29.md)
  Returns whether the view can automatically take control of the QuickLook panel.
### Getting Columns and Rows Information
- [func numberOfColumns() -> Int](./ikimagebrowserview/numberofcolumns%28%29.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](./ikimagebrowserview/numberofrows%28%29.md)
  Returns the current number of rows.
- [func rect(ofColumn: Int) -> NSRect](./ikimagebrowserview/rect%28ofcolumn%29.md)
  Returns the rectangle containing the specified column.
- [func columnIndexes(in: NSRect) -> IndexSet!](./ikimagebrowserview/columnindexes%28in%29.md)
  Returns the column indexes in the specified rectangle.
- [func rect(ofRow: Int) -> NSRect](./ikimagebrowserview/rect%28ofrow%29.md)
  Returns the rectangle containing the specified row.
- [func rowIndexes(in: NSRect) -> IndexSet!](./ikimagebrowserview/rowindexes%28in%29.md)
  Returns the row indexes in the specified rectangle.
### Constants
- [Cell Appearance Style Masks](./api-1564248-cell-appearance-style-masks.md)
  Masks for the appearance style bit field.
- [Group Style Attributes](./api-1564247-group-style-attributes.md)
  Attributes for the group style. Used by the
- [View Options Keys](./view-options-keys.md)
  Keys for image browser view options. You set and retrieve values for these keys by sending the view `setValue:forKey` and `valueForKey:` messages.
- [Group Keys](./group-keys.md)
  Keys for group attributes.
- [struct IKImageBrowserDropOperation](./ikimagebrowserdropoperation.md)
  These constants specify the locations for dropping items onto the browser view. Used by the method [`setDrop(_:dropOperation:)`](./ikimagebrowserview/setdrop%28_,dropoperation%29.md).

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSDraggingSource](../AppKit/nsdraggingsource.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview)*