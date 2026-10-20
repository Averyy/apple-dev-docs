# tableView(_:shouldTypeSelectFor:withCurrentSearch:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to allow or deny type select for the specified event and current search string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldTypeSelectFor event: NSEvent, withCurrentSearch searchString: String?) -> Bool
```

```objc
- (BOOL) tableView:(NSTableView *) tableView shouldTypeSelectForEvent:(NSEvent *) event withCurrentSearchString:(NSString *) searchString;
```

#### Return Value

[`true`](../../Swift/true.md) to allow type select for event, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Typically, this is called from the [`NSTableView`](../nstableview.md) `keyDown:` implementation and the event will be a key event.

## Parameters

- `tableView`: The table view that sent the message.
- `event`: The event.
- `searchString`: The search string or `nil` if no type select has began.

## See Also

### Selecting rows
- [func selectionShouldChange(in: NSTableView) -> Bool](./selectionshouldchange%28in%29.md)
  Asks the delegate if the user is allowed to change the selection.
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
- [func tableView(NSTableView, typeSelectStringFor: NSTableColumn?, row: Int) -> String?](./tableview%28_,typeselectstringfor,row%29.md)
  Asks the delegate to provide an alternative text value used for type selection for the specified row and column.
- [func tableView(NSTableView, nextTypeSelectMatchFromRow: Int, toRow: Int, for: String) -> Int](./tableview%28_,nexttypeselectmatchfromrow,torow,for%29.md)
  Asks the delegate for the row within the specified search range that matches the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldtypeselectfor:withcurrentsearch:))*