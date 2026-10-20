# NSMatrix

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A legacy interface for grouping radio buttons or other types of cells together.

**Availability**:
- macOS

## Declaration

```swift
class NSMatrix
```

```objc
@interface NSMatrix : NSControl
```

#### Overview

> ❗ **Important**:  Use of NSMatrix is discouraged in apps that run in macOS 10.8 and later. If you need to create a radio button group in an app that runs in macOS 10.8 and later, create instances of [NSButton](https://developer.apple.com/library/archive/technotes/tn2219/_index.html#//apple_ref/doc/uid/DTS10004624-CH1-SUBSECTION12) that each specify a button type of `NSRadioButton` and specify the same action and the same superview for each button in the group.

`NSMatrix` uses flipped coordinates by default. The cells in an [`NSMatrix`](./nsmatrix.md) object are numbered by row and column, each starting with 0; for example, the top left [`NSCell`](./nscell.md) would be at (0, 0), and the [`NSCell`](./nscell.md) that’s second down and third across would be at (1, 2).

The [`NSMatrix`](./nsmatrix.md) class has the notion of a single selected cell, which is the cell that was most recently clicked or that was so designated by a [`selectCell(atRow:column:)`](./nsmatrix/selectcell%28atrow,column%29.md) or [`selectCell(withTag:)`](./nsmatrix/selectcell%28withtag%29.md) message. The selected cell is the cell chosen for action messages except for [`performClick(_:)`](./nscell/performclick%28_%29.md) ([`NSCell`](./nscell.md)), which is assigned to the key cell. (The key cell is generally identical to the selected cell, but can be given click focus while leaving the selected cell unchanged.) If the user has selected multiple cells, the selected cell is the one lowest and furthest to the right in the matrix of cells.

## Topics

### Initializing an NSMatrix Object
- [convenience init(frame: NSRect)](./nsmatrix/init%28frame%29.md)
  Initializes a newly allocated matrix with the specified frame.
- [init(frame: NSRect, mode: NSMatrix.Mode, cellClass: AnyClass?, numberOfRows: Int, numberOfColumns: Int)](./nsmatrix/init%28frame,mode,cellclass,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using cells of the given class.
- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](./nsmatrix/init%28frame,mode,prototype,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.
### Configuring the Matrix Object
- [var mode: NSMatrix.Mode](./nsmatrix/mode-swift.property.md)
  The selection mode of the receiver.
- [var allowsEmptySelection: Bool](./nsmatrix/allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
- [var isSelectionByRect: Bool](./nsmatrix/isselectionbyrect.md)
  A Boolean that indicates whether the user can select a rectangle of cells in the receiver by dragging the cursor.
### Managing the Cell Class
- [var cellClass: AnyClass](./nsmatrix/cellclass.md)
  The subclass of [`NSCell`](./nscell.md) that the matrix uses when creating new (empty) cells.
- [var prototype: NSCell?](./nsmatrix/prototype.md)
  The prototype cell that’s copied whenever the matrix creates a new cell.
### Laying Out the Cells of the Matrix
- [func addColumn()](./nsmatrix/addcolumn%28%29.md)
  Adds a new column of cells to the right of the last column.
- [func addColumn(with: [NSCell])](./nsmatrix/addcolumn%28with%29.md)
  Adds a new column of cells to the right of the last column, using the given cells.
- [func addRow()](./nsmatrix/addrow%28%29.md)
  Adds a new row of cells below the last row.
- [func addRow(with: [NSCell])](./nsmatrix/addrow%28with%29.md)
  Adds a new row of cells below the last row, using the specified cells.
- [func cellFrame(atRow: Int, column: Int) -> NSRect](./nsmatrix/cellframe%28atrow,column%29.md)
  Returns the frame rectangle of the cell that would be drawn at the specified location.
- [var cellSize: NSSize](./nsmatrix/cellsize.md)
  The size of each cell in the matrix.
- [func getNumberOfRows(UnsafeMutablePointer<Int>?, columns: UnsafeMutablePointer<Int>?)](./nsmatrix/getnumberofrows%28_,columns%29.md)
  Obtains the number of rows and columns in the receiver.
- [func insertColumn(Int)](./nsmatrix/insertcolumn%28_%29.md)
  Inserts a new column of cells at the specified location.
- [func insertColumn(Int, with: [NSCell]?)](./nsmatrix/insertcolumn%28_,with%29.md)
  Inserts a new column of cells before the specified column, using the given cells.
- [func insertRow(Int)](./nsmatrix/insertrow%28_%29.md)
  Inserts a new row of cells before the specified row.
- [func insertRow(Int, with: [NSCell]?)](./nsmatrix/insertrow%28_,with%29.md)
  Inserts a new row of cells before the specified row, using the given cells.
- [var intercellSpacing: NSSize](./nsmatrix/intercellspacing.md)
  The vertical and horizontal spacing between cells in the matrix.
- [func makeCell(atRow: Int, column: Int) -> NSCell](./nsmatrix/makecell%28atrow,column%29.md)
  Creates a new cell at the location specified by the given row and column in the receiver.
- [var numberOfColumns: Int](./nsmatrix/numberofcolumns.md)
  The number of columns in the matrix.
- [var numberOfRows: Int](./nsmatrix/numberofrows.md)
  The number of rows in the matrix.
- [func putCell(NSCell, atRow: Int, column: Int)](./nsmatrix/putcell%28_,atrow,column%29.md)
  Replaces the cell at the specified row and column with the new cell.
- [func removeColumn(Int)](./nsmatrix/removecolumn%28_%29.md)
  Removes the specified column at from the receiver.
- [func removeRow(Int)](./nsmatrix/removerow%28_%29.md)
  Removes the specified row from the receiver.
- [func renewRows(Int, columns: Int)](./nsmatrix/renewrows%28_,columns%29.md)
  Changes the number of rows and columns in the receiver.
- [func sort(using: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](./nsmatrix/sort%28using,context%29.md)
  Sorts the receiver’s cells in ascending order as defined by the specified comparison function.
- [func sort(using: Selector)](./nsmatrix/sort%28using%29.md)
  Sorts the receiver’s cells in ascending order as defined by the comparison method.
### Auto Layout Sizing
- [var autorecalculatesCellSize: Bool](./nsmatrix/autorecalculatescellsize.md)
  A Boolean that indicates whether the matrix auto-recalculates its cell size.
### Finding Matrix Coordinates
- [func getRow(UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, for: NSPoint) -> Bool](./nsmatrix/getrow%28_,column,for%29.md)
  Indicates whether the specified point lies within one of the cells of the matrix and returns the location of the cell within which the point lies.
- [func getRow(UnsafeMutablePointer<Int>, column: UnsafeMutablePointer<Int>, of: NSCell) -> Bool](./nsmatrix/getrow%28_,column,of%29.md)
  Searches the receiver for the specified cell and returns the row and column of the cell
### Managing Attributes of Individual Cells
- [func setState(Int, atRow: Int, column: Int)](./nsmatrix/setstate%28_,atrow,column%29.md)
  Sets the state of the cell at specified location.
- [func setToolTip(String?, for: NSCell)](./nsmatrix/settooltip%28_,for%29.md)
  Sets the tooltip for the cell.
- [func toolTip(for: NSCell) -> String?](./nsmatrix/tooltip%28for%29.md)
  Returns the tooltip for the specified cell.
### Selecting and Deselecting Cells
- [func selectCell(atRow: Int, column: Int)](./nsmatrix/selectcell%28atrow,column%29.md)
  Selects the cell at the specified row and column within the receiver.
- [func selectCell(withTag: Int) -> Bool](./nsmatrix/selectcell%28withtag%29.md)
  Selects the last cell with the given tag.
- [func selectAll(Any?)](./nsmatrix/selectall%28_%29.md)
  Selects and highlights all cells in the receiver.
- [var keyCell: NSCell?](./nsmatrix/keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func setSelectionFrom(Int, to: Int, anchor: Int, highlight: Bool)](./nsmatrix/setselectionfrom%28_,to,anchor,highlight%29.md)
  Programmatically selects a range of cells.
- [func deselectAllCells()](./nsmatrix/deselectallcells%28%29.md)
  Deselects all cells in the receiver and, if necessary, redisplays the receiver.
- [func deselectSelectedCell()](./nsmatrix/deselectselectedcell%28%29.md)
  Deselects the selected cell or cells.
### Finding Cells
- [var selectedCells: [NSCell]](./nsmatrix/selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](./nsmatrix/selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](./nsmatrix/selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](./nsmatrix/cell%28atrow,column%29.md)
  Returns the cell at the specified row and column.
- [func cell(withTag: Int) -> NSCell?](./nsmatrix/cell%28withtag%29.md)
  Searches the receiver and returns the last cell matching the specified tag.
- [var cells: [NSCell]](./nsmatrix/cells.md)
  An array containing the cells of the matrix.
### Modifying Graphics Attributes
- [var backgroundColor: NSColor](./nsmatrix/backgroundcolor.md)
  The background color of the matrix (the space between the cells).
- [var cellBackgroundColor: NSColor?](./nsmatrix/cellbackgroundcolor.md)
  The background color of the matrix’s cells.
- [var drawsBackground: Bool](./nsmatrix/drawsbackground.md)
  A Boolean that indicates whether the matrix draws its background.
- [var drawsCellBackground: Bool](./nsmatrix/drawscellbackground.md)
  A Boolean that indicates whether the matrix draws the background within each of its cells.
### Editing Text in Cells
- [func selectText(Any?)](./nsmatrix/selecttext%28_%29.md)
  Selects text in the currently selected cell or in the key cell.
- [func selectText(atRow: Int, column: Int) -> NSCell?](./nsmatrix/selecttext%28atrow,column%29.md)
  Selects the text in the cell at the specified location and returns the cell.
- [func textShouldBeginEditing(NSText) -> Bool](./nsmatrix/textshouldbeginediting%28_%29.md)
  Requests permission to begin editing text.
- [func textDidBeginEditing(Notification)](./nsmatrix/textdidbeginediting%28_%29.md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](./nsmatrix/textdidchange%28_%29.md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textShouldEndEditing(NSText) -> Bool](./nsmatrix/textshouldendediting%28_%29.md)
  Requests permission to end editing.
- [func textDidEndEditing(Notification)](./nsmatrix/textdidendediting%28_%29.md)
  Invoked when text editing ends.
### Setting Tab Key Behavior
- [var tabKeyTraversesCells: Bool](./nsmatrix/tabkeytraversescells.md)
  A Boolean that indicates whether pressing the Tab key advances the key cell to the next selectable cell.
### Managing the Delegate
- [var delegate: (any NSMatrixDelegate)?](./nsmatrix/delegate.md)
  The delegate for messages from the field editor.
- [protocol NSMatrixDelegate](./nsmatrixdelegate.md)
  The `NSMatrixDelegate` protocol defines the optional methods implemented by delegates of `NSMatrix` objects.
### Resizing the Matrix and Its Cells
- [var autosizesCells: Bool](./nsmatrix/autosizescells.md)
  A Boolean that indicates whether the cell sizes change when the receiver is resized.
- [func setValidateSize(Bool)](./nsmatrix/setvalidatesize%28_%29.md)
  Specifies whether the receiver’s size information is validated.
- [func sizeToCells()](./nsmatrix/sizetocells%28%29.md)
  Changes the width and the height of the receiver’s frame so it exactly contains the cells.
### Scrolling Cells in the Matrix
- [var isAutoscroll: Bool](./nsmatrix/isautoscroll.md)
  A Boolean that indicates whether the receiver is automatically scrolled.
- [func setScrollable(Bool)](./nsmatrix/setscrollable%28_%29.md)
  Specifies whether the cells in the matrix are scrollable.
- [func scrollCellToVisible(atRow: Int, column: Int)](./nsmatrix/scrollcelltovisible%28atrow,column%29.md)
  Scrolls the receiver so the specified cell is visible.
### Displaying and Highlighting Cells
- [func drawCell(atRow: Int, column: Int)](./nsmatrix/drawcell%28atrow,column%29.md)
  Displays the cell at the specified row and column.
- [func highlightCell(Bool, atRow: Int, column: Int)](./nsmatrix/highlightcell%28_,atrow,column%29.md)
  Highlights or unhighlights the cell at the specified row and column location.
### Managing and Sending Action Messages
- [func sendAction() -> Bool](./nsmatrix/sendaction%28%29.md)
  If the selected cell has both an action and a target, sends its action to its target.
- [func sendAction(Selector, to: Any, forAllCells: Bool)](./nsmatrix/sendaction%28_,to,forallcells%29.md)
  Iterates through the cells in the receiver, sending the specified selector to an object for each cell.
- [var doubleAction: Selector?](./nsmatrix/doubleaction.md)
  The action sent to the target of the receiver when the user double-clicks a cell.
- [func sendDoubleAction()](./nsmatrix/senddoubleaction%28%29.md)
  Sends the double-click action message to the target of the receiver.
### Handling Event and Action Messages
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./nsmatrix/acceptsfirstmouse%28for%29.md)
  Returns a Boolean value indicating whether the receiver accepts the first mouse.
- [func mouseDown(with: NSEvent)](./nsmatrix/mousedown%28with%29.md)
  Responds to a mouse-down event.
- [var mouseDownFlags: Int](./nsmatrix/mousedownflags.md)
  The flags in effect at the mouse-down event that started the current tracking session.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./nsmatrix/performkeyequivalent%28with%29.md)
  Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.
### Managing the Cursor
- [func resetCursorRects()](./nsmatrix/resetcursorrects%28%29.md)
  Resets cursor rectangles so the cursor becomes an I-beam over text cells.
### Constants
- [NSMatrix.Mode](./nsmatrix/mode-swift.enum.md)
  These constants determine how [`NSCell`](./nscell.md) objects behave when an [`NSMatrix`](./nsmatrix.md) object is tracking the mouse.
### Instance Methods
- [func selectedCell() -> NSCell?](./nsmatrix/selectedcell%28%29.md)

## Relationships

### Inherits From
- [NSControl](./nscontrol.md)
### Inherited By
- [NSForm](./nsform.md)
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
- [NSUserInterfaceValidations](./nsuserinterfacevalidations.md)
- [NSViewToolTipOwner](./nsviewtooltipowner.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controls
- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](./nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](./nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](./combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](./nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](./date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](./nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](./nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](./path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](./nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSProgressIndicator](./nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSRuleEditor](./nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](./nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](./search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](./nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix)*