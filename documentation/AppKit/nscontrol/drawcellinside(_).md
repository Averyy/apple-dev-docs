# drawCellInside(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the inside of the receiver’s cell (the area within the bezel or border)

**Availability**:
- macOS

## Declaration

```swift
func drawCellInside(_ cell: NSCell)
```

```objc
- (void) drawCellInside:(NSCell *) cell;
```

#### Discussion

If the receiver is transparent, the method causes the superview to draw itself. This method invokes the  [`drawInterior(withFrame:in:)`](../nscell/drawinterior%28withframe,in%29.md) method of NSCell. This method has no effect on controls (such as `NSMatrix` and `NSForm`) that have multiple cells.

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
- [func drawCell(NSCell)](./drawcell%28_%29.md)
  Draws the specified cell, as long as it belongs to the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/drawcellinside(_:))*