# setScalesWhenResized:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether to scale different-sized image representations to fit the image’s size.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: This method was related to caching behavior. In macOS 10.6 and later, image caching is no longer necessary and as a result there is no replacement necessary.

## Declaration

```objc
- (void) setScalesWhenResized:(BOOL) flag;
```

#### Discussion

Most images (especially those loaded from files and URLs) contain only a single image representation whose size is the same as the receiver. It is possible to add image representations using the [`addRepresentation(_:)`](./addrepresentation%28_%29.md) or [`addRepresentations(_:)`](./addrepresentations%28_%29.md) methods but doing so is rarely necessary because modern hardware is powerful enough to resize and scale images quickly. The only reason to consider creating new representations is if each representations contains a customized version of the image at a specific size. (TIFF images may also contain a thumbnail version of an image, which is stored using a separate image representation.) If you pass [`true`](../../Swift/true.md) in the `flag` parameter, and subsequently assign a new value to the [`size`](./size.md) property, all such image representations would be scaled to the same size. Scaling of bitmap images usually results in the interpolation of the bitmap data.

This method does not invalidate the caches of any of the receiver’s image representations. The caches are not invalidated until you change the image size using the [`size`](./size.md) property. Scaling affects only the cached offscreen data for a given image representation.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if image representations are scaled to fit; otherwise [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [- scalesWhenResized](./scaleswhenresized.md)
  Returns a Boolean value that indicates whether to scale image representations to fit the image’s size.
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
- [- scalesWhenResized](./scaleswhenresized.md)
  Returns a Boolean value that indicates whether to scale image representations to fit the image’s size.
- [- setDataRetained:](./setdataretained_.md)
  Sets whether the image retains its source image data.
- [- isDataRetained](./isdataretained.md)
  Returns a Boolean value that incidates whether the image retains its source image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/setscaleswhenresized:)*