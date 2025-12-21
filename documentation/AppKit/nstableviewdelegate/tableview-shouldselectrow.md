# tableView(_:shouldSelectRow:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate if the table view should allow selection of the specified row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldSelectRow row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to permit selection of the row, [`false`](https://developer.apple.com/documentation/Swift/false) to deny selection.

#### Discussion

The delegate can implement this method to disallow selection of particular rows.

For better performance and finer-grain control over the selection, use [`tableView(_:selectionIndexesForProposedSelection:)`](nstableviewdelegate/tableview(_:selectionindexesforproposedselection:).md).

## Parameters

- `tableView`: The table view that sent the message.
- `row`: The row index.

## See Also

- [func selectionShouldChange(in: NSTableView) -> Bool](nstableviewdelegate/selectionshouldchange(in:).md)
  Asks the delegate if the user is allowed to change the selection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldselectrow:))*