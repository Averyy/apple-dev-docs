# numberOfRows(in:)

**Framework**: AppKit  
**Kind**: method

Returns the number of records managed for `aTableView` by the data source object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func numberOfRows(in tableView: NSTableView) -> Int
```

#### Return Value

The number of rows in `aTableView`.

#### Discussion

An instance of [`NSTableView`](nstableview.md) uses this method to determine how many rows it should create and display. Your [`numberOfRows(in:)`](nstableviewdatasource/numberofrows(in:).md) implementation is called very frequently, so it must be efficient.

Both view-based table views and cell-based table views must implement this method.

> **Note**:  This method is mandatory unless your application is using Cocoa bindings for providing data to the table view.

## Parameters

- `tableView`: The table view that sent the message.

## See Also

- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)
- [func tableView(NSTableView, objectValueFor: NSTableColumn?, row: Int) -> Any?](nstableviewdatasource/tableview(_:objectvaluefor:row:).md)
  Called by the table view to return the data object associated with the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/numberofrows(in:))*