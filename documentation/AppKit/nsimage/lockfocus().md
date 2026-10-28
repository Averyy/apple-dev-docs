# lockFocus()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prepares the image to receive drawing commands.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use [`init(size:flipped:drawingHandler:)`](./init%28size,flipped,drawinghandler%29.md) instead.

## Declaration

```swift
func lockFocus()
```

```objc
- (void) lockFocus;
```

## Discussion

This method sets the current drawing context to the area of the offscreen window used to cache the receiver’s contents. Subsequent drawing commands are composited to this offscreen window. If the offscreen drawing area already has some content, any new drawing commands are composited with that content. This method does not modify the original image data directly.

When locking focus, this method chooses the best image representation object available and locks focus on that object. If the receiver has no image representations, this method creates one with the default depth and locks focus on it.

A successful [`lockFocus()`](./lockfocus%28%29.md) message must be balanced with a matching [`unlockFocus()`](./unlockfocus%28%29.md) message to the same `NSImage` object. These messages bracket the code that draws the image.

If [`lockFocus()`](./lockfocus%28%29.md) is unable to focus on the image, it raises an `NSImageCacheException`.

## See Also

### Related Documentation
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether it is possible to draw an image representation.
- [var representations: [NSImageRep]](./representations.md)
  An array containing all of the image object’s image representations.
- [var prefersColorMatch: Bool](./preferscolormatch.md)
  A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.
- [- bestRepresentationForDevice:](./bestrepresentationfordevice_.md)
  Returns the best representation for the device with the specified characteristics.
### Deprecated instance methods
- [func lockFocusFlipped(Bool)](./lockfocusflipped%28_%29.md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](./init%28iconref%29.md)
  Initializes the image object with a Carbon-style icon resource.
- [- lockFocusOnRepresentation:](./lockfocusonrepresentation_.md)
  Prepares the specified image representation to receive drawing commands.
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
- [- isDataRetained](./isdataretained.md)
  Returns a Boolean value that incidates whether the image retains its source image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/lockfocus())*