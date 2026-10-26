# renderPassDescriptor

**Framework**: Metal  
**Kind**: method  
**Role**: Type Method

Creates a default render pass descriptor.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (MTLRenderPassDescriptor *) renderPassDescriptor;
```

#### Return Value

A new render pass descriptor with no attachments at all.

#### Discussion

Set the desired color attachments with the [`setObject:atIndexedSubscript:`](../mtlrenderpasscolorattachmentdescriptorarray/setobject_atindexedsubscript_.md) method of the [`colorAttachments`](./colorattachments.md) property. Set the desired depth and stencil attachments with the [`depthAttachment`](./depthattachment.md) and [`stencilAttachment`](./stencilattachment.md) properties, respectively.

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/renderpassdescriptor)*