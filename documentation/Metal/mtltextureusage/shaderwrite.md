# shaderWrite

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

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

```c
MTLTextureUsageShaderWrite
```

## Mentions

- [Optimizing texture data](../optimizing-texture-data.md)

## Discussion

Set this option if you access the given texture with a `write()` function in any shader. This option enables the `access::write` attribute for the texture. For more information about texture functions and access attributes, see [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364).

If the texture is a read-write texture that you also access with a `read()` function in the same shader, set the [`shaderRead`](./shaderread.md) option to enable the `access::read_write` attribute.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to the given texture if you set this option.

> ❗ **Important**:  Rendering and writing to a texture are different operations, and you don’t need to combine their usage options. Set the [`renderTarget`](./rendertarget.md) option if you render to a given texture, but don’t set the [`shaderWrite`](./shaderwrite.md) option if you don’t write to the texture. The [`renderTarget`](./rendertarget.md) and [`shaderWrite`](./shaderwrite.md) options aren’t equivalent, and setting [`renderTarget`](./rendertarget.md) doesn’t require you to also set [`shaderWrite`](./shaderwrite.md).

## See Also

### Specifying texture usage options
- [static var unknown: MTLTextureUsage](./unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderRead: MTLTextureUsage](./shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var shaderAtomic: MTLTextureUsage](./shaderatomic.md)
  An option that enables atomic memory operations on texture elements in shader code.
- [static var renderTarget: MTLTextureUsage](./rendertarget.md)
  An option for rendering to the texture in a render pass.
- [static var pixelFormatView: MTLTextureUsage](./pixelformatview.md)
  An option to create texture views with a different component layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/shaderwrite)*