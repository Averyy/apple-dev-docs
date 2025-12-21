# tableView(_:shouldEdit:row:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate if the cell at the specified row and column can be edited.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldEdit tableColumn: NSTableColumn?, row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow editing the cell, [`false`](https://developer.apple.com/documentation/Swift/false) to deny editing.

#### Discussion

The delegate can implement this method to disallow editing of specific cells.

> **Note**:  This method is only valid for [`NSCell`](nscell.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.
- `row`: The row index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldedit:row:))*