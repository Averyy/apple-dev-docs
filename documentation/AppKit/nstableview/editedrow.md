# editedRow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the row being edited.

**Availability**:
- macOS

## Declaration

```swift
var editedRow: Int { get }
```

```objc
@property (readonly) NSInteger editedRow;
```

#### Discussion

This property does not apply to view-based table views. In a view-based table view, the views are responsible for their own editing behavior. For other tables, the value reflects the index of the row being edited or `–1` when there is no editing session in progress.

## See Also

### Editing Cells
- [func editColumn(Int, row: Int, with: NSEvent?, select: Bool)](./editcolumn%28_,row,with,select%29.md)
  Edits the cell at the specified column and row using the specified event and selection behavior.
- [var editedColumn: Int](./editedcolumn.md)
  The index of the column being edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/editedrow)*