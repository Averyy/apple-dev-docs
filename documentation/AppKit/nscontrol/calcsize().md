# calcSize()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Recomputes any internal sizing information for the receiver, if necessary.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Override -layout instead. This method should never be called

## Declaration

```swift
func calcSize()
```

```objc
- (void) calcSize;
```

## Discussion

This method uses the [`calcDrawInfo(_:)`](../nscell/calcdrawinfo%28_%29.md) method of its cell to perform the calculations. Most controls maintain a flag that informs them if any of their cells have been modified in such a way that the location or size of the cell should be recomputed. If such a modification happens, this method is automatically invoked before the control is displayed. You should never need to invoke it yourself.

## See Also

### Related Documentation
- [func sizeToFit()](./sizetofit%28%29.md)
  Resizes the receiver’s frame so that it’s the minimum size needed to contain its cell.
### Deprecated methods
- [func selectedCell() -> NSCell?](./selectedcell%28%29.md)
  Returns the receiver’s selected cell.
- [func selectedTag() -> Int](./selectedtag%28%29.md)
  Returns the tag of the receiver’s selected cell.
- [func setNeedsDisplay()](./setneedsdisplay%28%29.md)
  Marks the receiver as needing redisplay (assuming automatic display is enabled).
- [func selectCell(NSCell)](./selectcell%28_%29.md)
  Selects the specified cell and redraws the control as needed.
- [func drawCell(NSCell)](./drawcell%28_%29.md)
  Draws the specified cell, as long as it belongs to the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/calcsize())*