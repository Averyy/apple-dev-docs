# controlSize

**Framework**: AppKit  
**Kind**: property

The size of the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var controlSize: NSControl.ControlSize { get set }
```

#### Discussion

Use this property to change the rendered size of the cell and its control. For a list of possible values, see [`NSControl.ControlSize`](nscontrol/controlsize-swift.enum.md).

Changing the cell’s control size does not change the font used by the cell. Use the [`systemFontSize(for:)`](nsfont/systemfontsize(for:).md) class method of [`NSFont`](nsfont.md) to obtain an appropriate font based on the new control size.

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
- [func titleRect(forBounds: NSRect) -> NSRect](nscell/titlerect(forbounds:).md)
  Returns the rectangle in which the receiver draws its title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/controlsize)*