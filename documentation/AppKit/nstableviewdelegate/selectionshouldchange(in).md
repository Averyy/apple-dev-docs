# selectionShouldChange(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the user is allowed to change the selection.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func selectionShouldChange(in tableView: NSTableView) -> Bool
```

```objc
- (BOOL) selectionShouldChangeInTableView:(NSTableView *) tableView;
```

#### Return Value

[`true`](../../Swift/true.md) to allow the table view to change its selection (typically a row being edited), [`false`](../../Swift/false.md) to deny selection change.

#### Discussion

The user can select and edit different cells within the same row, but can’t select another row unless the delegate approves. The delegate can implement this method for complex validation of edited rows based on the values of any of their cells.

## Parameters

- `tableView`: The table view that sent the message.

## See Also

### Selecting rows
- [func tableView(NSTableView, shouldSelectRow: Int) -> Bool](./tableview%28_,shouldselectrow%29.md)
  Asks the delegate if the table view should allow selection of the specified row.
- [func tableView(NSTableView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](./tableview%28_,selectionindexesforproposedselection%29.md)
  Asks the delegate to accept or reject the proposed selection.
- [func tableView(NSTableView, shouldSelect: NSTableColumn?) -> Bool](./tableview%28_,shouldselect%29.md)
  Asks the delegate whether the specified table column can be selected.
- [func tableViewSelectionIsChanging(Notification)](./tableviewselectionischanging%28_%29.md)
  Tells the delegate that the table view’s selection is in the process of changing.
- [func tableViewSelectionDidChange(Notification)](./tableviewselectiondidchange%28_%29.md)
  Tells the delegate that the table view’s selection has changed.
- [func tableView(NSTableView, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](./tableview%28_,shouldtypeselectfor,withcurrentsearch%29.md)
  Asks the delegate to allow or deny type select for the specified event and current search string.
- [func tableView(NSTableView, typeSelectStringFor: NSTableColumn?, row: Int) -> String?](./tableview%28_,typeselectstringfor,row%29.md)
  Asks the delegate to provide an alternative text value used for type selection for the specified row and column.
- [func tableView(NSTableView, nextTypeSelectMatchFromRow: Int, toRow: Int, for: String) -> Int](./tableview%28_,nexttypeselectmatchfromrow,torow,for%29.md)
  Asks the delegate for the row within the specified search range that matches the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/selectionshouldchange(in:))*