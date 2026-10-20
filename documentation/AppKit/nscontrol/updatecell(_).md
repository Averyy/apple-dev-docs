# updateCell(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks the specified cell as in need of redrawing.

**Availability**:
- macOS

## Declaration

```swift
func updateCell(_ cell: NSCell)
```

```objc
- (void) updateCell:(NSCell *) cell;
```

#### Discussion

If the cell currently has the focus, this method updates the cell’s focus ring; otherwise, the entire cell is marked as needing redisplay. The cell is redrawn during the next update cycle.

## Parameters

- `cell`: The cell to redraw.

## See Also

### Deprecated methods
- [func selectedCell() -> NSCell?](./selectedcell%28%29.md)
  Returns the receiver’s selected cell.
- [func selectedTag() -> Int](./selectedtag%28%29.md)
  Returns the tag of the receiver’s selected cell.
- [func setNeedsDisplay()](./setneedsdisplay%28%29.md)
  Marks the receiver as needing redisplay (assuming automatic display is enabled).
- [func calcSize()](./calcsize%28%29.md)
  Recomputes any internal sizing information for the receiver, if necessary.
- [func selectCell(NSCell)](./selectcell%28_%29.md)
  Selects the specified cell and redraws the control as needed.
- [func drawCell(NSCell)](./drawcell%28_%29.md)
  Draws the specified cell, as long as it belongs to the receiver.
- [func drawCellInside(NSCell)](./drawcellinside%28_%29.md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
- [func updateCellInside(NSCell)](./updatecellinside%28_%29.md)
  Marks the inside of the specified cell as in need of redrawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/updatecell(_:))*