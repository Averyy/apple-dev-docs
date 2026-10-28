# setFlipped:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the polarity of the y axis is inverted when drawing an image.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: The flipped property of an image was widely misunderstood and has been deprecated. Use  [`draw(in:from:operation:fraction:respectFlipped:hints:)`](./draw%28in,from,operation,fraction,respectflipped,hints%29.md) to draw respecting a context’s flipped status and [`lockFocusFlipped(_:)`](./lockfocusflipped%28_%29.md) to draw into a flipped image.

## Declaration

```objc
- (void) setFlipped:(BOOL) flag;
```

## Discussion

If `flag` is [`true`](../../Swift/true.md), the y-axis of the image’s internal coordinate system is inverted, with the origin in the upper-left corner and the positive y axis extending downward. This method affects only the coordinate system used internally by the image and the orientation of the image when it is drawn; it does not affect the coordinate system used to specify the position of an image in a view. This method does not cause the receiver to recache itself.

If you set `flag` to [`true`](../../Swift/true.md) and then lock focus and draw into the image, the content you draw is cached in the inverted (flipped) orientation. Changing the value for  `flag` does not affect the orientation of the cached image.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if you want the image data to be inverted before drawing; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [func recache()](./recache%28%29.md)
  Invalidates and frees offscreen caches of all image representations.
- [- isFlipped](./isflipped.md)
  Returns a Boolean value that indicates whether the image uses a flipped coordinate system.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/setflipped:)*