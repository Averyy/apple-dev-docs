# cellSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum size needed to display the cell.

**Availability**:
- macOS

## Declaration

```swift
var cellSize: NSSize { get }
```

```objc
@property (readonly) NSSize cellSize;
```

## Discussion

This property contains the smallest cell size (in points) required to draw its contents. If the cell is not a text or image cell, the cell size is set to (`10000`, `10000`). If an image cell does not yet have an associated image, the cell size is [`NSZeroSize`](../../Foundation/nszerosize.md).This method takes into account of the size of the image or text in the cell along with any margin areas required by the cell’s border, if any.

## See Also

### Determining Cell Size
- [func calcDrawInfo(NSRect)](./calcdrawinfo%28_%29.md)
  Recalculates the cell geometry.
- [func cellSize(forBounds: NSRect) -> NSSize](./cellsize%28forbounds%29.md)
  Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.
- [func drawingRect(forBounds: NSRect) -> NSRect](./drawingrect%28forbounds%29.md)
  Returns the rectangle within which the receiver draws itself
- [func imageRect(forBounds: NSRect) -> NSRect](./imagerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its image.
- [func titleRect(forBounds: NSRect) -> NSRect](./titlerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/cellsize)*