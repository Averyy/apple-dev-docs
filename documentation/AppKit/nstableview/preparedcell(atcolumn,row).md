# preparedCell(atColumn:row:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

> **Deprecated**: Use a view-based table view and the [`view(atColumn:row:makeIfNecessary:)`](./view%28atcolumn,row,makeifnecessary%29.md) method.

## Declaration

```swift
func preparedCell(atColumn column: Int, row: Int) -> NSCell?
```

```objc
- (NSCell *) preparedCellAtColumn:(NSInteger) column row:(NSInteger) row;
```

#### Return Value

New [`NSCell`](../nscell.md) subclass instance to use for the specified `row` and `column`. The value for the cell is correctly set, and the delegate method [`tableView(_:willDisplayCell:for:row:)`](../nstableviewdelegate/tableview%28_,willdisplaycell,for,row%29.md) will have been called.

#### Discussion

You can override this method to do any additional cell set up that is required, or invoke it to retrieve a cell that has its contents configured for the specified `column` and `row`.

> **Note**:  This method is only available to [`NSCell`](../nscell.md)-based table views.

## Parameters

- `column`: The index in the [`tableColumns`](./tablecolumns.md) array for which to return the appropriate cell.
- `row`: The row index for which to return the appropriate cell.

## See Also

### Deprecated methods
- [func focusedColumn() -> Int](./focusedcolumn%28%29.md)
  Returns the currently focused column.
- [func setFocusedColumn(Int)](./setfocusedcolumn%28_%29.md)
  Sets the currently focused column to the specified index.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](./shouldfocuscell%28_,atcolumn,row%29.md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](./performclickoncell%28atcolumn,row%29.md)
  Performs a click action on the cell at the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/preparedcell(atcolumn:row:))*