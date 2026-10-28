# renderTarget

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option for rendering to the texture in a render pass.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var renderTarget: MTLTextureUsage { get }
```

```c
MTLTextureUsageRenderTarget
```

## Mentions

- [Developing Metal apps that run in Simulator](../developing-metal-apps-that-run-in-simulator.md)
- [Optimizing texture data](../optimizing-texture-data.md)

## Discussion

Set this option if you use the given texture as a color, depth, or stencil render target in any render pass. This option allows you to assign the texture to the [`texture`](../mtlrenderpassattachmentdescriptor/texture.md) property of an [`MTLRenderPassAttachmentDescriptor`](../mtlrenderpassattachmentdescriptor.md).

> ❗ **Important**:  Rendering and writing to a texture are different operations, and you don’t need to combine their usage options. Set the [`renderTarget`](./rendertarget.md) option if you render to a given texture, but don’t set the [`shaderWrite`](./shaderwrite.md) option if you don’t write to the texture. The [`renderTarget`](./rendertarget.md) and [`shaderWrite`](./shaderwrite.md) options aren’t equivalent, and setting [`renderTarget`](./rendertarget.md) doesn’t require you to also set [`shaderWrite`](./shaderwrite.md).

## See Also

### Specifying texture usage options
- [static var unknown: MTLTextureUsage](./unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderRead: MTLTextureUsage](./shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var shaderWrite: MTLTextureUsage](./shaderwrite.md)
  An option for writing to the texture in a shader.
- [static var shaderAtomic: MTLTextureUsage](./shaderatomic.md)
  An option that enables atomic memory operations on texture elements in shader code.
- [static var pixelFormatView: MTLTextureUsage](./pixelformatview.md)
  An option to create texture views with a different component layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/rendertarget)*