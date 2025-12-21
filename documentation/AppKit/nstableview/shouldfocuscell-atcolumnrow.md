# shouldFocusCell(_:atColumn:row:)

**Framework**: AppKit  
**Kind**: method

Returns whether the fully prepared cell at the specified row and column can be made the focused cell.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func shouldFocusCell(_ cell: NSCell, atColumn column: Int, row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the cell can be made the focused cell, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

By default, only cells that are enabled can be focused. In addition, if the cell is an [`NSTextFieldCell`](nstextfieldcell.md), it can only be focused if it is selectable or editable, and the table view delegate responds [`true`](https://developer.apple.com/documentation/Swift/true) to -[`tableView(_:shouldEdit:row:)`](nstableviewdelegate/tableview(_:shouldedit:row:).md).

Subclasses can override this to further control which cells can and can’t be made focused.

> **Note**:  This method is only applicable to [`NSCell`](nscell.md)-based table views.

## Parameters

- `cell`: The prepared cell to be focused upon.
- `column`: The column of the cell.
- `row`: The row of the cell.

## See Also

- [func focusedColumn() -> Int](nstableview/focusedcolumn.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](nstableview/setfocusedcolumn(_:).md)
  Sets the currently focused column to the specified index.
- [func performClickOnCell(atColumn: Int, row: Int)](nstableview/performclickoncell(atcolumn:row:).md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](nstableview/preparedcell(atcolumn:row:).md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/shouldfocuscell(_:atcolumn:row:))*