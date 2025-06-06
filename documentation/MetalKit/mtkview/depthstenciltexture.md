# depthStencilTexture

**Framework**: MetalKit  
**Kind**: property

A packed depth and stencil texture associated with the current drawable object’s texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var depthStencilTexture: (any MTLTexture)? { get }
```

#### Discussion

The value of [`depthStencilPixelFormat`](mtkview/depthstencilpixelformat.md) determines the format of this texture.

The default value is `nil`. This value is also `nil` if the specified pixel format is [`MTLPixelFormat.invalid`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/invalid).

## See Also

- [var currentRenderPassDescriptor: MTLRenderPassDescriptor?](mtkview/currentrenderpassdescriptor.md)
  A render pass descriptor to draw into the current drawable.
- [var currentDrawable: (any CAMetalDrawable)?](mtkview/currentdrawable.md)
  The drawable to use for the current frame.
- [var depthStencilStorageMode: MTLStorageMode](mtkview/depthstencilstoragemode.md)
  The storage mode that the packed depth and stencil texture use.
- [var multisampleColorTexture: (any MTLTexture)?](mtkview/multisamplecolortexture.md)
  The multisample color sample texture to render into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/depthstenciltexture)*