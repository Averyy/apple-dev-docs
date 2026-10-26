# compositeToPoint:operation:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Composites the entire image to the specified point in the current coordinate system.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`draw(at:from:operation:fraction:)`](./draw%28at,from,operation,fraction%29.md) instead.

## Declaration

```objc
- (void) compositeToPoint:(NSPoint) point operation:(NSCompositingOperation) operation;
```

#### Discussion

This method draws the receiver’s best image representation at the specified point in the currently focused view. The entire image is drawn using its current size information. During drawing, the image is composited from its offscreen window cache. Because the offscreen cache is not created until the image representation is first used, this method may need to render the image before compositing. Bitmap representations in particular are not cached until they are explicitly rendered. You can use the [`lockFocus()`](./lockfocus%28%29.md) and [`unlockFocus()`](./unlockfocus%28%29.md) methods to force the cached version to be created.

During printing, this method ignores the `op` parameter. Even though this parameter is ignored, this method attempts to render the image as close as possible to its appearance when the compositing operation is used on the screen. In either case, the best image representation is chosen for the printing context.

## Parameters

- `point`: The point at which to draw the image, specified in the current coordinate system.
- `operation`: The compositing operation to use when drawing the image to the screen. The supported compositing operations are described in `Constants`.

## See Also

### Related Documentation
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28at,from,operation,fraction%29.md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](./draw%28in,from,operation,fraction%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [- dissolveToPoint:fraction:](./dissolvetopoint_fraction_.md)
  Composites the entire image to the specified location using the source-over operator.
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
- [- compositeToPoint:fromRect:operation:](./compositetopoint_fromrect_operation_.md)
  Composites a portion of the image to the specified point in the current coordinate system.
- [- compositeToPoint:fromRect:operation:fraction:](./compositetopoint_fromrect_operation_fraction_.md)
  Composites a portion of the image at the specified opacity to the current coordinate system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/compositetopoint:operation:)*