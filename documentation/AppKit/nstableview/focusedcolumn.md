# focusedColumn()

**Framework**: AppKit  
**Kind**: method

Returns the currently focused column.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func focusedColumn() -> Int
```

#### Return Value

The index of the column, or -1 if there is no focused column

#### Discussion

The focus interaction will always be on the [`selectedRow`](nstableview/selectedrow.md) of the table. If the [`selectedRow`](nstableview/selectedrow.md) is a full width cell, then `focusedColumn` will return `1` when focused.

> **Note**:  This method is not applicable for [`NSView`](nsview.md)-based table views. Instead, the view that has focus will be the [`firstResponder`](nswindow/firstresponder.md).

## See Also

- [func setFocusedColumn(Int)](nstableview/setfocusedcolumn(_:).md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](nstableview/shouldfocuscell(_:atcolumn:row:).md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](nstableview/performclickoncell(atcolumn:row:).md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](nstableview/preparedcell(atcolumn:row:).md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/focusedcolumn())*