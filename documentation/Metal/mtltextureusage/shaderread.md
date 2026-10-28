# shaderRead

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option for reading or sampling from the texture in a shader.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var shaderRead: MTLTextureUsage { get }
```

```c
MTLTextureUsageShaderRead
```

## Discussion

Set this option if you access the given texture with a `read()` or `sample()` function in any shader. This option enables the `access::read` and `access::sample` attributes for the texture. For more information about texture functions and access attributes, see [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364).

If the texture is a read-write texture that you also access with a `write()` function in the same shader, set the [`shaderWrite`](./shaderwrite.md) option to enable the `access::read_write` attribute.

## See Also

### Specifying texture usage options
- [static var unknown: MTLTextureUsage](./unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderWrite: MTLTextureUsage](./shaderwrite.md)
  An option for writing to the texture in a shader.
- [static var shaderAtomic: MTLTextureUsage](./shaderatomic.md)
  An option that enables atomic memory operations on texture elements in shader code.
- [static var renderTarget: MTLTextureUsage](./rendertarget.md)
  An option for rendering to the texture in a render pass.
- [static var pixelFormatView: MTLTextureUsage](./pixelformatview.md)
  An option to create texture views with a different component layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/shaderread)*