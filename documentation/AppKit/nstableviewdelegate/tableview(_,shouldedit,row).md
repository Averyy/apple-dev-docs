# tableView(_:shouldEdit:row:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the cell at the specified row and column can be edited.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldEdit tableColumn: NSTableColumn?, row: Int) -> Bool
```

```objc
- (BOOL) tableView:(NSTableView *) tableView shouldEditTableColumn:(NSTableColumn *) tableColumn row:(NSInteger) row;
```

## Return Value

[`true`](../../Swift/true.md) to allow editing the cell, [`false`](../../Swift/false.md) to deny editing.

## Discussion

The delegate can implement this method to disallow editing of specific cells.

> **Note**:  This method is only valid for [`NSCell`](../nscell.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.
- `row`: The row index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldedit:row:))*