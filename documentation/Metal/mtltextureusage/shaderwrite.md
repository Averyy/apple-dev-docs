# shaderWrite

**Framework**: Metal  
**Kind**: property

An option for writing to the texture in a shader.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var shaderWrite: MTLTextureUsage { get }
```

## Mentions

- [Optimizing Texture Data](optimizing-texture-data.md)

#### Discussion

Set this option if you access the given texture with a `write()` function in any shader. This option enables the `access::write` attribute for the texture. For more information about texture functions and access attributes, see [`Metal Shading Language Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364).

If the texture is a read-write texture that you also access with a `read()` function in the same shader, set the [`shaderRead`](mtltextureusage/shaderread.md) option to enable the `access::read_write` attribute.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to the given texture if you set this option.

> ❗ **Important**:  Rendering and writing to a texture are different operations, and you don’t need to combine their usage options. Set the [`renderTarget`](mtltextureusage/rendertarget.md) option if you render to a given texture, but don’t set the [`shaderWrite`](mtltextureusage/shaderwrite.md) option if you don’t write to the texture. The [`renderTarget`](mtltextureusage/rendertarget.md) and [`shaderWrite`](mtltextureusage/shaderwrite.md) options aren’t equivalent, and setting [`renderTarget`](mtltextureusage/rendertarget.md) doesn’t require you to also set [`shaderWrite`](mtltextureusage/shaderwrite.md).

 Rendering and writing to a texture are different operations, and you don’t need to combine their usage options. Set the [`renderTarget`](mtltextureusage/rendertarget.md) option if you render to a given texture, but don’t set the [`shaderWrite`](mtltextureusage/shaderwrite.md) option if you don’t write to the texture. The [`renderTarget`](mtltextureusage/rendertarget.md) and [`shaderWrite`](mtltextureusage/shaderwrite.md) options aren’t equivalent, and setting [`renderTarget`](mtltextureusage/rendertarget.md) doesn’t require you to also set [`shaderWrite`](mtltextureusage/shaderwrite.md).

## See Also

- [static var unknown: MTLTextureUsage](mtltextureusage/unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderRead: MTLTextureUsage](mtltextureusage/shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var renderTarget: MTLTextureUsage](mtltextureusage/rendertarget.md)
  An option for rendering to the texture in a render pass.
- [static var pixelFormatView: MTLTextureUsage](mtltextureusage/pixelformatview.md)
  An option to create texture views with a different component layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/shaderwrite)*