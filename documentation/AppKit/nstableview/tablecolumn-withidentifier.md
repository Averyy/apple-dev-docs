# tableColumn(withIdentifier:)

**Framework**: AppKit  
**Kind**: method

Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tableColumn(withIdentifier identifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?
```

#### Return Value

The `NSTableColumn` object for the first column whose identifier is equal to `anObject` (when compared using `isEqual:`), or `nil` if no columns are found with the specified identifier.

## Parameters

- `identifier`: A column identifier.

## See Also

- [func addTableColumn(NSTableColumn)](nstableview/addtablecolumn(_:).md)
  Adds the specified column as the last column of the table view.
- [func removeTableColumn(NSTableColumn)](nstableview/removetablecolumn(_:).md)
  Removes the specified column from the table view.
- [func moveColumn(Int, toColumn: Int)](nstableview/movecolumn(_:tocolumn:).md)
  Moves the column and heading at the specified index to the new specified index.
- [var tableColumns: [NSTableColumn]](nstableview/tablecolumns.md)
  An array containing the current table column objects.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](nstableview/column(withidentifier:).md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/tablecolumn(withidentifier:))*