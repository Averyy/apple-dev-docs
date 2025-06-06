# drawCell(_:)

**Framework**: AppKit  
**Kind**: method

Draws the specified cell, as long as it belongs to the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawCell(_ cell: NSCell)
```

#### Discussion

This method is provided primarily to support a consistent set of methods between `NSControl` objects with single and multiple cells, because a control with multiple cells needs to be able to draw individual cells.

## Parameters

- `cell`: The cell to draw. If the cell does not belong to the receiver, this method does nothing.

## See Also

- [func selectedCell() -> NSCell?](nscontrol/selectedcell.md)
  Returns the receiver’s selected cell.
- [func selectedTag() -> Int](nscontrol/selectedtag.md)
  Returns the tag of the receiver’s selected cell.
- [func setNeedsDisplay()](nscontrol/setneedsdisplay.md)
  Marks the receiver as needing redisplay (assuming automatic display is enabled).
- [func calcSize()](nscontrol/calcsize.md)
  Recomputes any internal sizing information for the receiver, if necessary.
- [func selectCell(NSCell)](nscontrol/selectcell(_:).md)
  Selects the specified cell and redraws the control as needed.
- [func drawCellInside(NSCell)](nscontrol/drawcellinside(_:).md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
- [func updateCell(NSCell)](nscontrol/updatecell(_:).md)
  Marks the specified cell as in need of redrawing.
- [func updateCellInside(NSCell)](nscontrol/updatecellinside(_:).md)
  Marks the inside of the specified cell as in need of redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/drawcell(_:))*