# stencilAttachment

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

State information for an attachment that stores stencil data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) MTLRenderPassStencilAttachmentDescriptor * stencilAttachment;
```

## See Also

### Specifying the attachments for a rendering pass
- [var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray](./colorattachments.md)
  An array of state information for attachments that store color data.
- [var depthAttachment: MTLRenderPassDepthAttachmentDescriptor!](./depthattachment.md)
  State information for an attachment that stores depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/stencilattachment)*