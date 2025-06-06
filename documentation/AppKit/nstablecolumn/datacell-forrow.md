# dataCell(forRow:)

**Framework**: AppKit  
**Kind**: method

Returns the cell object used to display values in the specified row of the table column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func dataCell(forRow row: Int) -> Any
```

#### Return Value

The data cell object.

#### Discussion

Returns the [`NSCell`](nscell.md) object used by the table view to draw values for the receiver. The table view calls this method when drawing the row, so you shouldn’t need to call it directly. By default, this method just accesses [`dataCell`](nstablecolumn/datacell.md).

To enable per-row customization of the cell used by the table column, you can override this method or use the `NSTableViewDelegate` method [`tableView(_:dataCellFor:row:)`](nstableviewdelegate/tableview(_:datacellfor:row:).md). In both cases, the cell that’s returned should properly implement [`copy(with:)`](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy), because the table view may copy the cell during certain operations.

Subclasses should be prepared for this method to be called with `row` equal to –1 in cases where no actual row is involved but the table view needs to get some generic cell information.

> **Note**:  This method is only valid for cell-based table views.

 This method is only valid for cell-based table views.

## Parameters

- `row`: The table column row.

## See Also

- [var dataCell: Any](nstablecolumn/datacell.md)
  The cell prototype used by the table column to draw individual cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/datacell(forrow:))*