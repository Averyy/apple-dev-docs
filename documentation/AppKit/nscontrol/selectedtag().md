# selectedTag()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the tag of the receiver’s selected cell.

**Availability**:
- macOS

## Declaration

```swift
func selectedTag() -> Int
```

```objc
- (NSInteger) selectedTag;
```

#### Return Value

The tag of the selected cell, or `-1` if no cell is selected.

#### Discussion

When you set the tag of a control with a single cell in Interface Builder, it sets the tags of both the control and the cell with the same value as a convenience.

## See Also

### Related Documentation
- [var tag: Int](./tag.md)
  The tag identifying the receiver (not the tag of the receiver’s cell).
### Deprecated methods
- [func selectedCell() -> NSCell?](./selectedcell%28%29.md)
  Returns the receiver’s selected cell.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/selectedtag())*