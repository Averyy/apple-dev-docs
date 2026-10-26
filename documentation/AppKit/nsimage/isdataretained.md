# isDataRetained

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that incidates whether the image retains its source image data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: In macOS 10.6 and later, [`NSImage`](../nsimage.md) no longer discards data in such a way that the original can no longer be reconstructed. There is no replacement method.

## Declaration

```objc
- (BOOL) isDataRetained;
```

#### Return Value

[`true`](../../Swift/true.md) if the image retains its source data; otherwise, [`false`](../../Swift/false.md). The default value is [`false`](../../Swift/false.md) with some exceptions, which are covered in the discussion.

#### Discussion

For image objects initialized using either the [`init(byReferencingFile:)`](./init%28byreferencingfile%29.md) or [`init(byReferencing:)`](./init%28byreferencing%29.md) method, this value is [`true`](../../Swift/true.md) by default. The reason is that for these methods, data retention simply involves retaining the filename or URL.

Data retention increases the memory used by the `NSImage` object and its image representations.

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
- [- setDataRetained:](./setdataretained_.md)
  Sets whether the image retains its source image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/isdataretained)*