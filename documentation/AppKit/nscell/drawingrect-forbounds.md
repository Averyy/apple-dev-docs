# drawingRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle within which the receiver draws itself

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawingRect(forBounds rect: NSRect) -> NSRect
```

#### Return Value

The rectangle in which the receiver draws itself. This rectangle is slightly inset from the one in `theRect`.

## Parameters

- `rect`: The bounding rectangle of the receiver.

## See Also

- [func calcSize()](nscontrol/calcsize.md)
  Recomputes any internal sizing information for the receiver, if necessary.
- [func calcDrawInfo(NSRect)](nscell/calcdrawinfo(_:).md)
  Recalculates the cell geometry.
- [var cellSize: NSSize](nscell/cellsize.md)
  The minimum size needed to display the cell.
- [func cellSize(forBounds: NSRect) -> NSSize](nscell/cellsize(forbounds:).md)
  Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.
- [func imageRect(forBounds: NSRect) -> NSRect](nscell/imagerect(forbounds:).md)
  Returns the rectangle in which the receiver draws its image.
- [func titleRect(forBounds: NSRect) -> NSRect](nscell/titlerect(forbounds:).md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](nscell/controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/drawingrect(forbounds:))*