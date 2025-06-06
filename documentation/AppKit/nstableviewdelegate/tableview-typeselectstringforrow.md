# tableView(_:typeSelectStringFor:row:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to provide an alternative text value used for type selection for the specified row and column.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, typeSelectStringFor tableColumn: NSTableColumn?, row: Int) -> String?
```

#### Return Value

A string that is used in type select comparison for `row` and `tableColumn`. Return `nil` if `row` or `tableColumn` should not be searched.

#### Discussion

Implement this method to change the string value that is searched for based on what is displayed. By default, all cells with text in them are searched.

If this delegate method isn’t implemented, the default string value (which can also be returned from the delegate method) is:

```objc
[[tableView preparedCellAtColumn:tableColumn row:row] stringValue]
```

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.
- `row`: The row index.

## See Also

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
- [func tableView(NSTableView, nextTypeSelectMatchFromRow: Int, toRow: Int, for: String) -> Int](nstableviewdelegate/tableview(_:nexttypeselectmatchfromrow:torow:for:).md)
  Asks the delegate for the row within the specified search range that matches the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:typeselectstringfor:row:))*