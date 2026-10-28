# toolTip(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the tooltip for the specified cell.

**Availability**:
- macOS

## Declaration

```swift
func toolTip(for cell: NSCell) -> String?
```

```objc
- (NSString *) toolTipForCell:(NSCell *) cell;
```

## Return Value

The string used as the cell’s tooltip.

## Parameters

- `cell`: The cell for which to return the tooltip.

## See Also

### Managing Attributes of Individual Cells
- [func setState(Int, atRow: Int, column: Int)](./setstate%28_,atrow,column%29.md)
  Sets the state of the cell at specified location.
- [func setToolTip(String?, for: NSCell)](./settooltip%28_,for%29.md)
  Sets the tooltip for the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/tooltip(for:))*