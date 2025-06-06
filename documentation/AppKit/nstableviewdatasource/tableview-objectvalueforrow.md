# tableView(_:objectValueFor:row:)

**Framework**: Appkit  
**Kind**: method

Called by the table view to return the data object associated with the specified row and column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, objectValueFor tableColumn: NSTableColumn?, row: Int) -> Any?
```

#### Return Value

An item in the data source in the specified table column of the view.

#### Discussion

[`tableView(_:objectValueFor:row:)`](nstableviewdatasource/tableview(_:objectvaluefor:row:).md) is called each time the table cell needs to be redisplayed, so it must be efficient.

> **Note**:  This method is mandatory unless your application is using Cocoa bindings for providing data to the table view.

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: A column in  .
- `row`: The row of the item in  .

## See Also

- [func numberOfRows(in: NSTableView) -> Int](nstableviewdatasource/numberofrows(in:).md)
  Returns the number of records managed for `aTableView` by the data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:objectvaluefor:row:))*