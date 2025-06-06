# calcSize()

**Framework**: AppKit  
**Kind**: method

Recomputes any internal sizing information for the receiver, if necessary.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func calcSize()
```

#### Discussion

This method uses the [`calcDrawInfo(_:)`](nscell/calcdrawinfo(_:).md) method of its cell to perform the calculations. Most controls maintain a flag that informs them if any of their cells have been modified in such a way that the location or size of the cell should be recomputed. If such a modification happens, this method is automatically invoked before the control is displayed. You should never need to invoke it yourself.

## See Also

- [func sizeToFit()](nscontrol/sizetofit.md)
  Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.
- [func selectedCell() -> NSCell?](nscontrol/selectedcell.md)
  Returns the receiver’s selected cell.
- [func selectedTag() -> Int](nscontrol/selectedtag.md)
  Returns the tag of the receiver’s selected cell.
- [func setNeedsDisplay()](nscontrol/setneedsdisplay.md)
  Marks the receiver as needing redisplay (assuming automatic display is enabled).
- [func selectCell(NSCell)](nscontrol/selectcell(_:).md)
  Selects the specified cell and redraws the control as needed.
- [func drawCell(NSCell)](nscontrol/drawcell(_:).md)
  Draws the specified cell, as long as it belongs to the receiver.
- [func drawCellInside(NSCell)](nscontrol/drawcellinside(_:).md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
- [func updateCell(NSCell)](nscontrol/updatecell(_:).md)
  Marks the specified cell as in need of redrawing.
- [func updateCellInside(NSCell)](nscontrol/updatecellinside(_:).md)
  Marks the inside of the specified cell as in need of redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/calcsize())*