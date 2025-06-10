# setFocusedColumn(_:)

**Framework**: AppKit  
**Kind**: method

Sets the currently focused column to the specified index.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func setFocusedColumn(_ focusedColumn: Int)
```

#### Discussion

This method will redisplay the previously focused column and (if required) the new `focusedColumn`.

The focused column has a focus ring drawn around the [`selectedRow`](nstableview/selectedrow.md) that intersects with `focusedColumn`.

You should not override this method.

> **Note**:  This method is not applicable for [`NSView`](nsview.md)-based table views.

## Parameters

- `focusedColumn`: The index of the column to focus, or -1 if there should be no focused column.

## See Also

- [func focusedColumn() -> Int](nstableview/focusedcolumn.md)
  Returns the currently focused column.
- [func shouldFocusCell(NSCell, atColumn: Int, row: Int) -> Bool](nstableview/shouldfocuscell(_:atcolumn:row:).md)
  Returns whether the fully prepared cell at the specified row and column can be made the focused cell.
- [func performClickOnCell(atColumn: Int, row: Int)](nstableview/performclickoncell(atcolumn:row:).md)
  Performs a click action on the cell at the specified row and column.
- [func preparedCell(atColumn: Int, row: Int) -> NSCell?](nstableview/preparedcell(atcolumn:row:).md)
  Returns the fully prepared cell that the table view will use for drawing or processing of the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setfocusedcolumn(_:))*