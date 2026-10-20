# colorAttachments

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of state information for attachments that store color data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray { get }
```

```objc
@property (readonly) MTLRenderPassColorAttachmentDescriptorArray * colorAttachments;
```

## See Also

### Specifying the attachments for a rendering pass
- [var depthAttachment: MTLRenderPassDepthAttachmentDescriptor!](./depthattachment.md)
  State information for an attachment that stores depth data.
- [var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor!](./stencilattachment.md)
  State information for an attachment that stores stencil data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/colorattachments)*