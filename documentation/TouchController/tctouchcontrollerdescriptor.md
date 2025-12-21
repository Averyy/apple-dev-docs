# TCTouchControllerDescriptor

**Framework**: Touch Controller  
**Kind**: class

A descriptor for configuring a touch controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCTouchControllerDescriptor
```

## Topics

### Creating a touch controller descriptor
- [init()](tctouchcontrollerdescriptor/init.md)
- [convenience init(mtkView: MTKView)](tctouchcontrollerdescriptor/init(mtkview:).md)
### Inspecting the controller descriptor
- [var colorPixelFormat: MTLPixelFormat](tctouchcontrollerdescriptor/colorpixelformat.md)
  The pixel format for the drawable texture.
- [var depthAttachmentPixelFormat: MTLPixelFormat](tctouchcontrollerdescriptor/depthattachmentpixelformat.md)
  The pixel format for the depth attachment.
- [var device: any MTLDevice](tctouchcontrollerdescriptor/device.md)
  The Metal device to use for rendering.
- [var drawableSize: CGSize](tctouchcontrollerdescriptor/drawablesize.md)
  The size of the drawable to which the touch controller’s contents be drawn, in native pixels.
- [var sampleCount: Int](tctouchcontrollerdescriptor/samplecount.md)
  The number of samples per pixel for multisampling.
- [var size: CGSize](tctouchcontrollerdescriptor/size.md)
  The size of the view the touch controller’s drawable is embedded in, in points.
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