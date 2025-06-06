# tableView(_:isGroupRow:)

**Framework**: Appkit  
**Kind**: method

Returns whether the specified row is a group row.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, isGroupRow row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified row should have the group row style drawn, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

If the cell in `row` is an [`NSTextFieldCell`](nstextfieldcell.md) object and contains only a string, the group row style attributes are automatically applied to the cell.

Group rows in [`NSView`](nsview.md)-based table views can be made to visually “float” by setting the table view method [`floatsGroupRows`](nstableview/floatsgrouprows.md) to [`true`](https://developer.apple.com/documentation/swift/true).

> **Note**:  When configured as a source list style table view, rows identified as group rows draw with a specific style unique to source lists.

## Parameters

- `tableView`: The table view that sent the message.
- `row`: The row index.

## See Also

- [var floatsGroupRows: Bool](nstableview/floatsgrouprows.md)
  A Boolean value indicating whether the table view draws grouped rows as if they are floating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:isgrouprow:))*