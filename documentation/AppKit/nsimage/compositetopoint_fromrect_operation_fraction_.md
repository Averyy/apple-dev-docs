# compositeToPoint:fromRect:operation:fraction:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Composites a portion of the image at the specified opacity to the current coordinate system.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`draw(in:from:operation:fraction:)`](./draw%28in,from,operation,fraction%29.md) instead.

## Declaration

```objc
- (void) compositeToPoint:(NSPoint) point fromRect:(NSRect) rect operation:(NSCompositingOperation) operation fraction:(CGFloat) fraction;
```

## Discussion

Behaves the same as [`compositeToPoint:fromRect:operation:`](./compositetopoint_fromrect_operation_.md) except that you can specify the amount of opacity to use when drawing the image.

## Parameters

- `point`: The point at which to draw the image, specified in the current coordinate system.
- `rect`: The portion of the image you want to draw, specified in the image’s coordinate system.
- `operation`: The compositing operation to use when drawing the image to the screen. The supported compositing operations are described in `Constants`.
- `fraction`: The desired opacity of the image, specified as a value between 0.0 and 1.0, with 1.0 representing total opacity. Values larger than 1.0 are interpreted as 1.0. This method always expects to render something, so for values that are equal to or less than 0, this method renders at full opacity.

## See Also

### Related Documentation
- [- dissolveToPoint:fromRect:fraction:](./dissolvetopoint_fromrect_fraction_.md)
  Composites a portion of the image to the specified location using the source-over operator.
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28at,from,operation,fraction%29.md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28in,from,operation,fraction%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
### Deprecated instance methods
- [func lockFocus()](./lockfocus%28%29.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](./lockfocusflipped%28_%29.md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](./init%28iconref%29.md)
  Initializes the image object with a Carbon-style icon resource.
- [- lockFocusOnRepresentation:](./lockfocusonrepresentation_.md)
  Prepares the specified image representation to receive drawing commands.
- [- bestRepresentationForDevice:](./bestrepresentationfordevice_.md)
  Returns the best representation for the device with the specified characteristics.
- [- compositeToPoint:operation:](./compositetopoint_operation_.md)
  Composites the entire image to the specified point in the current coordinate system.
- [- compositeToPoint:fromRect:operation:](./compositetopoint_fromrect_operation_.md)
  Composites a portion of the image to the specified point in the current coordinate system.
- [- compositeToPoint:operation:fraction:](./compositetopoint_operation_fraction_.md)
  Composites the entire image at the specified opacity in the current coordinate system.
- [- dissolveToPoint:fraction:](./dissolvetopoint_fraction_.md)
  Composites the entire image to the specified location using the source-over operator.
- [- dissolveToPoint:fromRect:fraction:](./dissolvetopoint_fromrect_fraction_.md)
  Composites a portion of the image to the specified location using the source-over operator.
- [- setScalesWhenResized:](./setscaleswhenresized_.md)
  Sets whether to scale different-sized image representations to fit the image’s size.
- [- scalesWhenResized](./scaleswhenresized.md)
  Returns a Boolean value that indicates whether to scale image representations to fit the image’s size.
- [- setDataRetained:](./setdataretained_.md)
  Sets whether the image retains its source image data.
- [- isDataRetained](./isdataretained.md)
  Returns a Boolean value that incidates whether the image retains its source image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/compositetopoint:fromrect:operation:fraction:)*