# imageRect(forBounds:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle in which the receiver draws its image.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func imageRect(forBounds rect: NSRect) -> NSRect
```

#### Return Value

The rectangle in which the receiver draws its image. This rectangle is slightly offset from the one in `theRect`.

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
- [func titleRect(forBounds: NSRect) -> NSRect](nscell/titlerect(forbounds:).md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](nscell/controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/imagerect(forbounds:))*