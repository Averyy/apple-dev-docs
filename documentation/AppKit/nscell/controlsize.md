# controlSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the cell.

**Availability**:
- macOS

## Declaration

```swift
var controlSize: NSControl.ControlSize { get set }
```

```objc
@property NSControlSize controlSize;
```

## Discussion

Use this property to change the rendered size of the cell and its control. For a list of possible values, see [`NSControl.ControlSize`](../nscontrol/controlsize-swift.enum.md).

Changing the cell’s control size does not change the font used by the cell. Use the [`systemFontSize(for:)`](../nsfont/systemfontsize%28for%29.md) class method of [`NSFont`](../nsfont.md) to obtain an appropriate font based on the new control size.

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
- [func titleRect(forBounds: NSRect) -> NSRect](./titlerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its title text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/controlsize)*