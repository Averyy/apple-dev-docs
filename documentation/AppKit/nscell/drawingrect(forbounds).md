# drawingRect(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle within which the receiver draws itself

**Availability**:
- macOS

## Declaration

```swift
func drawingRect(forBounds rect: NSRect) -> NSRect
```

```objc
- (NSRect) drawingRectForBounds:(NSRect) rect;
```

## Return Value

The rectangle in which the receiver draws itself. This rectangle is slightly inset from the one in `theRect`.

## Parameters

- `rect`: The bounding rectangle of the receiver.

## See Also

### Related Documentation
- [func calcSize()](../nscontrol/calcsize%28%29.md)
  Recomputes any internal sizing information for the receiver, if necessary.
### Determining Cell Size
- [func calcDrawInfo(NSRect)](./calcdrawinfo%28_%29.md)
  Recalculates the cell geometry.
- [var cellSize: NSSize](./cellsize.md)
  The minimum size needed to display the cell.
- [func cellSize(forBounds: NSRect) -> NSSize](./cellsize%28forbounds%29.md)
  Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.
- [func imageRect(forBounds: NSRect) -> NSRect](./imagerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its image.
- [func titleRect(forBounds: NSRect) -> NSRect](./titlerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/drawingrect(forbounds:))*