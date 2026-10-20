# calcDrawInfo(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Recalculates the cell geometry.

**Availability**:
- macOS

## Declaration

```swift
func calcDrawInfo(_ rect: NSRect)
```

```objc
- (void) calcDrawInfo:(NSRect) rect;
```

#### Discussion

Objects (such as controls) that manage `NSCell` objects generally maintain a flag that informs them if any of their cells have been modified in such a way that the location or size of the cell should be recomputed. If so, [`calcSize()`](../nscontrol/calcsize%28%29.md) method of `NSControl` is automatically invoked prior to the display of the cell, and that method invokes the [`calcDrawInfo(_:)`](./calcdrawinfo%28_%29.md) method of the cell.

The default implementation of this method does nothing.

## Parameters

- `rect`: The reference rectangle to use when calculating the cell information.

## See Also

### Determining Cell Size
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
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/calcdrawinfo(_:))*