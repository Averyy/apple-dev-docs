# updateCell(_:)

**Framework**: AppKit  
**Kind**: method

Marks the specified cell as in need of redrawing.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func updateCell(_ cell: NSCell)
```

#### Discussion

If the cell currently has the focus, this method updates the cell’s focus ring; otherwise, the entire cell is marked as needing redisplay. The cell is redrawn during the next update cycle.

## Parameters

- `cell`: The cell to redraw.

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
- [func drawCell(NSCell)](nscontrol/drawcell(_:).md)
  Draws the specified cell, as long as it belongs to the receiver.
- [func drawCellInside(NSCell)](nscontrol/drawcellinside(_:).md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
- [func updateCellInside(NSCell)](nscontrol/updatecellinside(_:).md)
  Marks the inside of the specified cell as in need of redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/updatecell(_:))*