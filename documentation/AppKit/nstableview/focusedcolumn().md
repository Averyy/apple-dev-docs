# focusedColumn()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the currently focused column.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

> **Deprecated**: Use a view-based table view and observe the window’s first responder.

## Declaration

```swift
func focusedColumn() -> Int
```

```objc
- (NSInteger) focusedColumn;
```

#### Return Value

The index of the column, or -1 if there is no focused column

#### Discussion

The focus interaction will always be on the [`selectedRow`](./selectedrow.md) of the table. If the [`selectedRow`](./selectedrow.md) is a full width cell, then `focusedColumn` will return `1` when focused.

> **Note**:  This method is not applicable for [`NSView`](../nsview.md)-based table views. Instead, the view that has focus will be the [`firstResponder`](../nswindow/firstresponder.md).

## See Also

### Deprecated methods
- [func setFocusedColumn(Int)](./setfocusedcolumn%28_%29.md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](./shouldfocuscell%28_,atcolumn,row%29.md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](./performclickoncell%28atcolumn,row%29.md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](./preparedcell%28atcolumn,row%29.md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/focusedcolumn())*