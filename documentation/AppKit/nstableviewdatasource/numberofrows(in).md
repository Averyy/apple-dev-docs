# numberOfRows(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of records managed for `aTableView` by the data source object.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func numberOfRows(in tableView: NSTableView) -> Int
```

```objc
- (NSInteger) numberOfRowsInTableView:(NSTableView *) tableView;
```

#### Return Value

The number of rows in `aTableView`.

#### Discussion

An instance of [`NSTableView`](../nstableview.md) uses this method to determine how many rows it should create and display. Your [`numberOfRows(in:)`](./numberofrows%28in%29.md) implementation is called very frequently, so it must be efficient.

Both view-based table views and cell-based table views must implement this method.

> **Note**:  This method is mandatory unless your application is using Cocoa bindings for providing data to the table view.

## Parameters

- `tableView`: The table view that sent the message.

## See Also

### Related Documentation
- [class NSTableView](../nstableview.md)
  A set of related records, displayed in rows that represent individual records and columns that represent the attributes of those records.
### Getting Values
- [func tableView(NSTableView, objectValueFor: NSTableColumn?, row: Int) -> Any?](./tableview%28_,objectvaluefor,row%29.md)
  Called by the table view to return the data object associated with the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdatasource/numberofrows(in:))*