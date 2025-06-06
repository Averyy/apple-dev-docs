# NSTableColumn

**Framework**: AppKit  
**Kind**: class

The display characteristics and identifier for a column in a table view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTableColumn
```

#### Overview

A table column object determines the width (including the maximum and minimum widths) of its column in the table view and specifies the column’s  resizing and editing behavior. A table column stores two cell objects: the header cell, which is used to draw the column header, and the data cell, which is used to draw the values for each row. In a cell-based table, you can control the display of the column by specifying subclasses of `NSCell` to use and by setting the font and other display characteristics for these cells. For example, you can use an [`NSTextFieldCell`](nstextfieldcell.md) to display string values or substitute an [`NSImageCell`](nsimagecell.md) to display pictures.

## Topics

### Creating a Table Column
- [init(identifier: NSUserInterfaceItemIdentifier)](nstablecolumn/init(identifier:).md)
  Initializes a newly created table column with a string identifier.
### Setting the Table View
- [var tableView: NSTableView?](nstablecolumn/tableview.md)
  The table view that contains the table column.
### Controlling Size
- [var width: CGFloat](nstablecolumn/width.md)
  The table column’s width, in points.
- [var minWidth: CGFloat](nstablecolumn/minwidth.md)
  The table column’s minimum width, in points.
- [var maxWidth: CGFloat](nstablecolumn/maxwidth.md)
  The table column’s maximum width, in points.
- [var resizingMask: NSTableColumn.ResizingOptions](nstablecolumn/resizingmask.md)
  The table column’s resizing mask.
- [func sizeToFit()](nstablecolumn/sizetofit.md)
  Resizes the table column to fit the width of its header cell.
### Setting the Header
- [var title: String](nstablecolumn/title.md)
  The title of the table column’s header.
- [var headerCell: NSTableHeaderCell](nstablecolumn/headercell.md)
  The cell used to draw the table column’s header.
### Setting the Identifier
- [var identifier: NSUserInterfaceItemIdentifier](nstablecolumn/identifier.md)
  The identifier string for the table column.
### Controlling Editability in a Cell-Based Table
- [var isEditable: Bool](nstablecolumn/iseditable.md)
  A Boolean that indicates whether a cell-based table’s column cells are user editable.
### Sorting
- [var sortDescriptorPrototype: NSSortDescriptor?](nstablecolumn/sortdescriptorprototype.md)
  The table column’s sort descriptor prototype.
### Setting Column Visibility
- [var isHidden: Bool](nstablecolumn/ishidden.md)
  A Boolean that indicates whether the table column is hidden.
### Setting Tooltips
- [var headerToolTip: String?](nstablecolumn/headertooltip.md)
  The string that’s displayed in a help tag over the table column header.
### Deprecated Methods
- [var dataCell: Any](nstablecolumn/datacell.md)
  The cell prototype used by the table column to draw individual cells.
- [func dataCell(forRow: Int) -> Any](nstablecolumn/datacell(forrow:).md)
  Returns the cell object used to display values in the specified row of the table column.
### Constants
- [Resizing Modes](resizing-modes.md)
  These constants specify the resizing modes for a table column. The values are used to set the [`resizingMask`](nstablecolumn/resizingmask.md) property.
### Initializers
- [init(coder: NSCoder)](nstablecolumn/init(coder:).md)
### Structures
- [NSTableColumn.ResizingOptions](nstablecolumn/resizingoptions.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSTableHeaderView](nstableheaderview.md)
  An object that draws headers over a table view’s columns and handles mouse events in those headers.
- [class NSTableHeaderCell](nstableheadercell.md)
  An object that a table header view uses to draw the content of the column headers.
- [class NSTableRowView](nstablerowview.md)
  The view shown for a row in a table view.
- [class NSTableViewRowAction](nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.
- [NSTableColumn.ResizingOptions](nstablecolumn/resizingoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn)*