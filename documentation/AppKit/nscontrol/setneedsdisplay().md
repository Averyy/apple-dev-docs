# setNeedsDisplay()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks the receiver as needing redisplay (assuming automatic display is enabled).

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Set the needsDisplay property to YES instead

## Declaration

```swift
func setNeedsDisplay()
```

```objc
- (void) setNeedsDisplay;
```

## Discussion

This method also recalculates the dimensions of the control as needed.

## See Also

### Related Documentation
- [var needsDisplay: Bool](../nsview/needsdisplay.md)
  A Boolean value that determines whether the view needs to be redrawn before being displayed.
### Deprecated methods
- [func selectedCell() -> NSCell?](./selectedcell%28%29.md)
  Returns the receiver’s selected cell.
- [func selectedTag() -> Int](./selectedtag%28%29.md)
  Returns the tag of the receiver’s selected cell.
- [func calcSize()](./calcsize%28%29.md)
  Recomputes any internal sizing information for the receiver, if necessary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/setneedsdisplay())*