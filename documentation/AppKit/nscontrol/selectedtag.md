# selectedTag()

**Framework**: AppKit  
**Kind**: method

Returns the tag of the receiver’s selected cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectedTag() -> Int
```

#### Return Value

The tag of the selected cell, or `-1` if no cell is selected.

#### Discussion

When you set the tag of a control with a single cell in Interface Builder, it sets the tags of both the control and the cell with the same value as a convenience.

## See Also

- [var tag: Int](nscontrol/tag.md)
  The tag identifying the receiver (not the tag of the receiver’s cell).
- [func selectedCell() -> NSCell?](nscontrol/selectedcell.md)
  Returns the receiver’s selected cell.
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
- [func updateCell(NSCell)](nscontrol/updatecell(_:).md)
  Marks the specified cell as in need of redrawing.
- [func updateCellInside(NSCell)](nscontrol/updatecellinside(_:).md)
  Marks the inside of the specified cell as in need of redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/selectedtag())*