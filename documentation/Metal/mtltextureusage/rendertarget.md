# renderTarget

**Framework**: Metal  
**Kind**: property

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

## Mentions

- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
- [Optimizing Texture Data](optimizing-texture-data.md)

#### Discussion

Set this option if you use the given texture as a color, depth, or stencil render target in any render pass. This option allows you to assign the texture to the [`texture`](mtlrenderpassattachmentdescriptor/texture.md) property of a [`MTLRenderPassAttachmentDescriptor`](mtlrenderpassattachmentdescriptor.md).

> ❗ **Important**:  Rendering and writing to a texture are different operations, and you don’t need to combine their usage options. Set the [`renderTarget`](mtltextureusage/rendertarget.md) option if you render to a given texture, but don’t set the [`shaderWrite`](mtltextureusage/shaderwrite.md) option if you don’t write to the texture. The [`renderTarget`](mtltextureusage/rendertarget.md) and [`shaderWrite`](mtltextureusage/shaderwrite.md) options aren’t equivalent, and setting [`renderTarget`](mtltextureusage/rendertarget.md) doesn’t require you to also set [`shaderWrite`](mtltextureusage/shaderwrite.md).

## See Also

- [static var unknown: MTLTextureUsage](mtltextureusage/unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderRead: MTLTextureUsage](mtltextureusage/shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var shaderWrite: MTLTextureUsage](mtltextureusage/shaderwrite.md)
  An option for writing to the texture in a shader.
- [static var pixelFormatView: MTLTextureUsage](mtltextureusage/pixelformatview.md)
  An option to create texture views with a different component layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/rendertarget)*