# drawCell(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the specified cell, as long as it belongs to the receiver.

**Availability**:
- macOS

## Declaration

```swift
func drawCell(_ cell: NSCell)
```

```objc
- (void) drawCell:(NSCell *) cell;
```

## Discussion

This method is provided primarily to support a consistent set of methods between `NSControl` objects with single and multiple cells, because a control with multiple cells needs to be able to draw individual cells.

## Parameters

- `cell`: The cell to draw. If the cell does not belong to the receiver, this method does nothing.

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
- [func drawCellInside(NSCell)](./drawcellinside%28_%29.md)
  Draws the inside of the receiver’s cell (the area within the bezel or border)
- [func updateCell(NSCell)](./updatecell%28_%29.md)
  Marks the specified cell as in need of redrawing.
- [func updateCellInside(NSCell)](./updatecellinside%28_%29.md)
  Marks the inside of the specified cell as in need of redrawing.
- [- controlTextDidBeginEditing:](../../ObjectiveC/nsobject-swift.class/controltextdidbeginediting_.md)
  Sent when a control with editable text begins an editing session.
- [- controlTextDidChange:](../../ObjectiveC/nsobject-swift.class/controltextdidchange_.md)
  Sent when the text in the receiving control changes.
- [- controlTextDidEndEditing:](../../ObjectiveC/nsobject-swift.class/controltextdidendediting_.md)
  Sent when a control with editable text ends an editing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/drawcell(_:))*