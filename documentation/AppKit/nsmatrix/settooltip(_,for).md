# setToolTip(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the tooltip for the cell.

**Availability**:
- macOS

## Declaration

```swift
func setToolTip(_ toolTipString: String?, for cell: NSCell)
```

```objc
- (void) setToolTip:(NSString *) toolTipString forCell:(NSCell *) cell;
```

## Parameters

- `toolTipString`: The string to use as the cell’s tooltip (or help tag).
- `cell`: The cell to which to assign the tooltip.

## See Also

### Managing Attributes of Individual Cells
- [func setState(Int, atRow: Int, column: Int)](./setstate%28_,atrow,column%29.md)
  Sets the state of the cell at specified location.
- [func toolTip(for: NSCell) -> String?](./tooltip%28for%29.md)
  Returns the tooltip for the specified cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/settooltip(_:for:))*