# sampleCount

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The number of samples per pixel for multisampling.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var sampleCount: Int { get set }
```

```objc
@property (nonatomic, assign, readwrite) NSUInteger sampleCount;
```

## See Also

### Inspecting the controller descriptor
- [var colorPixelFormat: MTLPixelFormat](./colorpixelformat.md)
  The pixel format for the drawable texture.
- [var depthAttachmentPixelFormat: MTLPixelFormat](./depthattachmentpixelformat.md)
  The pixel format for the depth attachment.
- [var device: any MTLDevice](./device.md)
  The Metal device to use for rendering.
- [var drawableSize: CGSize](./drawablesize.md)
  The size of the drawable to which the touch controller’s contents be drawn, in native pixels.
- [var size: CGSize](./size.md)
  The size of the view the touch controller’s drawable is embedded in, in points.
- [var stencilAttachmentPixelFormat: MTLPixelFormat](./stencilattachmentpixelformat.md)
  The pixel format for the stencil attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontrollerdescriptor/samplecount)*