# titleRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle in which the receiver draws its title text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func titleRect(forBounds rect: NSRect) -> NSRect
```

#### Return Value

The rectangle in which the receiver draws its title text.

#### Discussion

If the receiver is a text-type cell, this method resizes the drawing rectangle for the title (`theRect`) inward by a small offset to accommodate the cell border. If the receiver is not a text-type cell, the method does nothing.

## Parameters

- `rect`: The bounding rectangle of the receiver.

## See Also

- [func calcDrawInfo(NSRect)](nscell/calcdrawinfo(_:).md)
  Recalculates the cell geometry.
- [var cellSize: NSSize](nscell/cellsize.md)
  The minimum size needed to display the cell.
- [func cellSize(forBounds: NSRect) -> NSSize](nscell/cellsize(forbounds:).md)
  Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.
- [func drawingRect(forBounds: NSRect) -> NSRect](nscell/drawingrect(forbounds:).md)
  Returns the rectangle within which the receiver draws itself
- [func imageRect(forBounds: NSRect) -> NSRect](nscell/imagerect(forbounds:).md)
  Returns the rectangle in which the receiver draws its image.
- [var controlSize: NSControl.ControlSize](nscell/controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/titlerect(forbounds:))*