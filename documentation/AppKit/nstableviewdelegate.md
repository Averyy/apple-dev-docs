# NSTableViewDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods you implement in a table view delegate to customize the behavior of the table view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTableViewDelegate : NSControlTextEditingDelegate
```

#### Overview

Using a table view delegate allows you to customize a table view’s behavior without creating a table view subclass. A table view delegate provides views for table rows and columns, and supports functionality such as column reordering and resizing and row selection. To learn more about table views, see [`NSTableView`](nstableview.md).

## Topics

### Providing views for rows and columns
- [func tableView(NSTableView, viewFor: NSTableColumn?, row: Int) -> NSView?](nstableviewdelegate/tableview(_:viewfor:row:).md)
  Asks the delegate for a view to display the specified row and column.
- [func tableView(NSTableView, rowViewForRow: Int) -> NSTableRowView?](nstableviewdelegate/tableview(_:rowviewforrow:).md)
  Asks the delegate for a view to display the specified row.
### Notification of row views being added or removed
- [func tableView(NSTableView, didAdd: NSTableRowView, forRow: Int)](nstableviewdelegate/tableview(_:didadd:forrow:).md)
  Tells the delegate that a row view was added at the specified row.
- [func tableView(NSTableView, didRemove: NSTableRowView, forRow: Int)](nstableviewdelegate/tableview(_:didremove:forrow:).md)
  Tells the delegate that a row view was removed from the table at the specified row.
### Grouping rows
- [func tableView(NSTableView, isGroupRow: Int) -> Bool](nstableviewdelegate/tableview(_:isgrouprow:).md)
  Returns whether the specified row is a group row.
### Providing cells for rows and columns
- [func tableView(NSTableView, willDisplayCell: Any, for: NSTableColumn?, row: Int)](nstableviewdelegate/tableview(_:willdisplaycell:for:row:).md)
  Tells the delegate that the table view will display the specified cell at the specified row and column.
- [func tableView(NSTableView, dataCellFor: NSTableColumn?, row: Int) -> NSCell?](nstableviewdelegate/tableview(_:datacellfor:row:).md)
  Asks the delegate for a custom data cell for the specified row and column.
- [func tableView(NSTableView, shouldShowCellExpansionFor: NSTableColumn?, row: Int) -> Bool](nstableviewdelegate/tableview(_:shouldshowcellexpansionfor:row:).md)
  Asks the delegate if an expansion tooltip should be displayed for a specific row and column.
- [func tableView(NSTableView, toolTipFor: NSCell, rect: NSRectPointer, tableColumn: NSTableColumn?, row: Int, mouseLocation: NSPoint) -> String](nstableviewdelegate/tableview(_:tooltipfor:rect:tablecolumn:row:mouselocation:).md)
  Asks the delegate for a string to display in a tooltip for the specified cell in the column and row.
### Editing cells
- [func tableView(NSTableView, shouldEdit: NSTableColumn?, row: Int) -> Bool](nstableviewdelegate/tableview(_:shouldedit:row:).md)
  Asks the delegate if the cell at the specified row and column can be edited.
### Setting row and column size
- [func tableView(NSTableView, heightOfRow: Int) -> CGFloat](nstableviewdelegate/tableview(_:heightofrow:).md)
  Asks the delegate for the height of the specified row.
- [func tableView(NSTableView, sizeToFitWidthOfColumn: Int) -> CGFloat](nstableviewdelegate/tableview(_:sizetofitwidthofcolumn:).md)
  Asks the delegate to provide custom sizing behavior when a column’s resize divider is double clicked.
### Selecting rows
- [func selectionShouldChange(in: NSTableView) -> Bool](nstableviewdelegate/selectionshouldchange(in:).md)
  Asks the delegate if the user is allowed to change the selection.
- [func tableView(NSTableView, shouldSelectRow: Int) -> Bool](nstableviewdelegate/tableview(_:shouldselectrow:).md)
  Asks the delegate if the table view should allow selection of the specified row.
- [func tableView(NSTableView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](nstableviewdelegate/tableview(_:selectionindexesforproposedselection:).md)
  Asks the delegate to accept or reject the proposed selection.
- [func tableView(NSTableView, shouldSelect: NSTableColumn?) -> Bool](nstableviewdelegate/tableview(_:shouldselect:).md)
  Asks the delegate whether the specified table column can be selected.
- [func tableViewSelectionIsChanging(Notification)](nstableviewdelegate/tableviewselectionischanging(_:).md)
  Tells the delegate that the table view’s selection is in the process of changing.
- [func tableViewSelectionDidChange(Notification)](nstableviewdelegate/tableviewselectiondidchange(_:).md)
  Tells the delegate that the table view’s selection has changed.
- [func tableView(NSTableView, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](nstableviewdelegate/tableview(_:shouldtypeselectfor:withcurrentsearch:).md)
  Asks the delegate to allow or deny type select for the specified event and current search string.
- [func tableView(NSTableView, typeSelectStringFor: NSTableColumn?, row: Int) -> String?](nstableviewdelegate/tableview(_:typeselectstringfor:row:).md)
  Asks the delegate to provide an alternative text value used for type selection for the specified row and column.
- [func tableView(NSTableView, nextTypeSelectMatchFromRow: Int, toRow: Int, for: String) -> Int](nstableviewdelegate/tableview(_:nexttypeselectmatchfromrow:torow:for:).md)
  Asks the delegate for the row within the specified search range that matches the specified string.
### Moving and resizing columns
- [func tableView(NSTableView, shouldReorderColumn: Int, toColumn: Int) -> Bool](nstableviewdelegate/tableview(_:shouldreordercolumn:tocolumn:).md)
  Asks the delegate to allow or prohibit the specified column to be dragged to a new location.
- [func tableView(NSTableView, didDrag: NSTableColumn)](nstableviewdelegate/tableview(_:diddrag:).md)
  Tells the delegate that the specified table column was dragged.
- [func tableViewColumnDidMove(Notification)](nstableviewdelegate/tableviewcolumndidmove(_:).md)
  Tells the delegate that a table column was moved by user action.
- [func tableViewColumnDidResize(Notification)](nstableviewdelegate/tableviewcolumndidresize(_:).md)
  Tells the delegate that a table column was resized.
### Responding to mouse events
- [func tableView(NSTableView, didClick: NSTableColumn)](nstableviewdelegate/tableview(_:didclick:).md)
  Tells the delegate that the mouse button was clicked in the specified table column, but the column was not dragged.
- [func tableView(NSTableView, mouseDownInHeaderOf: NSTableColumn)](nstableviewdelegate/tableview(_:mousedowninheaderof:).md)
  Tells the delegate that the mouse button was clicked in the specified table column’s header.
- [func tableView(NSTableView, shouldTrackCell: NSCell, for: NSTableColumn?, row: Int) -> Bool](nstableviewdelegate/tableview(_:shouldtrackcell:for:row:).md)
  Asks the delegate whether the specified cell should be tracked.
### Enabling table row actions
- [func tableView(NSTableView, rowActionsForRow: Int, edge: NSTableView.RowActionEdge) -> [NSTableViewRowAction]](nstableviewdelegate/tableview(_:rowactionsforrow:edge:).md)
  Asks the delegate to provide an array of row actions to be attached to the specified edge of a table row and displayed when the user swipes horizontally across the row.
### Showing and hiding columns
- [func tableView(NSTableView, userCanChangeVisibilityOf: NSTableColumn) -> Bool](nstableviewdelegate/tableview(_:usercanchangevisibilityof:).md)
  Asks the delegate to verify that the user can change the given column’s visibility.
- [func tableView(NSTableView, userDidChangeVisibilityOf: [NSTableColumn])](nstableviewdelegate/tableview(_:userdidchangevisibilityof:).md)
  Tells the delegate that the user changed the visibility of one or more table columns.

## Relationships

### Inherits From
- [NSControlTextEditingDelegate](nscontroltexteditingdelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSTableViewDataSource](nstableviewdatasource.md)
  A set of methods that a table view uses to provide data to a table view and to allow the editing of the table view’s data source object.
- [class NSTableViewDiffableDataSource](nstableviewdiffabledatasource-c5gl.md)
  The object you use to manage data and provide items for a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate)*