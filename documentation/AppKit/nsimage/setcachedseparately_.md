# setCachedSeparately:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether each image representation uses a separate offscreen window to cache its contents.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: `NSImage` no longer caches to windows. There is no replacement method

## Declaration

```objc
- (void) setCachedSeparately:(BOOL) flag;
```

## Discussion

If you specify [`false`](../../Swift/false.md), a representation can be cached together with other images, though in practice it might not be. This method does not invalidate any existing caches.

If you plan to resize an `NSImage` object frequently, it is usually more efficient to cache its representations separately. In some situations, you might also want to enable separate caching if you plan to use the [`compositeToPoint:fromRect:operation:`](./compositetopoint_fromrect_operation_.md) or [`compositeToPoint:fromRect:operation:fraction:`](./compositetopoint_fromrect_operation_fraction_.md)methods to draw the image.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if you want each of the receiver’s image representation objects to use a separate offscreen window for caching; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [func recache()](./recache%28%29.md)
  Invalidates and frees offscreen caches of all image representations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/setcachedseparately:)*