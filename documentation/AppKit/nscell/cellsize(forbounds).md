# cellSize(forBounds:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the minimum size needed to display the receiver, constraining it to the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func cellSize(forBounds rect: NSRect) -> NSSize
```

```objc
- (NSSize) cellSizeForBounds:(NSRect) rect;
```

#### Discussion

This method takes into account of the size of the image or text within a certain offset determined by the border type of the cell. If the receiver is of text type, the text is resized to fit within `aRect` (as much as `aRect` is within the bounds of the cell).

To support constraint-based layout, when the content of a custom cell changes in such a way that the return value of this method would change, the cell needs to notify its control of the change by calling the control’s [`invalidateIntrinsicContentSize(for:)`](../nscontrol/invalidateintrinsiccontentsize%28for%29.md) method.

## Parameters

- `rect`: The size of the cell, or the size of the `aRect` parameter if the cell is not a text or image cell. If the cell is an image cell but no image has been set, returns `NSZeroSize`.

## See Also

### Determining Cell Size
- [func calcDrawInfo(NSRect)](./calcdrawinfo%28_%29.md)
  Recalculates the cell geometry.
- [var cellSize: NSSize](./cellsize.md)
  The minimum size needed to display the cell.
- [func drawingRect(forBounds: NSRect) -> NSRect](./drawingrect%28forbounds%29.md)
  Returns the rectangle within which the receiver draws itself
- [func imageRect(forBounds: NSRect) -> NSRect](./imagerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its image.
- [func titleRect(forBounds: NSRect) -> NSRect](./titlerect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its title text.
- [var controlSize: NSControl.ControlSize](./controlsize.md)
  The size of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/cellsize(forbounds:))*