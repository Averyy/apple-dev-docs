# depthStencilStorageMode

**Framework**: MetalKit  
**Kind**: property

The storage mode that the packed depth and stencil texture use.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var depthStencilStorageMode: MTLStorageMode { get set }
```

#### Discussion

The default value is [`MTLStorageMode.private`](https://developer.apple.com/documentation/Metal/MTLStorageMode/private).

## See Also

- [var currentRenderPassDescriptor: MTLRenderPassDescriptor?](mtkview/currentrenderpassdescriptor.md)
  A render pass descriptor to draw into the current drawable.
- [var currentDrawable: (any CAMetalDrawable)?](mtkview/currentdrawable.md)
  The drawable to use for the current frame.
- [var depthStencilTexture: (any MTLTexture)?](mtkview/depthstenciltexture.md)
  A packed depth and stencil texture associated with the current drawable object’s texture.
- [var multisampleColorTexture: (any MTLTexture)?](mtkview/multisamplecolortexture.md)
  The multisample color sample texture to render into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/depthstencilstoragemode)*