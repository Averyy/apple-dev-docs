# setDataRetained:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the image retains its source image data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: In macOS 10.6 and later, [`NSImage`](../nsimage.md) no longer discards data in such a way that the original can no longer be reconstructed. There is no replacement method.

## Declaration

```objc
- (void) setDataRetained:(BOOL) flag;
```

#### Discussion

Retention of the source image data is important if the source of the image data could change, be moved, or be deleted. Data retention is also useful if you plan to resize an image frequently; otherwise, resizing occurs on a cached copy of the image, which can lose image quality during successive scaling operations. With data retention enabled, the image is resized from the original source data.

If the responsibility for drawing the image is delegated to another object, there is no reason to retain the image data. Similarly, if the source of the image data is not expected to change or you do not plan to resize the image, you do not need to retain the data. In fact, retaining the data leads to increased memory usage, which could have a negative impact on performance.

If you create your image object using the [`init(byReferencingFile:)`](./init%28byreferencingfile%29.md) method, the only data retained is the name of the source file.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if you want the source image data to be retained; otherwise [`false`](../../Swift/false.md).

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
- [- dissolveToPoint:fraction:](./dissolvetopoint_fraction_.md)
  Composites the entire image to the specified location using the source-over operator.
- [- dissolveToPoint:fromRect:fraction:](./dissolvetopoint_fromrect_fraction_.md)
  Composites a portion of the image to the specified location using the source-over operator.
- [- setScalesWhenResized:](./setscaleswhenresized_.md)
  Sets whether to scale different-sized image representations to fit the image’s size.
- [- scalesWhenResized](./scaleswhenresized.md)
  Returns a Boolean value that indicates whether to scale image representations to fit the image’s size.
- [- isDataRetained](./isdataretained.md)
  Returns a Boolean value that incidates whether the image retains its source image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/setdataretained:)*