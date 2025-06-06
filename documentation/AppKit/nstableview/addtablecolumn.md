# addTableColumn(_:)

**Framework**: AppKit  
**Kind**: method

Adds the specified column as the last column of the table view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addTableColumn(_ tableColumn: NSTableColumn)
```

## Parameters

- `tableColumn`: The column to add to the table view.

## See Also

- [func sizeLastColumnToFit()](nstableview/sizelastcolumntofit.md)
  Resizes the last column so the table view fits exactly within its enclosing clip view.
- [func removeTableColumn(NSTableColumn)](nstableview/removetablecolumn(_:).md)
  Removes the specified column from the table view.
- [func moveColumn(Int, toColumn: Int)](nstableview/movecolumn(_:tocolumn:).md)
  Moves the column and heading at the specified index to the new specified index.
- [var tableColumns: [NSTableColumn]](nstableview/tablecolumns.md)
  An array containing the current table column objects.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](nstableview/column(withidentifier:).md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](nstableview/tablecolumn(withidentifier:).md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/addtablecolumn(_:))*