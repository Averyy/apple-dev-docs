# depthStencilAttachmentTextureUsage

**Framework**: MetalKit  
**Kind**: property

The texture usage characteristics that the view uses when creating the depth and stencil textures.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var depthStencilAttachmentTextureUsage: MTLTextureUsage { get set }
```

#### Discussion

The default value is [`renderTarget`](https://developer.apple.com/documentation/Metal/MTLTextureUsage/renderTarget).

## See Also

- [var depthStencilPixelFormat: MTLPixelFormat](mtkview/depthstencilpixelformat.md)
  The format used to generate the [`depthStencilTexture`](mtkview/depthstenciltexture.md) object.
- [var clearDepth: Double](mtkview/cleardepth.md)
  The depth value to use to clear the depth target when creating a render pass descriptor.
- [var clearStencil: UInt32](mtkview/clearstencil.md)
  The stencil value to use to clear the stencil target when creating a render pass descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/depthstencilattachmenttextureusage)*