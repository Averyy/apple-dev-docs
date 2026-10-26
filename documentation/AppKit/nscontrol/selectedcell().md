# selectedCell()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s selected cell.

**Availability**:
- macOS

## Declaration

```swift
func selectedCell() -> NSCell?
```

```objc
- (NSCell *) selectedCell;
```

#### Return Value

The selected cell object.

#### Discussion

The default implementation of this method simply returns the control’s associated cell (or `nil` if no cell has been set). Subclasses of `NSControl` that manage multiple cells (such as `NSMatrix` and `NSForm`) must override this method to return the cell selected by the user.

## See Also

### Related Documentation
- [var cell: NSCell?](./cell.md)
  The receiver’s cell object.
### Deprecated methods
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/selectedcell())*