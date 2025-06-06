# tableView(_:selectionIndexesForProposedSelection:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to accept or reject the proposed selection.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, selectionIndexesForProposedSelection proposedSelectionIndexes: IndexSet) -> IndexSet
```

#### Return Value

An [`NSIndexSet`](https://developer.apple.com/documentation/Foundation/NSIndexSet) instance containing the indexes of the new selection. Return `proposedSelectionIndexes` if the proposed selection is acceptable, or the value of the table view’s existing selection to avoid changing the selection.

#### Discussion

This method may be called multiple times with one new index added to the existing selection to find out if a particular index can be selected when the user is extending the selection with the keyboard or mouse.

If implemented, this method will be called instead of [`tableView(_:shouldSelectRow:)`](nstableviewdelegate/tableview(_:shouldselectrow:).md).

## Parameters

- `tableView`: The table view that sent the message.
- `proposedSelectionIndexes`: An index set containing the indexes of the proposed selection.

## See Also

- [func selectionShouldChange(in: NSTableView) -> Bool](nstableviewdelegate/selectionshouldchange(in:).md)
  Asks the delegate if the user is allowed to change the selection.
- [func tableView(NSTableView, shouldSelectRow: Int) -> Bool](nstableviewdelegate/tableview(_:shouldselectrow:).md)
  Asks the delegate if the table view should allow selection of the specified row.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:selectionindexesforproposedselection:))*