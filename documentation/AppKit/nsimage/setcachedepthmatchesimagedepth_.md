# setCacheDepthMatchesImageDepth:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the image’s offscreen window caches use the same bit depth as the image data itself.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: `NSImage` no longer caches to windows. A cache is now generated appropriate for the destination where an image is drawn. There is no replacement method.

## Declaration

```objc
- (void) setCacheDepthMatchesImageDepth:(BOOL) flag;
```

#### Discussion

This method does not cause the receiver to recache itself. The default depth limit is equal to the bit depth of the deepest screen on the system.

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the offscreen caches use the same bit-depth associated with the image data; otherwise, [`false`](../../Swift/false.md) to indicate they should use the default bit depth.

## See Also

### Related Documentation
- [func recache()](./recache%28%29.md)
  Invalidates and frees offscreen caches of all image representations.
- [func lockFocus()](./lockfocus%28%29.md)
  Prepares the image to receive drawing commands.
- [- cacheDepthMatchesImageDepth](./cachedepthmatchesimagedepth.md)
  Returns a Boolean value that indicates whether an image’s offscreen window caches use the same bit depth as the image data itself.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/setcachedepthmatchesimagedepth:)*