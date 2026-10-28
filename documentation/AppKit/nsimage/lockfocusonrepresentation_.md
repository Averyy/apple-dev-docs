# lockFocusOnRepresentation:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prepares the specified image representation to receive drawing commands.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use the code fragment shown in the special considerations below.

## Declaration

```objc
- (void) lockFocusOnRepresentation:(NSImageRep *) imageRepresentation;
```

## Discussion

This method sets the current drawing context to the area of the offscreen window used to cache the specified image representation’s contents. Subsequent drawing commands are composited to this offscreen window. If the offscreen drawing area already has some content, any new drawing commands are composited with that content. This method does not modify the original image data directly.

If `imageRepresentation` is `nil`, this method acts like the [`lockFocus()`](./lockfocus%28%29.md) method, setting the focus to the best representation for the `NSImage` object.

A successful [`lockFocusOnRepresentation:`](./lockfocusonrepresentation_.md) message must be balanced with a matching [`unlockFocus()`](./unlockfocus%28%29.md) message to the same `NSImage` object. These messages bracket the code that draws the image.

If [`lockFocusOnRepresentation:`](./lockfocusonrepresentation_.md) is unable to focus on the specified image representation, it raises an `NSImageCacheException`.

### Special Considerations

This method is deprecated as it did not set up `imageRepresentation` as a drawing destination, it set the image up as a drawing destination, then drew `imageRepresentation` into it. You can replace this functionality with the following code fragment:

```objc
[image lockFocus];
[imageRepresentation drawInRect:NSMakeRect(0,0,[image size].width, [image size].height)];
 
[image unlockFocus];
```

## Parameters

- `imageRepresentation`: An image representation belonging to the receiver, or `nil` if you want the receiver to choose which image representation to use.

## See Also

### Related Documentation
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether it is possible to draw an image representation.
### Deprecated instance methods
- [func lockFocus()](./lockfocus%28%29.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](./lockfocusflipped%28_%29.md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](./init%28iconref%29.md)
  Initializes the image object with a Carbon-style icon resource.
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
- [- isDataRetained](./isdataretained.md)
  Returns a Boolean value that incidates whether the image retains its source image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/lockfocusonrepresentation:)*