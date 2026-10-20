# shaderAtomic

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that enables atomic memory operations on texture elements in shader code.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static var shaderAtomic: MTLTextureUsage { get }
```

```c
MTLTextureUsageShaderAtomic
```

#### Discussion

Shaders can run atomic memory operations on textures with specific element type and pixel format combinations:

| Shader element type | Pixel format |
| --- | --- |
| `int` | [`MTLPixelFormat.r32Sint`](../mtlpixelformat/r32sint.md) |
| `uint` | [`MTLPixelFormat.r32Uint`](../mtlpixelformat/r32uint.md) |
| `ulong` | [`MTLPixelFormat.rg32Uint`](../mtlpixelformat/rg32uint.md) |

> **Note**:  Applying this usage option to a texture disables lossless compression.

## See Also

### Specifying texture usage options
- [static var unknown: MTLTextureUsage](./unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderRead: MTLTextureUsage](./shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var shaderWrite: MTLTextureUsage](./shaderwrite.md)
  An option for writing to the texture in a shader.
- [static var renderTarget: MTLTextureUsage](./rendertarget.md)
  An option for rendering to the texture in a render pass.
- [static var pixelFormatView: MTLTextureUsage](./pixelformatview.md)
  An option to create texture views with a different component layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/shaderatomic)*