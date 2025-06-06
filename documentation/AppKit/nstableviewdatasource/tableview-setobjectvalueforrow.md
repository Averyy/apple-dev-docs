# tableView(_:setObjectValue:for:row:)

**Framework**: AppKit  
**Kind**: method

Sets the data object for an item in the specified row and column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, setObjectValue object: Any?, for tableColumn: NSTableColumn?, row: Int)
```

#### Discussion

This method is intended for use with cell-based table views, it must not be used with view-based table views. In view-based tables, use target/action to set each item in the view cell.

> **Note**:  This method is optional if your application is using Cocoa bindings for providing data to the table view, otherwise it must be implemented.

 This method is optional if your application is using Cocoa bindings for providing data to the table view, otherwise it must be implemented.

## Parameters

- `tableView`: The table view that sent the message.
- `object`: The new value for the item.
- `tableColumn`: A column in  .
- `row`: The row of the item in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:setobjectvalue:for:row:))*