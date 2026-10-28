# stencilAttachmentPixelFormat

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The pixel format of the attachment that stores stencil data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var stencilAttachmentPixelFormat: MTLPixelFormat { get set }
```

```objc
@property (nonatomic) MTLPixelFormat stencilAttachmentPixelFormat;
```

## Discussion

By default, the pixel format of the rendering pipeline state for each attachment is `MTLPixelFormatInvalid`.

## See Also

### Specifying rendering pipeline state
- [func reset()](./reset%28%29.md)
  Specifies the default rendering pipeline state values for the descriptor.
- [var colorAttachments: MTLRenderPipelineColorAttachmentDescriptorArray](./colorattachments.md)
  An array of attachments that store color data.
- [var depthAttachmentPixelFormat: MTLPixelFormat](./depthattachmentpixelformat.md)
  The pixel format of the attachment that stores depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/stencilattachmentpixelformat)*