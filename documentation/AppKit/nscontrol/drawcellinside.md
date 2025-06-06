# drawCellInside(_:)

**Framework**: AppKit  
**Kind**: method

Draws the inside of the receiver’s cell (the area within the bezel or border)

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawCellInside(_ cell: NSCell)
```

#### Discussion

If the receiver is transparent, the method causes the superview to draw itself. This method invokes the  [`drawInterior(withFrame:in:)`](nscell/drawinterior(withframe:in:).md) method of NSCell. This method has no effect on controls (such as `NSMatrix` and `NSForm`) that have multiple cells.

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
- [func drawCell(NSCell)](nscontrol/drawcell(_:).md)
  Draws the specified cell, as long as it belongs to the receiver.
- [func updateCell(NSCell)](nscontrol/updatecell(_:).md)
  Marks the specified cell as in need of redrawing.
- [func updateCellInside(NSCell)](nscontrol/updatecellinside(_:).md)
  Marks the inside of the specified cell as in need of redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/drawcellinside(_:))*