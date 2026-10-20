# titleRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle in which the receiver draws its title text.

**Availability**:
- macOS

## Declaration

```swift
func titleRect(forBounds rect: NSRect) -> NSRect
```

```objc
- (NSRect) titleRectForBounds:(NSRect) rect;
```

#### Return Value

The rectangle in which the receiver draws its title text.

#### Discussion

If the receiver is a text-type cell, this method resizes the drawing rectangle for the title (`theRect`) inward by a small offset to accommodate the cell border. If the receiver is not a text-type cell, the method does nothing.

## Parameters

- `rect`: The bounding rectangle of the receiver.

## See Also

### Determining Cell Size
- [func calcDrawInfo(NSRect)](./calcdrawinfo%28_%29.md)
  Recalculates the cell geometry.
- [var cellSize: NSSize](./cellsize.md)
  The minimum size needed to display the cell.
- [func cellSize(forBounds: NSRect) -> NSSize](./cellsize%28forbounds%29.md)
  Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.
- [func drawingRect(forBounds: NSRect) -> NSRect](./drawingrect%28forbounds%29.md)
  Returns the rectangle within which the receiver draws itself
- [func imageRect(forBounds: NSRect) -> NSRect](./imagerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its image.
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/titlerect(forbounds:))*