# tableView(_:nextTypeSelectMatchFromRow:toRow:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the row within the specified search range that matches the specified string.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, nextTypeSelectMatchFromRow startRow: Int, toRow endRow: Int, for searchString: String) -> Int
```

```objc
- (NSInteger) tableView:(NSTableView *) tableView nextTypeSelectMatchFromRow:(NSInteger) startRow toRow:(NSInteger) endRow forString:(NSString *) searchString;
```

#### Return Value

The first row in the range of `startRow` through `endRow` (excluding `endRow` itself) that matches `selectionString`. Return `-1` if no match is found.

#### Discussion

Use this method to control how type selection works in a table. (Implementation of this method isn’t required to support type selection.) Note that it’s possible for `endRow` to be less than `startRow` if the search will wrap.

## Parameters

- `tableView`: The table view that sent the message.
- `startRow`: The starting row of the search range.
- `endRow`: The ending row of the search range.
- `searchString`: A string containing the typed selection.

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
- [func tableView(NSTableView, shouldTypeSelectFor: NSEvent, withCurrentSearch: String?) -> Bool](./tableview%28_,shouldtypeselectfor,withcurrentsearch%29.md)
  Asks the delegate to allow or deny type select for the specified event and current search string.
- [func tableView(NSTableView, typeSelectStringFor: NSTableColumn?, row: Int) -> String?](./tableview%28_,typeselectstringfor,row%29.md)
  Asks the delegate to provide an alternative text value used for type selection for the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:nexttypeselectmatchfromrow:torow:for:))*