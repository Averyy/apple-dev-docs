# texture

**Framework**: Metal  
**Kind**: property

The texture object associated with this attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var texture: (any MTLTexture)? { get set }
```

## Mentions

- [Setting Load and Store Actions](setting-load-and-store-actions.md)
- [Choosing a Resource Storage Mode for Apple GPUs](choosing-a-resource-storage-mode-for-apple-gpus.md)

#### Discussion

You must set the attachment’s `texture` property, choosing an appropriate pixel format for the texture.

- To store color values in an attachment, use a texture with a color-renderable pixel format.
- To store depth values, use a texture with a depth-renderable pixel format, such as [`MTLPixelFormat.depth32Float`](mtlpixelformat/depth32float.md).
- To store stencil values, use a texture with a stencil-renderable pixel format, such as [`MTLPixelFormat.stencil8`](mtlpixelformat/stencil8.md).

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var level: Int](mtlrenderpassattachmentdescriptor/level.md)
  The mipmap level of the texture used for rendering to the attachment.
- [var slice: Int](mtlrenderpassattachmentdescriptor/slice.md)
  The slice of the texture used for rendering to the attachment.
- [var depthPlane: Int](mtlrenderpassattachmentdescriptor/depthplane.md)
  The depth plane of the texture used for rendering to the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/texture)*