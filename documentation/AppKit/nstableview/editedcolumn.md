# editedColumn

**Framework**: AppKit  
**Kind**: property

The index of the column being edited.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var editedColumn: Int { get }
```

#### Return Value

If sent during [`editColumn(_:row:with:select:)`](nstableview/editcolumn(_:row:with:select:).md), the index in the [`tableColumns`](nstableview/tablecolumns.md) array of the column being edited; otherwise `–1`.

#### Discussion

This property does not apply to view-based table views. In a view-based table view, the views are responsible for their own editing behavior. For other tables, the value reflects the index of the column being edited or `–1` when there is no editing session in progress or when the currently edited row is a “full width” row.

## See Also

- [func editColumn(Int, row: Int, with: NSEvent?, select: Bool)](nstableview/editcolumn(_:row:with:select:).md)
  Edits the cell at the specified column and row using the specified event and selection behavior.
- [var editedRow: Int](nstableview/editedrow.md)
  The index of the row being edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/editedcolumn)*