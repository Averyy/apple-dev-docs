# draw(at:from:operation:fraction:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Draws all or part of the image at the specified point in the current coordinate system.

**Availability**:
- macOS

## Declaration

```swift
func draw(at point: NSPoint, from fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)
```

```objc
- (void) drawAtPoint:(NSPoint) point fromRect:(NSRect) fromRect operation:(NSCompositingOperation) op fraction:(CGFloat) delta;
```

#### Discussion

The image content is drawn at its current resolution and is not scaled unless the CTM of the current coordinate system itself contains a scaling factor. The image is otherwise positioned and oriented using the current coordinate system.

## Parameters

- `point`: The location in the current coordinate system at which to draw the image.
- `fromRect`: The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle must be specified using the image’s own coordinate system.
- `op`: The compositing operation to use when drawing the image. For details, see [`NSCompositingOperation`](../../AppKit/nscompositingoperation.md).
- `delta`: The opacity of the image, specified as a value from `0.0` to `1.0`. Specifying a value of `0.0` draws the image as fully transparent while a value of `1.0` draws the image as fully opaque. Values greater than `1.0` are interpreted as `1.0`.

## See Also

### Drawing Images
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28in,from,operation,fraction%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/draw(at:from:operation:fraction:))*