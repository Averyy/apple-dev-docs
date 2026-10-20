# colorAttachments

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of attachments that store color data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var colorAttachments: MTLRenderPipelineColorAttachmentDescriptorArray { get }
```

```objc
@property (readonly) MTLRenderPipelineColorAttachmentDescriptorArray * colorAttachments;
```

## See Also

### Specifying rendering pipeline state
- [func reset()](./reset%28%29.md)
  Specifies the default rendering pipeline state values for the descriptor.
- [var depthAttachmentPixelFormat: MTLPixelFormat](./depthattachmentpixelformat.md)
  The pixel format of the attachment that stores depth data.
- [var stencilAttachmentPixelFormat: MTLPixelFormat](./stencilattachmentpixelformat.md)
  The pixel format of the attachment that stores stencil data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/colorattachments)*