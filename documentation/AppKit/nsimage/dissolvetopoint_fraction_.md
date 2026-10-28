# dissolveToPoint:fraction:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Composites the entire image to the specified location using the source-over operator.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`draw(at:from:operation:fraction:)`](./draw%28at,from,operation,fraction%29.md) instead.

## Declaration

```objc
- (void) dissolveToPoint:(NSPoint) point fraction:(CGFloat) fraction;
```

## Discussion

Except for the choice of compositing operator, this method behaves in the same way as the [`compositeToPoint:operation:`](./compositetopoint_operation_.md) method. During printing, the `delta` parameter is ignored.

If the source image contains alpha information, this operation may promote the destination `NSWindow` object to contain alpha information.

To slowly dissolve this image onto another, you can invoke this method (or the [`dissolveToPoint:fromRect:fraction:`](./dissolvetopoint_fromrect_fraction_.md) method) repeatedly with an ever-increasing `delta` value. Because the `delta` parameter refers to the visible fraction of the source image, increasing the value causes the source image to replace the destination content gradually. You should generally perform this type of operation using a buffered window or other offscreen drawing environment.

## Parameters

- `point`: The point at which to draw the image, specified in the current coordinate system.
- `fraction`: The desired opacity of the image, specified as a value between 0.0 and 1.0. A value of 0.0 renders the image totally transparent while 1.0 renders it fully opaque. Values larger than 1.0 are interpreted as 1.0.

## See Also

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
- [- compositeToPoint:fromRect:operation:fraction:](./compositetopoint_fromrect_operation_fraction_.md)
  Composites a portion of the image at the specified opacity to the current coordinate system.
- [- compositeToPoint:operation:fraction:](./compositetopoint_operation_fraction_.md)
  Composites the entire image at the specified opacity in the current coordinate system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/dissolvetopoint:fraction:)*