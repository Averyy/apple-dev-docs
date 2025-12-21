# unknown

**Framework**: Metal  
**Kind**: property

An option for a texture whose usage is unknown.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var unknown: MTLTextureUsage { get }
```

## Mentions

- [Optimizing texture data](optimizing-texture-data.md)

#### Discussion

Set this option if you’re not sure how your app uses the given texture, but you want to be able to use it in many ways. This might be the case if you have multiple code paths and it’s unclear how your app specifically uses the texture at runtime.

This is the most flexible usage option for a texture, but it incurs a significant performance cost. Metal can’t optimize operations for the texture if you don’t set specific usage options.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to the given texture if you set this option.

## See Also

- [static var shaderRead: MTLTextureUsage](mtltextureusage/shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var shaderWrite: MTLTextureUsage](mtltextureusage/shaderwrite.md)
  An option for writing to the texture in a shader.
- [static var shaderAtomic: MTLTextureUsage](mtltextureusage/shaderatomic.md)
  An option that enables atomic memory operations on texture elements in shader code.
- [static var renderTarget: MTLTextureUsage](mtltextureusage/rendertarget.md)
  An option for rendering to the texture in a render pass.
- [static var pixelFormatView: MTLTextureUsage](mtltextureusage/pixelformatview.md)
  An option to create texture views with a different component layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage/unknown)*