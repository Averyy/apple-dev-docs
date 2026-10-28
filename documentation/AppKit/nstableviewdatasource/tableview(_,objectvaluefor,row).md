# tableView(_:objectValueFor:row:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called by the table view to return the data object associated with the specified row and column.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, objectValueFor tableColumn: NSTableColumn?, row: Int) -> Any?
```

```objc
- (id) tableView:(NSTableView *) tableView objectValueForTableColumn:(NSTableColumn *) tableColumn row:(NSInteger) row;
```

## Return Value

An item in the data source in the specified table column of the view.

## Discussion

[`tableView(_:objectValueFor:row:)`](./tableview%28_,objectvaluefor,row%29.md) is called each time the table cell needs to be redisplayed, so it must be efficient.

> **Note**:  This method is mandatory unless your application is using Cocoa bindings for providing data to the table view.

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: A column in `aTableView`.
- `row`: The row of the item in `aTableColumn`.

## See Also

### Getting Values
- [func numberOfRows(in: NSTableView) -> Int](./numberofrows%28in%29.md)
  Returns the number of records managed for `aTableView` by the data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/tableview(_:objectvaluefor:row:))*