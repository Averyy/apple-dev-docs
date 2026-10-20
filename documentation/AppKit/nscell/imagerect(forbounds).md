# imageRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle in which the receiver draws its image.

**Availability**:
- macOS

## Declaration

```swift
func imageRect(forBounds rect: NSRect) -> NSRect
```

```objc
- (NSRect) imageRectForBounds:(NSRect) rect;
```

#### Return Value

The rectangle in which the receiver draws its image. This rectangle is slightly offset from the one in `theRect`.

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
- [func titleRect(forBounds: NSRect) -> NSRect](./titlerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/imagerect(forbounds:))*