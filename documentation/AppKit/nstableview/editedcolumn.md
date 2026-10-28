# editedColumn

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the column being edited.

**Availability**:
- macOS

## Declaration

```swift
var editedColumn: Int { get }
```

```objc
@property (readonly) NSInteger editedColumn;
```

## Return Value

If sent during [`editColumn(_:row:with:select:)`](./editcolumn%28_,row,with,select%29.md), the index in the [`tableColumns`](./tablecolumns.md) array of the column being edited; otherwise `–1`.

## Discussion

This property does not apply to view-based table views. In a view-based table view, the views are responsible for their own editing behavior. For other tables, the value reflects the index of the column being edited or `–1` when there is no editing session in progress or when the currently edited row is a “full width” row.

## See Also

### Editing Cells
- [func editColumn(Int, row: Int, with: NSEvent?, select: Bool)](./editcolumn%28_,row,with,select%29.md)
  Edits the cell at the specified column and row using the specified event and selection behavior.
- [var editedRow: Int](./editedrow.md)
  The index of the row being edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/editedcolumn)*