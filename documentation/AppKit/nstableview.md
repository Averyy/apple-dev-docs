# NSTableView

**Framework**: AppKit  
**Kind**: class

A set of related records, displayed in rows that represent individual records and columns that represent the attributes of those records.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTableView
```

#### Overview

Table views are displayed in scroll views. Beginning with macOS v10.7, you can use [`NSView`](nsview.md) objects (most commonly customized [`NSTableCellView`](nstablecellview.md) objects) instead of cells for specifying rows and columns. You can still use [`NSCell`](nscell.md) objects for each row and column item if you prefer.

A table view does not store its own data; it retrieves data values as needed from a data source to which it has a weak reference. You should not, therefore, directly set data values programmatically in the table view; instead, modify the values in the data source and allow the changes to be reflected in the table view. To learn about the methods that an `NSTableView` object uses to provide and access the contents of its data source object, see [`NSTableViewDataSource`](nstableviewdatasource.md).

To customize a table view’s behavior without subclassing `NSTableView`, use the methods defined by the `NSTableViewDelegate` protocol. For example, the delegate supports table column management, type-to-select functionality, row selection and editing, custom tracking, and custom views for individual columns and rows. To learn more about the table view delegate, see [`NSTableViewDelegate`](nstableviewdelegate.md).

> ❗ **Important**:  It’s possible that your data source methods for populating the table view may be called before [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) is called if the data source is specified in Interface Builder. You should defend against this by having the data source’s [`numberOfRows(in:)`](nstableviewdatasource/numberofrows(in:).md) method return `0` for the number of rows when the data source has not yet been configured. In [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()), when the data source is initialized you should always call `reloadData` on the table view.

 It’s possible that your data source methods for populating the table view may be called before [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) is called if the data source is specified in Interface Builder. You should defend against this by having the data source’s [`numberOfRows(in:)`](nstableviewdatasource/numberofrows(in:).md) method return `0` for the number of rows when the data source has not yet been configured. In [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()), when the data source is initialized you should always call `reloadData` on the table view.

##### Subclassing

Subclassing `NSTableView` is usually not necessary. Instead, you customize the table view using a delegate object (an object conforming to the [`NSTableViewDelegate`](nstableviewdelegate.md) protocol) and a data source object (conforming to the [`NSTableViewDataSource`](nstableviewdatasource.md) protocol), or by subclassing one of the following subcomponents: cells (when using [`NSCell`](nscell.md)-based table views), the row cell view or the row view (when using [`NSView`](nsview.md)-based table views), the table column class, or table column header classes.

##### Enabling the Table View

Use the [`isEnabled`](nscontrol/isenabled.md) property to enable or disable the table view, which the view inherits from [`NSControl`](nscontrol.md). This property affects the visual appearance of the table view differently depending on whether you use a view- or a cell-based table view. When you change the property’s value for a cell-based table view, the system manages the visual appearance of that table view’s rows, and updates them to a state that reflects the value. Because view-based table views permit complex items in their cells, it’s the developer’s responsibility to update each cell’s appearance as appropriate.

## Topics

### Creating a Table
- [init?(coder: NSCoder)](nstableview/init(coder:).md)
- [init(frame: NSRect)](nstableview/init(frame:).md)
### Managing the Table’s Data
- [var dataSource: (any NSTableViewDataSource)?](nstableview/datasource.md)
  The object that provides the data displayed by the table view.
- [var usesStaticContents: Bool](nstableview/usesstaticcontents.md)
  A Boolean value indicating whether the table uses static data.
- [func reloadData()](nstableview/reloaddata.md)
  Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.
- [func reloadData(forRowIndexes: IndexSet, columnIndexes: IndexSet)](nstableview/reloaddata(forrowindexes:columnindexes:).md)
  Reloads the data for only the specified rows and columns.
### Creating Views to Display
- [func makeView(withIdentifier: NSUserInterfaceItemIdentifier, owner: Any?) -> NSView?](nstableview/makeview(withidentifier:owner:).md)
  Returns a new or existing view with the specified identifier.
- [func rowView(atRow: Int, makeIfNecessary: Bool) -> NSTableRowView?](nstableview/rowview(atrow:makeifnecessary:).md)
  Returns a row view at the specified index, creating one if necessary.
- [func view(atColumn: Int, row: Int, makeIfNecessary: Bool) -> NSView?](nstableview/view(atcolumn:row:makeifnecessary:).md)
  Returns a view at the specified row and column indexes, creating one if necessary.
- [struct NSUserInterfaceItemIdentifier](nsuserinterfaceitemidentifier.md)
### Updating the Table View Arrangement
- [func beginUpdates()](nstableview/beginupdates.md)
  Begins a group of updates for the table view.
- [func endUpdates()](nstableview/endupdates.md)
  Ends the group of updates for the table view.
- [func moveRow(at: Int, to: Int)](nstableview/moverow(at:to:).md)
  Moves the specified row to the new row location using animation.
- [func insertRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/insertrows(at:withanimation:).md)
  Inserts the rows using the specified animation.
- [func removeRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/removerows(at:withanimation:).md)
  Removes the rows using the specified animation.
- [func row(for: NSView) -> Int](nstableview/row(for:).md)
  Returns the index of the row for the specified view.
- [func column(for: NSView) -> Int](nstableview/column(for:).md)
  Returns the column index for the specified view.
### NSView-Based Table Nib File Registration
- [func register(NSNib?, forIdentifier: NSUserInterfaceItemIdentifier)](nstableview/register(_:foridentifier:).md)
  Registers a NIB for the specified identifier, so that view-based table views can use it to instantiate views.
- [var registeredNibsByIdentifier: [NSUserInterfaceItemIdentifier : NSNib]?](nstableview/registerednibsbyidentifier.md)
  The dictionary of all registered nib files for view-based table view identifiers.
### Target-action Behavior
- [var doubleAction: Selector?](nstableview/doubleaction.md)
  The message sent to the table view’s target when the user double-clicks a cell or column header.
- [var clickedColumn: Int](nstableview/clickedcolumn.md)
  The index of the column the user clicked.
- [var clickedRow: Int](nstableview/clickedrow.md)
  The index of the row the user clicked.
### Configuring Behavior
- [var allowsColumnReordering: Bool](nstableview/allowscolumnreordering.md)
  A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.
- [var allowsColumnResizing: Bool](nstableview/allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsMultipleSelection: Bool](nstableview/allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
- [var allowsEmptySelection: Bool](nstableview/allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var allowsColumnSelection: Bool](nstableview/allowscolumnselection.md)
  A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.
- [var usesAutomaticRowHeights: Bool](nstableview/usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.
### Setting Display Attributes
- [var intercellSpacing: NSSize](nstableview/intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var rowHeight: CGFloat](nstableview/rowheight.md)
  The height of each row in the table.
- [var backgroundColor: NSColor](nstableview/backgroundcolor.md)
  The color used to draw the background of the table.
- [var usesAlternatingRowBackgroundColors: Bool](nstableview/usesalternatingrowbackgroundcolors.md)
  A Boolean value indicating whether the table view uses alternating row colors for its background.
- [var style: NSTableView.Style](nstableview/style-swift.property.md)
  The style that the table view uses.
- [var effectiveStyle: NSTableView.Style](nstableview/effectivestyle.md)
  The effective style that the table uses.
- [NSTableView.Style](nstableview/style-swift.enum.md)
  Contains the possible style values for a table view.
- [var selectionHighlightStyle: NSTableView.SelectionHighlightStyle](nstableview/selectionhighlightstyle-swift.property.md)
  The selection highlight style used by the table view to indicate row and column selection.
- [var gridColor: NSColor](nstableview/gridcolor.md)
  The color used to draw grid lines.
- [var gridStyleMask: NSTableView.GridLineStyle](nstableview/gridstylemask.md)
  The grid lines drawn by the table view.
- [func indicatorImage(in: NSTableColumn) -> NSImage?](nstableview/indicatorimage(in:).md)
  Returns the indicator image of the specified table column.
- [func setIndicatorImage(NSImage?, in: NSTableColumn)](nstableview/setindicatorimage(_:in:).md)
  Sets the indicator image of the specified column.
### Getting and Setting Row Size Styles
- [var effectiveRowSizeStyle: NSTableView.RowSizeStyle](nstableview/effectiverowsizestyle.md)
  The effective row size style for the table.
- [var rowSizeStyle: NSTableView.RowSizeStyle](nstableview/rowsizestyle-swift.property.md)
  The row size style (small, medium, large, or custom) used by the table view.
### Column Management
- [func addTableColumn(NSTableColumn)](nstableview/addtablecolumn(_:).md)
  Adds the specified column as the last column of the table view.
- [func removeTableColumn(NSTableColumn)](nstableview/removetablecolumn(_:).md)
  Removes the specified column from the table view.
- [func moveColumn(Int, toColumn: Int)](nstableview/movecolumn(_:tocolumn:).md)
  Moves the column and heading at the specified index to the new specified index.
- [var tableColumns: [NSTableColumn]](nstableview/tablecolumns.md)
  An array containing the current table column objects.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](nstableview/column(withidentifier:).md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](nstableview/tablecolumn(withidentifier:).md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.
### Selecting Columns and Rows
- [func selectColumnIndexes(IndexSet, byExtendingSelection: Bool)](nstableview/selectcolumnindexes(_:byextendingselection:).md)
  Sets the column selection using `indexes` possibly extending the selection.
- [var selectedColumn: Int](nstableview/selectedcolumn.md)
  The index of the last selected column (or the last column added to the selection).
- [var selectedColumnIndexes: IndexSet](nstableview/selectedcolumnindexes.md)
  An index set containing the indexes of the selected columns.
- [func deselectColumn(Int)](nstableview/deselectcolumn(_:).md)
  Deselects the column at the specified index if it’s selected.
- [var numberOfSelectedColumns: Int](nstableview/numberofselectedcolumns.md)
  The number of selected columns.
- [func isColumnSelected(Int) -> Bool](nstableview/iscolumnselected(_:).md)
  Returns a Boolean value that indicates whether the column at the specified index is selected.
- [func selectRowIndexes(IndexSet, byExtendingSelection: Bool)](nstableview/selectrowindexes(_:byextendingselection:).md)
  Sets the row selection using `indexes` extending the selection if specified.
- [var selectedRow: Int](nstableview/selectedrow.md)
  The index of the last selected row (or the last row added to the selection).
- [var selectedRowIndexes: IndexSet](nstableview/selectedrowindexes.md)
  An index set containing the indexes of the selected rows.
- [func deselectRow(Int)](nstableview/deselectrow(_:).md)
  Deselects the row at the specified index if it’s selected.
- [var numberOfSelectedRows: Int](nstableview/numberofselectedrows.md)
  The number of selected rows.
- [func isRowSelected(Int) -> Bool](nstableview/isrowselected(_:).md)
  Returns a Boolean value that indicates whether the row at the specified index is selected.
- [func selectAll(Any?)](nstableview/selectall(_:).md)
  Selects all rows or all columns, according to whether rows or columns were most recently selected.
- [func deselectAll(Any?)](nstableview/deselectall(_:).md)
  Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.
### Enumerating Table Rows
- [func enumerateAvailableRowViews((NSTableRowView, Int) -> Void)](nstableview/enumerateavailablerowviews(_:).md)
  Allows the enumeration of all the table rows that are known to the table view.
### Managing Type Select
- [var allowsTypeSelect: Bool](nstableview/allowstypeselect.md)
  A Boolean value indicating whether the table view allows the user to type characters to select rows.
### Table Dimensions
- [var numberOfColumns: Int](nstableview/numberofcolumns.md)
  The number of columns in the table.
- [var numberOfRows: Int](nstableview/numberofrows.md)
  The number of rows in the table.
### Getting and Setting Floating Rows
- [var floatsGroupRows: Bool](nstableview/floatsgrouprows.md)
  A Boolean value indicating whether the table view draws grouped rows as if they are floating.
### Editing Cells
- [func editColumn(Int, row: Int, with: NSEvent?, select: Bool)](nstableview/editcolumn(_:row:with:select:).md)
  Edits the cell at the specified column and row using the specified event and selection behavior.
- [var editedColumn: Int](nstableview/editedcolumn.md)
  The index of the column being edited.
- [var editedRow: Int](nstableview/editedrow.md)
  The index of the row being edited.
### Adding and Deleting Row Views
- [func didAdd(NSTableRowView, forRow: Int)](nstableview/didadd(_:forrow:).md)
  Invoked when a row view is added to the table.
- [func didRemove(NSTableRowView, forRow: Int)](nstableview/didremove(_:forrow:).md)
  Invoked when a row view is removed from the table.
### Setting Auxiliary Views
- [var headerView: NSTableHeaderView?](nstableview/headerview.md)
  The view object used to draw headers over columns.
- [var cornerView: NSView?](nstableview/cornerview.md)
  The view used to draw the area to the right of the column headers and above the vertical scroller of the enclosing scroll view.
### Layout Support
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nstableview/userinterfacelayoutdirection.md)
  The layout direction of the user interface.
- [func rect(ofColumn: Int) -> NSRect](nstableview/rect(ofcolumn:).md)
  Returns the rectangle containing the column at the specified index.
- [func rect(ofRow: Int) -> NSRect](nstableview/rect(ofrow:).md)
  Returns the rectangle containing the row at the specified index.
- [func rows(in: NSRect) -> NSRange](nstableview/rows(in:).md)
  Returns a range of indexes for the rows that lie wholly or partially within the vertical boundaries of the specified rectangle.
- [func columnIndexes(in: NSRect) -> IndexSet](nstableview/columnindexes(in:).md)
  Returns the indexes of the table view’s columns that intersect the specified rectangle.
- [func column(at: NSPoint) -> Int](nstableview/column(at:).md)
  Returns the index of the column the specified point lies in.
- [func row(at: NSPoint) -> Int](nstableview/row(at:).md)
  Returns the index of the row the specified point lies in.
- [func frameOfCell(atColumn: Int, row: Int) -> NSRect](nstableview/frameofcell(atcolumn:row:).md)
  Returns a rectangle locating the cell that lies at the intersection of the specified column and row.
- [var columnAutoresizingStyle: NSTableView.ColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.property.md)
  The table view’s column autoresizing style.
- [func sizeLastColumnToFit()](nstableview/sizelastcolumntofit.md)
  Resizes the last column so the table view fits exactly within its enclosing clip view.
- [func noteNumberOfRowsChanged()](nstableview/notenumberofrowschanged.md)
  Informs the table view that the number of records in its data source has changed.
- [func tile()](nstableview/tile.md)
  Properly sizes the table view and its header view and marks it as needing display.
- [func sizeToFit()](nstableview/sizetofit.md)
  Sizes the  table view based on a uniform column autoresizing style.
- [func noteHeightOfRows(withIndexesChanged: IndexSet)](nstableview/noteheightofrows(withindexeschanged:).md)
  Informs the table view that the rows specified in `indexSet` have changed height.
### Drawing
- [func drawRow(Int, clipRect: NSRect)](nstableview/drawrow(_:cliprect:).md)
  Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.
- [func drawGrid(inClipRect: NSRect)](nstableview/drawgrid(incliprect:).md)
  Draws the grid lines within the supplied rectangle.
- [func highlightSelection(inClipRect: NSRect)](nstableview/highlightselection(incliprect:).md)
  Highlights the region of the table view in the specified rectangle.
- [func drawBackground(inClipRect: NSRect)](nstableview/drawbackground(incliprect:).md)
  Draws the background of the table view in the clip rect specified by the rectangle.
### Scrolling
- [func scrollRowToVisible(Int)](nstableview/scrollrowtovisible(_:).md)
  Scrolls the view so the specified row is visible.
- [func scrollColumnToVisible(Int)](nstableview/scrollcolumntovisible(_:).md)
  Scrolls the view so the specified column is visible.
### Table Column State Persistence
- [var autosaveTableColumns: Bool](nstableview/autosavetablecolumns.md)
  A Boolean value indicating whether the order and width of the table view’s columns are automatically saved.
- [var autosaveName: NSTableView.AutosaveName?](nstableview/autosavename-swift.property.md)
  The name under which table information is automatically saved.
- [NSTableView.AutosaveName](nstableview/autosavename-swift.typealias.md)
### Accessing the Delegate
- [var delegate: (any NSTableViewDelegate)?](nstableview/delegate.md)
  The table view’s delegate.
### Highlightable Column Headers
- [var highlightedTableColumn: NSTableColumn?](nstableview/highlightedtablecolumn.md)
  The column highlighted in the table.
### Dragging
- [func dragImageForRows(with: IndexSet, tableColumns: [NSTableColumn], event: NSEvent, offset: NSPointPointer) -> NSImage](nstableview/dragimageforrows(with:tablecolumns:event:offset:).md)
  Computes and returns an image to use for dragging.
- [func canDragRows(with: IndexSet, at: NSPoint) -> Bool](nstableview/candragrows(with:at:).md)
  Returns a Boolean value indicating whether the table view allows dragging the rows with the drag initiated at the specified point.
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nstableview/setdraggingsourceoperationmask(_:forlocal:).md)
  Sets the default operation mask returned by `draggingSourceOperationMaskForLocal:` to `mask`.
- [var verticalMotionCanBeginDrag: Bool](nstableview/verticalmotioncanbegindrag.md)
  A Boolean value indicating whether vertical motion is treated as a drag or selection change.
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.property.md)
  The feedback style displayed when the user drags over the table view.
- [func setDropRow(Int, dropOperation: NSTableView.DropOperation)](nstableview/setdroprow(_:dropoperation:).md)
  Retargets the proposed drop operation.
### Sorting
- [var sortDescriptors: [NSSortDescriptor]](nstableview/sortdescriptors.md)
  The table view’s sort descriptors.
### Row Actions
- [var rowActionsVisible: Bool](nstableview/rowactionsvisible.md)
  A Boolean value indicating whether a table row’s actions are visible.
### Hiding and Showing Table Rows
- [func hideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/hiderows(at:withanimation:).md)
  Hides the specified table rows.
- [func unhideRows(at: IndexSet, withAnimation: NSTableView.AnimationOptions)](nstableview/unhiderows(at:withanimation:).md)
  Unhides the specified table rows.
- [var hiddenRowIndexes: IndexSet](nstableview/hiddenrowindexes.md)
  The indexes of all hidden table rows.
### Deprecated Methods
- [func focusedColumn() -> Int](nstableview/focusedcolumn.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](nstableview/setfocusedcolumn(_:).md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](nstableview/shouldfocuscell(_:atcolumn:row:).md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](nstableview/performclickoncell(atcolumn:row:).md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](nstableview/preparedcell(atcolumn:row:).md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.
### Constants
- [Specifying a Custom Row View in a Nib File](specifying-a-custom-row-view-in-a-nib-file.md)
  View-based table view instances use `NSTableViewRowKey` to identify the nib file containing the template row view. You can specify a custom row view (without any code) by associating this key with the appropriate nib name in Interface Builder.
- [NSTableView.DraggingDestinationFeedbackStyle](nstableview/draggingdestinationfeedbackstyle-swift.enum.md)
  These constants specify the drag styles displayed by the table view. They’re used by [`draggingDestinationFeedbackStyle`](nstableview/draggingdestinationfeedbackstyle-swift.property.md).
- [NSTableView.DropOperation](nstableview/dropoperation.md)
  `NSTableView` defines these constants to specify drop operations.
- [NSTableView.GridLineStyle](nstableview/gridlinestyle.md)
  `NSTableView` defines these constants to specify grid styles. These constants are used by the [`gridStyleMask`](nstableview/gridstylemask.md) property. The mask can be either [`NSTableViewGridNone`](nstableviewgridlinestyle/nstableviewgridnone.md) or it can contain either or both of the other options combined using the C bitwise `OR` operator.
- [NSTableView.ColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum.md)
  The following constants specify the autoresizing styles. These constants are used by the  [`columnAutoresizingStyle`](nstableview/columnautoresizingstyle-swift.property.md) property.
- [NSTableView.SelectionHighlightStyle](nstableview/selectionhighlightstyle-swift.enum.md)
  The following constants specify the selection highlight styles. These constants are used by the [`selectionHighlightStyle`](nstableview/selectionhighlightstyle-swift.property.md) property.
- [NSTableView.AnimationOptions](nstableview/animationoptions.md)
  Specifies the animation effects to apply when inserting or removing rows.
- [NSTableView.RowSizeStyle](nstableview/rowsizestyle-swift.enum.md)
  The row size style constants define the size of the rows in the table view. They are used by the [`effectiveRowSizeStyle`](nstableview/effectiverowsizestyle.md) and [`rowSizeStyle`](nstableview/rowsizestyle-swift.property.md) properties. You can also query the row size in the [`NSTableCellView`](nstablecellview.md) class’ property [`rowSizeStyle`](nstablecellview/rowsizestyle.md).
- [NSTableView.RowActionEdge](nstableview/rowactionedge.md)
  These constants define table row edges on which row actions are attached. They are used by the `tableView:rowActionsForRow:edge:` delegate method.
### Notifications
- [class let columnDidMoveNotification: NSNotification.Name](nstableview/columndidmovenotification.md)
  Posted whenever a column is moved by user action in an `NSTableView` object.
- [class let columnDidResizeNotification: NSNotification.Name](nstableview/columndidresizenotification.md)
  Posted whenever a column is resized in an `NSTableView` object.
- [class let selectionDidChangeNotification: NSNotification.Name](nstableview/selectiondidchangenotification.md)
  Posted after an `NSTableView` object’s selection changes.
- [class let selectionIsChangingNotification: NSNotification.Name](nstableview/selectionischangingnotification.md)
  Posted as an `NSTableView` object’s selection changes (while the mouse button is still down).

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
### Inherited By
- [NSOutlineView](nsoutlineview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityTable](nsaccessibilitytable.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSDraggingSource](nsdraggingsource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTextDelegate](nstextdelegate.md)
- [NSTextViewDelegate](nstextviewdelegate.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)
- [class NSTableCellView](nstablecellview.md)
  A reusable container view shown for a particular cell in a table view that uses rows for content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview)*