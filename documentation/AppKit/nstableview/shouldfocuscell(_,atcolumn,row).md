# shouldFocusCell(_:atColumn:row:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the fully prepared cell at the specified row and column can be made the focused cell.

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: Use a view-based table view and observe the window’s first responder.

## Declaration

```swift
func shouldFocusCell(_ cell: NSCell, atColumn column: Int, row: Int) -> Bool
```

```objc
- (BOOL) shouldFocusCell:(NSCell *) cell atColumn:(NSInteger) column row:(NSInteger) row;
```

#### Return Value

[`true`](../../Swift/true.md) if the cell can be made the focused cell, otherwise [`false`](../../Swift/false.md).

#### Discussion

By default, only cells that are enabled can be focused. In addition, if the cell is an [`NSTextFieldCell`](../nstextfieldcell.md), it can only be focused if it is selectable or editable, and the table view delegate responds [`true`](../../Swift/true.md) to -[`tableView(_:shouldEdit:row:)`](../nstableviewdelegate/tableview%28_,shouldedit,row%29.md).

Subclasses can override this to further control which cells can and can’t be made focused.

> **Note**:  This method is only applicable to [`NSCell`](../nscell.md)-based table views.

## Parameters

- `cell`: The prepared cell to be focused upon.
- `column`: The column of the cell.
- `row`: The row of the cell.

## See Also

### Deprecated methods
- [func focusedColumn() -> Int](./focusedcolumn%28%29.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](./setfocusedcolumn%28_%29.md)
  Sets the currently focused column to the specified index.
- [func performClickOnCell(atColumn: Int, row: Int)](./performclickoncell%28atcolumn,row%29.md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](./preparedcell%28atcolumn,row%29.md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/shouldfocuscell(_:atcolumn:row:))*