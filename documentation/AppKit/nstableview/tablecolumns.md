# tableColumns

**Framework**: AppKit  
**Kind**: property

An array containing the current table column objects.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var tableColumns: [NSTableColumn] { get }
```

#### Discussion

This property contains an array of [`NSTableColumn`](nstablecolumn.md) objects corresponding to the columns in the table. This array contains all columns, including those that are currently hidden.

## See Also

- [func addTableColumn(NSTableColumn)](nstableview/addtablecolumn(_:).md)
  Adds the specified column as the last column of the table view.
- [func removeTableColumn(NSTableColumn)](nstableview/removetablecolumn(_:).md)
  Removes the specified column from the table view.
- [func moveColumn(Int, toColumn: Int)](nstableview/movecolumn(_:tocolumn:).md)
  Moves the column and heading at the specified index to the new specified index.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](nstableview/column(withidentifier:).md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](nstableview/tablecolumn(withidentifier:).md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/tablecolumns)*