# toolTip(for:)

**Framework**: AppKit  
**Kind**: method

Returns the tooltip for the specified cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func toolTip(for cell: NSCell) -> String?
```

#### Return Value

The string used as the cell’s tooltip.

## Parameters

- `cell`: The cell for which to return the tooltip.

## See Also

- [func setState(Int, atRow: Int, column: Int)](nsmatrix/setstate(_:atrow:column:).md)
  Sets the state of the cell at specified location.
- [func setToolTip(String?, for: NSCell)](nsmatrix/settooltip(_:for:).md)
  Sets the tooltip for the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/tooltip(for:))*