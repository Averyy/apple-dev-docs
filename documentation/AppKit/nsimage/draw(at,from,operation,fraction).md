# draw(at:from:operation:fraction:)

**Framework**: AppKit  
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

## Discussion

The image content is drawn at its current resolution and is not scaled unless the CTM of the current coordinate system itself contains a scaling factor. The image is otherwise positioned and oriented using the current coordinate system.

Unlike the [`compositeToPoint:fromRect:operation:`](./compositetopoint_fromrect_operation_.md) and  [`compositeToPoint:fromRect:operation:fraction:`](./compositetopoint_fromrect_operation_fraction_.md) methods, this method checks the rectangle you pass to the `srcRect` parameter and makes sure it does not lie outside the image bounds.

## Parameters

- `point`: The location in the current coordinate system at which to draw the image.
- `fromRect`: The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle are specified in the image’s own coordinate system. If you pass in `NSZeroRect`, the entire image is drawn.
- `op`: The compositing operation to use when drawing the image. See the [`NSCompositingOperation`](../nscompositingoperation.md) constants.
- `delta`: The opacity of the image, specified as a value from 0.0 to 1.0. Specifying a value of 0.0 draws the image as fully transparent while a value of 1.0 draws the image as fully opaque. Values greater than 1.0 are interpreted as 1.0.

## See Also

### Drawing Images
- [func draw(in: NSRect)](./draw%28in%29.md)
  Draws the image in the specified rectangle.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28in,from,operation,fraction%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?)](./draw%28in,from,operation,fraction,respectflipped,hints%29.md)
  Draws all or part of the image in the specified rectangle respecting the hints and the orientation of the current coordinate system.
- [func drawRepresentation(NSImageRep, in: NSRect) -> Bool](./drawrepresentation%28_,in%29.md)
  Draws the image using the specified image representation object.
- [enum NSCompositingOperation](../nscompositingoperation.md)
  Constants that describe compositing operators in terms of source and destination images, each having an opaque and transparent region.
### Related Documentation
- [- dissolveToPoint:fraction:](./dissolvetopoint_fraction_.md)
  Composites the entire image to the specified location using the source-over operator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/draw(at:from:operation:fraction:))*