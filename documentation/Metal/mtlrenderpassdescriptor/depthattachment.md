# depthAttachment

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

State information for an attachment that stores depth data.

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
var depthAttachment: MTLRenderPassDepthAttachmentDescriptor! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) MTLRenderPassDepthAttachmentDescriptor * depthAttachment;
```

## See Also

### Specifying the attachments for a rendering pass
- [var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray](./colorattachments.md)
  An array of state information for attachments that store color data.
- [var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor!](./stencilattachment.md)
  State information for an attachment that stores stencil data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/depthattachment)*