# NSBrowser

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An interface that displays a hierarchically organized list of data items that can be navigated and selected.

**Availability**:
- macOS

## Declaration

```swift
class NSBrowser
```

```objc
@interface NSBrowser : NSControl
```

#### Overview

A browser displays information using a set of columns, which are indexed from left to right. Each successive column displays the next level down in the data hierarchy. This class uses the [`NSBrowserCell`](./nsbrowsercell.md) class to implement its user interface.

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

##### Superclass overrides

- [`isOpaque`](./nsview/isopaque.md) returns [`true`](../Swift/true.md) when the browser doesn’t have a title and its background color’s alpha component is `1.0`; otherwise, it returns [`false`](../Swift/false.md).

##### Protocol implementations

- The [`NSBrowser`](./nsbrowser.md) implementation of [`namesOfPromisedFilesDropped(atDestination:)`](./nsdragginginfo/namesofpromisedfilesdropped%28atdestination%29.md) provides the names of the files that the browser promises to create at a specified location, the result of sending `browser:namesOfPromisedFilesDroppedAtDestination:forDraggedRowsWithIndexes:inColumn:` to the delegate.

## Topics

### Configuring Browsers
- [var reusesColumns: Bool](./nsbrowser/reusescolumns.md)
  A Boolean that indicates whether the browser reuses matrix objects after their columns are unloaded.
- [var maxVisibleColumns: Int](./nsbrowser/maxvisiblecolumns.md)
  The maximum number of visible columns.
- [var autohidesScroller: Bool](./nsbrowser/autohidesscroller.md)
  A Boolean that indicates whether the browser automatically hides its scroller.
- [var backgroundColor: NSColor](./nsbrowser/backgroundcolor.md)
  The browser’s background color.
- [var minColumnWidth: CGFloat](./nsbrowser/mincolumnwidth.md)
  The minimum column width, in pixels.
- [var separatesColumns: Bool](./nsbrowser/separatescolumns.md)
  A Boolean that indicates whether columns are separated by bezeled borders.
- [var takesTitleFromPreviousColumn: Bool](./nsbrowser/takestitlefrompreviouscolumn.md)
  A Boolean that indicates whether a column takes its title from the selected cell in the previous column.
- [func tile()](./nsbrowser/tile%28%29.md)
  Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.
- [var delegate: (any NSBrowserDelegate)?](./nsbrowser/delegate.md)
  The browser’s delegate.
### Managing Component Types
- [class var cellClass: AnyClass](./nsbrowser/cellclass.md)
  Returns the `NSBrowserCell` class.
- [func setCellClass(AnyClass)](./nsbrowser/setcellclass%28_%29.md)
  Sets the class of the cell to be used by the matrices in the columns of the browser.
- [var cellPrototype: Any!](./nsbrowser/cellprototype.md)
  The prototype `NSCell` for displaying items in the matrices in the columns of the browser.
### Managing Selection Behavior
- [var allowsBranchSelection: Bool](./nsbrowser/allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](./nsbrowser/allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](./nsbrowser/allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectedRowIndexes(inColumn: Int) -> IndexSet?](./nsbrowser/selectedrowindexes%28incolumn%29.md)
  Provides the indexes of the selected rows in a given column of the browser.
- [func selectRowIndexes(IndexSet, inColumn: Int)](./nsbrowser/selectrowindexes%28_,incolumn%29.md)
  Specifies the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](./nsbrowser/allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).
### Managing Selection
- [func selectedCell(inColumn: Int) -> Any?](./nsbrowser/selectedcell%28incolumn%29.md)
  Returns the last (lowest) cell selected in the given column.
- [var selectedCells: [NSCell]?](./nsbrowser/selectedcells.md)
  All cells selected in the rightmost column.
- [func selectAll(Any?)](./nsbrowser/selectall%28_%29.md)
  Selects all cells in the last column of the browser.
- [func selectedRow(inColumn: Int) -> Int](./nsbrowser/selectedrow%28incolumn%29.md)
  Returns the row index of the selected cell in the specified column.
- [func selectRow(Int, inColumn: Int)](./nsbrowser/selectrow%28_,incolumn%29.md)
  Selects the cell at the specified row and column index.
- [var selectionIndexPath: IndexPath?](./nsbrowser/selectionindexpath.md)
  The index path of the item selected in the browser.
- [var selectionIndexPaths: [IndexPath]](./nsbrowser/selectionindexpaths.md)
  An array containing the index paths of all items selected in the browser.
- [selectedCell](./nsbrowser/selectedcell.md)
  The last (rightmost and lowest) selected cell.
### Accessing Components
- [func loadedCell(atRow: Int, column: Int) -> Any?](./nsbrowser/loadedcell%28atrow,column%29.md)
  Loads, if necessary, and returns the cell at the specified row and column location.
- [func editItem(at: IndexPath, with: NSEvent?, select: Bool)](./nsbrowser/edititem%28at,with,select%29.md)
  Begins editing the item at the specified path.
- [func item(at: IndexPath) -> Any?](./nsbrowser/item%28at%29.md)
  Returns the item at the specified index path.
- [func item(atRow: Int, inColumn: Int) -> Any?](./nsbrowser/item%28atrow,incolumn%29.md)
  Returns the item located at the specified row and column.
- [func indexPath(forColumn: Int) -> IndexPath](./nsbrowser/indexpath%28forcolumn%29.md)
  Returns the index path of the item whose children are displayed in the given column.
- [func isLeafItem(Any?) -> Bool](./nsbrowser/isleafitem%28_%29.md)
  Returns whether the specified item is a leaf item.
- [func parentForItems(inColumn: Int) -> Any?](./nsbrowser/parentforitems%28incolumn%29.md)
  Returns the item that contains the children located in the specified column.
### Managing the Path
- [func path() -> String](./nsbrowser/path%28%29.md)
  Returns a string representing the browser’s current path.
- [func setPath(String) -> Bool](./nsbrowser/setpath%28_%29.md)
  Sets the path to be displayed by the browser.
- [func path(toColumn: Int) -> String](./nsbrowser/path%28tocolumn%29.md)
  Returns a string representing the path from the first column up to, but not including, the column at the given index.
- [var pathSeparator: String](./nsbrowser/pathseparator.md)
  The path separator.
### Managing Columns
- [func addColumn()](./nsbrowser/addcolumn%28%29.md)
  Adds a column to the right of the last column.
- [var selectedColumn: Int](./nsbrowser/selectedcolumn.md)
  The index of the last column with a selected item.
- [var lastColumn: Int](./nsbrowser/lastcolumn.md)
  The index of the last column loaded.
- [var firstVisibleColumn: Int](./nsbrowser/firstvisiblecolumn.md)
  The index of the first visible column.
- [var numberOfVisibleColumns: Int](./nsbrowser/numberofvisiblecolumns.md)
  The number of visible columns.
- [var lastVisibleColumn: Int](./nsbrowser/lastvisiblecolumn.md)
  The index of the last visible column.
- [func validateVisibleColumns()](./nsbrowser/validatevisiblecolumns%28%29.md)
  Validates the browser’s visible columns.
- [var isLoaded: Bool](./nsbrowser/isloaded.md)
  A Boolean that indicates whether column 0 is loaded.
- [func loadColumnZero()](./nsbrowser/loadcolumnzero%28%29.md)
  Loads column 0; unloads previously loaded columns.
- [func reloadColumn(Int)](./nsbrowser/reloadcolumn%28_%29.md)
  Reloads the given column.
### Accessing Column Titles
- [func title(ofColumn: Int) -> String?](./nsbrowser/title%28ofcolumn%29.md)
  Returns the title displayed for the given column.
- [func setTitle(String, ofColumn: Int)](./nsbrowser/settitle%28_,ofcolumn%29.md)
  Sets the title of the given column.
- [var isTitled: Bool](./nsbrowser/istitled.md)
  A Boolean that indicates whether columns display titles.
- [func drawTitle(ofColumn: Int, in: NSRect)](./nsbrowser/drawtitle%28ofcolumn,in%29.md)
  Draws the title for the specified column within the given rectangle.
- [var titleHeight: CGFloat](./nsbrowser/titleheight.md)
  The height of the column titles for the browser.
- [func titleFrame(ofColumn: Int) -> NSRect](./nsbrowser/titleframe%28ofcolumn%29.md)
  Returns the bounds of the title frame for the specified column.
### Updating Browsers
- [func noteHeightOfRowsWithIndexesChanged(IndexSet, inColumn: Int)](./nsbrowser/noteheightofrowswithindexeschanged%28_,incolumn%29.md)
  Immediately retiles the browser’s columns using row heights specified by the browser’s delegate.
- [func reloadData(forRowIndexes: IndexSet, inColumn: Int)](./nsbrowser/reloaddata%28forrowindexes,incolumn%29.md)
  Updates the rows in the column with the specified column index with indexes in the specified set.
### Scrolling
- [var hasHorizontalScroller: Bool](./nsbrowser/hashorizontalscroller.md)
  A Boolean that indicates whether the browser has a horizontal scroller.
- [func scrollColumnToVisible(Int)](./nsbrowser/scrollcolumntovisible%28_%29.md)
  Scrolls to make the specified column visible.
- [func scrollColumnsLeft(by: Int)](./nsbrowser/scrollcolumnsleft%28by%29.md)
  Scrolls columns left by the specified number of columns.
- [func scrollColumnsRight(by: Int)](./nsbrowser/scrollcolumnsright%28by%29.md)
  Scrolls columns right by the specified number of columns.
- [func scrollRowToVisible(Int, inColumn: Int)](./nsbrowser/scrollrowtovisible%28_,incolumn%29.md)
  Scrolls the specified row to be visible within the specified column.
### Dragging
- [func setDraggingSourceOperationMask(NSDragOperation, forLocal: Bool)](./nsbrowser/setdraggingsourceoperationmask%28_,forlocal%29.md)
  Specifies the drag-operation mask for dragging operations with local or external destinations.
- [func canDragRows(with: IndexSet, inColumn: Int, with: NSEvent) -> Bool](./nsbrowser/candragrows%28with,incolumn,with%29.md)
  Indicates whether the browser can attempt to initiate a drag of the given rows for the given event.
- [func draggingImageForRows(with: IndexSet, inColumn: Int, with: NSEvent, offset: NSPointPointer?) -> NSImage?](./nsbrowser/draggingimageforrows%28with,incolumn,with,offset%29.md)
  Provides an image to represent dragged rows during a drag operation on the browser.
### Getting Column Frames
- [func frame(ofColumn: Int) -> NSRect](./nsbrowser/frame%28ofcolumn%29.md)
  Returns the rectangle containing the given column.
- [func frame(ofInsideOfColumn: Int) -> NSRect](./nsbrowser/frame%28ofinsideofcolumn%29.md)
  Returns the rectangle containing the specified column, not including borders.
### Getting Row Frames
- [func frame(ofRow: Int, inColumn: Int) -> NSRect](./nsbrowser/frame%28ofrow,incolumn%29.md)
  Returns the frame of the cell at the specified location, including the expandable arrow.
- [func getRow(UnsafeMutablePointer<Int>?, column: UnsafeMutablePointer<Int>?, for: NSPoint) -> Bool](./nsbrowser/getrow%28_,column,for%29.md)
  Gets the row and column coordinates for the specified point, if a cell exists at that point.
### Managing Actions
- [var doubleAction: Selector?](./nsbrowser/doubleaction.md)
  The browser’s double-click action method.
- [var sendsActionOnArrowKeys: Bool](./nsbrowser/sendsactiononarrowkeys.md)
  A Boolean that indicates whether pressing an arrow key causes an action message to be sent.
- [func sendAction() -> Bool](./nsbrowser/sendaction%28%29.md)
  Sends the action message to the target.
### Handling Mouse-Click Events
- [func doClick(Any?)](./nsbrowser/doclick%28_%29.md)
  Responds to (single) mouse clicks in a column of the browser.
- [func doDoubleClick(Any?)](./nsbrowser/dodoubleclick%28_%29.md)
  Responds to double clicks in a column of the browser.
- [var clickedColumn: Int](./nsbrowser/clickedcolumn.md)
  The column number of the cell that the user clicked to display a context menu.
- [var clickedRow: Int](./nsbrowser/clickedrow.md)
  The row number of the cell that the user clicked to display a context menu.
### Sizing
- [class func removeSavedColumns(withAutosaveName: NSBrowser.ColumnsAutosaveName)](./nsbrowser/removesavedcolumns%28withautosavename%29.md)
  Removes the column configuration data stored under the given name from the application’s user defaults.
- [var columnsAutosaveName: NSBrowser.ColumnsAutosaveName](./nsbrowser/columnsautosavename-swift.property.md)
  The name used to automatically save the browser’s column configuration.
- [NSBrowser.ColumnsAutosaveName](./nsbrowser/columnsautosavename-swift.typealias.md)
- [func columnContentWidth(forColumnWidth: CGFloat) -> CGFloat](./nsbrowser/columncontentwidth%28forcolumnwidth%29.md)
  Returns the content width for a given column width.
- [func columnWidth(forColumnContentWidth: CGFloat) -> CGFloat](./nsbrowser/columnwidth%28forcolumncontentwidth%29.md)
  Returns the column width for the width of the given column’s content.
- [var columnResizingType: NSBrowser.ColumnResizingType](./nsbrowser/columnresizingtype-swift.property.md)
  A constant indicating the browser’s column resizing type.
- [var prefersAllColumnUserResizing: Bool](./nsbrowser/prefersallcolumnuserresizing.md)
  A Boolean that indicates whether the browser is set to resize all columns simultaneously rather than resizing a single column at a time.
- [func width(ofColumn: Int) -> CGFloat](./nsbrowser/width%28ofcolumn%29.md)
  Returns the width of the specified column.
- [func setWidth(CGFloat, ofColumn: Int)](./nsbrowser/setwidth%28_,ofcolumn%29.md)
  Sets the width of the specified column.
- [func defaultColumnWidth() -> CGFloat](./nsbrowser/defaultcolumnwidth%28%29.md)
  Returns the default column width of the browser’s columns.
- [func setDefaultColumnWidth(CGFloat)](./nsbrowser/setdefaultcolumnwidth%28_%29.md)
  Sets the default column width for new browser columns that do not otherwise have an initial width from defaults or the browser’s delegate.
- [var rowHeight: CGFloat](./nsbrowser/rowheight.md)
  The height of the browser’s rows.
### Constants
- [NSBrowser.ColumnResizingType](./nsbrowser/columnresizingtype-swift.enum.md)
  Types of browser column resizing.
- [NSBrowser.DropOperation](./nsbrowser/dropoperation.md)
  The type used to specify the drop type of a drag-and-drop operation. See [`browser(_:validateDrop:proposedRow:column:dropOperation:)`](./nsbrowserdelegate/browser%28_,validatedrop,proposedrow,column,dropoperation%29.md) for more information.
- [Application Kit Versions for NSBrowser Functionality](./application-kit-versions-for-nsbrowser-functionality.md)
  The version of the AppKit.framework containing a specific bug fix or capability.
### Notifications
- [class let columnConfigurationDidChangeNotification: NSNotification.Name](./nsbrowser/columnconfigurationdidchangenotification.md)
  Notifies the delegate when the width of a browser column has changed.
### Instance Methods
- [func selectedCell() -> Any?](./nsbrowser/selectedcell%28%29.md)
### Deprecated
- [Deprecated symbols](./nsbrowser-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Structures
- [NSBrowser.ColumnConfigurationDidChangeMessage](./nsbrowser/columnconfigurationdidchangemessage.md)

## Relationships

### Inherits From
- [NSControl](./nscontrol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser)*