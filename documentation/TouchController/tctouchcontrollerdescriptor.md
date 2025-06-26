# TCTouchControllerDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a touch controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TCTouchControllerDescriptor
```

## Topics

### Inspecting the controller descriptor
- [var colorPixelFormat: MTLPixelFormat](tctouchcontrollerdescriptor/colorpixelformat.md)
  The pixel format for the drawable texture.
- [var depthAttachmentPixelFormat: MTLPixelFormat](tctouchcontrollerdescriptor/depthattachmentpixelformat.md)
  The pixel format for the depth attachment.
- [var device: any MTLDevice](tctouchcontrollerdescriptor/device.md)
  The Metal device to use for rendering.
- [var sampleCount: Int](tctouchcontrollerdescriptor/samplecount.md)
  The number of samples per pixel for multisampling.
- [var scaleFactor: CGFloat](tctouchcontrollerdescriptor/scalefactor.md)
  The scale factor of the screen.
- [var screenHeight: CGFloat](tctouchcontrollerdescriptor/screenheight.md)
  The height of the screen in points.
- [var screenWidth: CGFloat](tctouchcontrollerdescriptor/screenwidth.md)
  The width of the screen in points.
- [var stencilAttachmentPixelFormat: MTLPixelFormat](tctouchcontrollerdescriptor/stencilattachmentpixelformat.md)
  The pixel format for the stencil attachment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(descriptor: TCTouchControllerDescriptor)](tctouchcontroller/init(descriptor:).md)
  Creates a new instance with the provided descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontrollerdescriptor)*