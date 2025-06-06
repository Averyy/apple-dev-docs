# setState(_:atRow:column:)

**Framework**: AppKit  
**Kind**: method

Sets the state of the cell at specified location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setState(_ value: Int, atRow row: Int, column col: Int)
```

#### Discussion

For radio-mode matrices, if `value` is nonzero the specified cell is selected before its state is set to `value`. If `value` is 0 and the receiver is a radio-mode matrix, the currently selected cell is deselected (providing that empty selection is allowed).

This method redraws the affected cell.

## Parameters

- `value`: The value to assign to the cell.
- `row`: The row in which the cell is located.
- `col`: The column in which the cell is located.

## See Also

- [var state: NSControl.StateValue](nscell/state.md)
  The cell’s current state.
- [func selectCell(atRow: Int, column: Int)](nsmatrix/selectcell(atrow:column:).md)
  Selects the cell at the specified row and column within the receiver.
- [var allowsEmptySelection: Bool](nsmatrix/allowsemptyselection.md)
  A Boolean that indicates whether a radio-mode matrix supports an empty selection.
- [func setToolTip(String?, for: NSCell)](nsmatrix/settooltip(_:for:).md)
  Sets the tooltip for the cell.
- [func toolTip(for: NSCell) -> String?](nsmatrix/tooltip(for:).md)
  Returns the tooltip for the specified cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/setstate(_:atrow:column:))*