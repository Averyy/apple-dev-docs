# setToolTip(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the tooltip for the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setToolTip(_ toolTipString: String?, for cell: NSCell)
```

## Parameters

- `toolTipString`: The string to use as the cell’s tooltip (or help tag).
- `cell`: The cell to which to assign the tooltip.

## See Also

- [func setState(Int, atRow: Int, column: Int)](nsmatrix/setstate(_:atrow:column:).md)
  Sets the state of the cell at specified location.
- [func toolTip(for: NSCell) -> String?](nsmatrix/tooltip(for:).md)
  Returns the tooltip for the specified cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/settooltip(_:for:))*