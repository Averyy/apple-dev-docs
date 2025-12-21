# NSBrowser

**Framework**: AppKit  
**Kind**: class

An interface that displays a hierarchically organized list of data items that can be navigated and selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSBrowser
```

#### Overview

A browser displays information using a set of columns, which are indexed from left to right. Each successive column displays the next level down in the data hierarchy. This class uses the [`NSBrowserCell`](nsbrowsercell.md) class to implement its user interface.

Browsers have the following components:

- Columns
- Scroll views
- Matrices
- Browser cells

To the user, browsers display data in columns and rows within each column. These components are arranged in the following component hierarchy:

```objc
Browser
|---Columns [1..*]
    |---Scroll view
       |---Matrix
           |---Rows [0..*]
```

##### Superclass Overrides

- [`isOpaque`](nsview/isopaque.md) returns [`true`](https://developer.apple.com/documentation/Swift/true) when the browser doesn’t have a title and its background color’s alpha component is `1.0`; otherwise, it returns [`false`](https://developer.apple.com/documentation/Swift/false).

##### Protocol Implementations

- The [`NSBrowser`](nsbrowser.md) implementation of [`namesOfPromisedFilesDropped(atDestination:)`](nsdragginginfo/namesofpromisedfilesdropped(atdestination:).md) provides the names of the files that the browser promises to create at a specified location, the result of sending `browser:namesOfPromisedFilesDroppedAtDestination:forDraggedRowsWithIndexes:inColumn:` to the delegate.

## Topics

### Configuring Browsers
- [var reusesColumns: Bool](nsbrowser/reusescolumns.md)
  A Boolean that indicates whether the browser reuses matrix objects after their columns are unloaded.
- [var maxVisibleColumns: Int](nsbrowser/maxvisiblecolumns.md)
  The maximum number of visible columns.
- [var autohidesScroller: Bool](nsbrowser/autohidesscroller.md)
  A Boolean that indicates whether the browser automatically hides its scroller.
- [var backgroundColor: NSColor](nsbrowser/backgroundcolor.md)
  The browser’s background color.
- [var minColumnWidth: CGFloat](nsbrowser/mincolumnwidth.md)
  The minimum column width, in pixels.
- [var separatesColumns: Bool](nsbrowser/separatescolumns.md)
  A Boolean that indicates whether columns are separated by bezeled borders.
- [var takesTitleFromPreviousColumn: Bool](nsbrowser/takestitlefrompreviouscolumn.md)
  A Boolean that indicates whether a column takes its title from the selected cell in the previous column.
- [func tile()](nsbrowser/tile.md)
  Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.
- [var delegate: (any NSBrowserDelegate)?](nsbrowser/delegate.md)
  The browser’s delegate.
### Managing Component Types
- [class var cellClass: AnyClass](nsbrowser/cellclass.md)
  Returns the `NSBrowserCell` class.
- [func setCellClass(AnyClass)](nsbrowser/setcellclass(_:).md)
  Sets the class of the cell to be used by the matrices in the columns of the browser.
- [var cellPrototype: Any!](nsbrowser/cellprototype.md)
  The prototype `NSCell` for displaying items in the matrices in the columns of the browser.
### Managing Selection Behavior
- [var allowsBranchSelection: Bool](nsbrowser/allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](nsbrowser/allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](nsbrowser/allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectedRowIndexes(inColumn: Int) -> IndexSet?](nsbrowser/selectedrowindexes(incolumn:).md)
  Provides the indexes of the selected rows in a given column of the browser.
- [func selectRowIndexes(IndexSet, inColumn: Int)](nsbrowser/selectrowindexes(_:incolumn:).md)
  Specifies the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](nsbrowser/allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).
### Managing Selection
- [func selectedCell(inColumn: Int) -> Any?](nsbrowser/selectedcell(incolumn:).md)
  Returns the last (lowest) cell selected in the given column.
- [var selectedCells: [NSCell]?](nsbrowser/selectedcells.md)
  All cells selected in the rightmost column.
- [func selectAll(Any?)](nsbrowser/selectall(_:).md)
  Selects all cells in the last column of the browser.
- [func selectedRow(inColumn: Int) -> Int](nsbrowser/selectedrow(incolumn:).md)
  Returns the row index of the selected cell in the specified column.
- [func selectRow(Int, inColumn: Int)](nsbrowser/selectrow(_:incolumn:).md)
  Selects the cell at the specified row and column index.
- [var selectionIndexPath: IndexPath?](nsbrowser/selectionindexpath.md)
  The index path of the item selected in the browser.
- [var selectionIndexPaths: [IndexPath]](nsbrowser/selectionindexpaths.md)
  An array containing the index paths of all items selected in the browser.
### Accessing Components
- [func loadedCell(atRow: Int, column: Int) -> Any?](nsbrowser/loadedcell(atrow:column:).md)
  Loads, if necessary, and returns the cell at the specified row and column location.
- [func editItem(at: IndexPath, with: NSEvent?, select: Bool)](nsbrowser/edititem(at:with:select:).md)
  Begins editing the item at the specified path.
- [func item(at: IndexPath) -> Any?](nsbrowser/item(at:).md)
  Returns the item at the specified index path.
- [func item(atRow: Int, inColumn: Int) -> Any?](nsbrowser/item(atrow:incolumn:).md)
  Returns the item located at the specified row and column.
- [func indexPath(forColumn: Int) -> IndexPath](nsbrowser/indexpath(forcolumn:).md)
  Returns the index path of the item whose children are displayed in the given column.
- [func isLeafItem(Any?) -> Bool](nsbrowser/isleafitem(_:).md)
  Returns whether the specified item is a leaf item.
- [func parentForItems(inColumn: Int) -> Any?](nsbrowser/parentforitems(incolumn:).md)
  Returns the item that contains the children located in the specified column.
### Managing the Path
- [func path() -> String](nsbrowser/path.md)
  Returns a string representing the browser’s current path.
- [func setPath(String) -> Bool](nsbrowser/setpath(_:).md)
  Sets the path to be displayed by the browser.
- [func path(toColumn: Int) -> String](nsbrowser/path(tocolumn:).md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.
- [var pathSeparator: String](nsbrowser/pathseparator.md)
  The path separator.
### Managing Columns
- [func addColumn()](nsbrowser/addcolumn.md)
  Adds a column to the right of the last column.
- [var selectedColumn: Int](nsbrowser/selectedcolumn.md)
  The index of the last column with a selected item.
- [var lastColumn: Int](nsbrowser/lastcolumn.md)
  The index of the last column loaded.
- [var firstVisibleColumn: Int](nsbrowser/firstvisiblecolumn.md)
  The index of the first visible column.
- [var numberOfVisibleColumns: Int](nsbrowser/numberofvisiblecolumns.md)
  The number of visible columns.
- [var lastVisibleColumn: Int](nsbrowser/lastvisiblecolumn.md)
  The index of the last visible column.
- [func validateVisibleColumns()](nsbrowser/validatevisiblecolumns.md)
  Validates the browser’s visible columns.
- [var isLoaded: Bool](nsbrowser/isloaded.md)
  A Boolean that indicates whether column 0 is loaded.
- [func loadColumnZero()](nsbrowser/loadcolumnzero.md)
  Loads column 0; unloads previously loaded columns.
- [func reloadColumn(Int)](nsbrowser/reloadcolumn(_:).md)
  Reloads the given column.
### Accessing Column Titles
- [func title(ofColumn: Int) -> String?](nsbrowser/title(ofcolumn:).md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](nsbrowser/settitle(_:ofcolumn:).md)
  Sets the title of the given column.
- [var isTitled: Bool](nsbrowser/istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](nsbrowser/drawtitle(ofcolumn:in:).md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](nsbrowser/titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](nsbrowser/titleframe(ofcolumn:).md)
  Returns the bounds of the title frame for the specified column.
### Updating Browsers
- [func noteHeightOfRowsWithIndexesChanged(IndexSet, inColumn: Int)](nsbrowser/noteheightofrowswithindexeschanged(_:incolumn:).md)
  Immediately retiles the browser’s columns using row heights specified by the browser’s delegate.
- [func reloadData(forRowIndexes: IndexSet, inColumn: Int)](nsbrowser/reloaddata(forrowindexes:incolumn:).md)
  Updates the rows in the column with the specified column index with indexes in the specified set.
### Scrolling
- [var hasHorizontalScroller: Bool](nsbrowser/hashorizontalscroller.md)
  A Boolean that indicates whether the browser has a horizontal scroller.
- [func scrollColumnToVisible(Int)](nsbrowser/scrollcolumntovisible(_:).md)
  Scrolls to make the specified column visible.
- [func scrollColumnsLeft(by: Int)](nsbrowser/scrollcolumnsleft(by:).md)
  Scrolls columns left by the specified number of columns.
- [func scrollColumnsRight(by: Int)](nsbrowser/scrollcolumnsright(by:).md)
  Scrolls columns right by the specified number of columns.
- [func scrollRowToVisible(Int, inColumn: Int)](nsbrowser/scrollrowtovisible(_:incolumn:).md)
  Scrolls the specified row to be visible within the specified column.
### Dragging
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](nsbrowser/setdraggingsourceoperationmask(_:forlocal:).md)
  Specifies the drag-operation mask for dragging operations with local or external destinations.
- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](nsbrowser/candragrows(with:incolumn:with:).md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.
- [func draggingImageForRows(with: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer?) -> NSImage?](nsbrowser/draggingimageforrows(with:incolumn:with:offset:).md)
  Provides an image to represent dragged rows during a drag operation on the browser.
### Getting Column Frames
- [func frame(ofColumn: Int) -> NSRect](nsbrowser/frame(ofcolumn:).md)
  Returns the rectangle containing the given column.
- [func frame(ofInsideOfColumn: Int) -> NSRect](nsbrowser/frame(ofinsideofcolumn:).md)
  Returns the rectangle containing the specified column, not including borders.
### Getting Row Frames
- [func frame(ofRow: Int, inColumn: Int) -> NSRect](nsbrowser/frame(ofrow:incolumn:).md)
  Returns the frame of the cell at the specified location, including the expandable arrow.
- [func getRow(UnsafeMutablePointer<Int>?, column: UnsafeMutablePointer<Int>?, for: NSPoint) -> Bool](nsbrowser/getrow(_:column:for:).md)
  Gets the row and column coordinates for the specified point, if a cell exists at that point.
### Managing Actions
- [var doubleAction: Selector?](nsbrowser/doubleaction.md)
  The browser’s double-click action method.
- [var sendsActionOnArrowKeys: Bool](nsbrowser/sendsactiononarrowkeys.md)
  A Boolean that indicates whether pressing an arrow key causes an action message to be sent.
- [func sendAction() -> Bool](nsbrowser/sendaction.md)
  Sends the action message to the target.
### Handling Mouse-Click Events
- [func doClick(Any?)](nsbrowser/doclick(_:).md)
  Responds to (single) mouse clicks in a column of the browser.
- [func doDoubleClick(Any?)](nsbrowser/dodoubleclick(_:).md)
  Responds to double clicks in a column of the browser.
- [var clickedColumn: Int](nsbrowser/clickedcolumn.md)
  The column number of the cell that the user clicked to display a context menu.
- [var clickedRow: Int](nsbrowser/clickedrow.md)
  The row number of the cell that the user clicked to display a context menu.
### Sizing
- [class func removeSavedColumns(withAutosaveName: NSBrowser.ColumnsAutosaveName)](nsbrowser/removesavedcolumns(withautosavename:).md)
  Removes the column configuration data stored under the given name from the application’s user defaults.
- [var columnsAutosaveName: NSBrowser.ColumnsAutosaveName](nsbrowser/columnsautosavename-swift.property.md)
  The name used to automatically save the browser’s column configuration.
- [NSBrowser.ColumnsAutosaveName](nsbrowser/columnsautosavename-swift.typealias.md)
- [func columnContentWidth(forColumnWidth: CGFloat) -> CGFloat](nsbrowser/columncontentwidth(forcolumnwidth:).md)
  Returns the content width for a given column width.
- [func columnWidth(forColumnContentWidth: CGFloat) -> CGFloat](nsbrowser/columnwidth(forcolumncontentwidth:).md)
  Returns the column width for the width of the given column’s content.
- [var columnResizingType: NSBrowser.ColumnResizingType](nsbrowser/columnresizingtype-swift.property.md)
  A constant indicating the browser’s column resizing type.
- [var prefersAllColumnUserResizing: Bool](nsbrowser/prefersallcolumnuserresizing.md)
  A Boolean that indicates whether the browser is set to resize all columns simultaneously rather than resizing a single column at a time.
- [func width(ofColumn: Int) -> CGFloat](nsbrowser/width(ofcolumn:).md)
  Returns the width of the specified column.
- [func setWidth(CGFloat, ofColumn: Int)](nsbrowser/setwidth(_:ofcolumn:).md)
  Sets the width of the specified column.
- [func defaultColumnWidth() -> CGFloat](nsbrowser/defaultcolumnwidth.md)
  Returns the default column width of the browser’s columns.
- [func setDefaultColumnWidth(CGFloat)](nsbrowser/setdefaultcolumnwidth(_:).md)
  Sets the default column width for new browser columns that do not otherwise have an initial width from defaults or the browser’s delegate.
- [var rowHeight: CGFloat](nsbrowser/rowheight.md)
  The height of the browser’s rows.
### Constants
- [NSBrowser.ColumnResizingType](nsbrowser/columnresizingtype-swift.enum.md)
  Types of browser column resizing.
- [NSBrowser.DropOperation](nsbrowser/dropoperation.md)
  The type used to specify the drop type of a drag-and-drop operation. See [`browser(_:validateDrop:proposedRow:column:dropOperation:)`](nsbrowserdelegate/browser(_:validatedrop:proposedrow:column:dropoperation:).md) for more information.
- [Application Kit Versions for NSBrowser Functionality](application-kit-versions-for-nsbrowser-functionality.md)
  The version of the AppKit.framework containing a specific bug fix or capability.
### Notifications
- [class let columnConfigurationDidChangeNotification: NSNotification.Name](nsbrowser/columnconfigurationdidchangenotification.md)
  Notifies the delegate when the width of a browser column has changed.
### Deprecated
- [func column(of: NSMatrix) -> Int](nsbrowser/column(of:).md)
  Returns the column number in which the given matrix is located.
- [func matrix(inColumn: Int) -> NSMatrix?](nsbrowser/matrix(incolumn:).md)
  Returns the matrix located in the specified column.
- [func matrixClass() -> AnyClass](nsbrowser/matrixclass.md)
  Returns the matrix class used in the browser’s columns.
- [func setMatrixClass(AnyClass)](nsbrowser/setmatrixclass(_:).md)
  Sets the matrix class to be used in the browser’s columns.
### Instance Methods
- [func selectedCell() -> Any?](nsbrowser/selectedcell.md)

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser)*