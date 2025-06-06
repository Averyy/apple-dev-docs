# multisampleColorTexture

**Framework**: MetalKit  
**Kind**: property

The multisample color sample texture to render into.

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
var multisampleColorTexture: (any MTLTexture)? { get }
```

#### Discussion

The format of this texture is determined by the value of the [`colorPixelFormat`](mtkview/colorpixelformat.md) and [`sampleCount`](mtkview/samplecount.md) properties.

The default value is `nil`. This value is also `nil` if the specified pixel format is [`MTLPixelFormat.invalid`](https://developer.apple.com/documentation/Metal/MTLPixelFormat/invalid), or if [`sampleCount`](mtkview/samplecount.md) is less than or equal to 1.

## See Also

- [var currentRenderPassDescriptor: MTLRenderPassDescriptor?](mtkview/currentrenderpassdescriptor.md)
  A render pass descriptor to draw into the current drawable.
- [var currentDrawable: (any CAMetalDrawable)?](mtkview/currentdrawable.md)
  The drawable to use for the current frame.
- [var depthStencilTexture: (any MTLTexture)?](mtkview/depthstenciltexture.md)
  A packed depth and stencil texture associated with the current drawable object’s texture.
- [var depthStencilStorageMode: MTLStorageMode](mtkview/depthstencilstoragemode.md)
  The storage mode that the packed depth and stencil texture use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/multisamplecolortexture)*