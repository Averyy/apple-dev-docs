# calcDrawInfo(_:)

**Framework**: AppKit  
**Kind**: method

Recalculates the cell geometry.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func calcDrawInfo(_ rect: NSRect)
```

#### Discussion

Objects (such as controls) that manage `NSCell` objects generally maintain a flag that informs them if any of their cells have been modified in such a way that the location or size of the cell should be recomputed. If so, [`calcSize()`](nscontrol/calcsize().md) method of `NSControl` is automatically invoked prior to the display of the cell, and that method invokes the [`calcDrawInfo(_:)`](nscell/calcdrawinfo(_:).md) method of the cell.

The default implementation of this method does nothing.

## Parameters

- `rect`: The reference rectangle to use when calculating the cell information.

## See Also

- [var cellSize: NSSize](nscell/cellsize.md)
  The minimum size needed to display the cell.
- [func cellSize(forBounds: NSRect) -> NSSize](nscell/cellsize(forbounds:).md)
  Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.
- [func drawingRect(forBounds: NSRect) -> NSRect](nscell/drawingrect(forbounds:).md)
  Returns the rectangle within which the receiver draws itself
- [func imageRect(forBounds: NSRect) -> NSRect](nscell/imagerect(forbounds:).md)
  Returns the rectangle in which the receiver draws its image.
- [func titleRect(forBounds: NSRect) -> NSRect](nscell/titlerect(forbounds:).md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](nscell/controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/calcdrawinfo(_:))*