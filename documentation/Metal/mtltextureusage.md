# MTLTextureUsage

**Framework**: Metal  
**Kind**: struct

An enumeration for the various options that determine how you can use a texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLTextureUsage
```

## Mentions

- [Optimizing Texture Data](optimizing-texture-data.md)

#### Overview

If a texture has multiple uses in your app, you can combine multiple usage options for that texture. After you set the texture’s usage options, you can use it only in the ways that you specified.

Metal can optimize operations for a given texture, based on its intended use. Set explicit usage options for a texture, if you know them in advance, before you use the texture. Only set usage options that correspond to a texture’s intended use.

In iOS devices with GPU family 5, Metal doesn’t apply lossless compression to a given texture if you set any of these options:

- [`unknown`](mtltextureusage/unknown.md)
- [`shaderWrite`](mtltextureusage/shaderwrite.md)
- [`pixelFormatView`](mtltextureusage/pixelformatview.md)

## Topics

### Specifying Texture Usage Options
- [static var unknown: MTLTextureUsage](mtltextureusage/unknown.md)
  An option for a texture whose usage is unknown.
- [static var shaderRead: MTLTextureUsage](mtltextureusage/shaderread.md)
  An option for reading or sampling from the texture in a shader.
- [static var shaderWrite: MTLTextureUsage](mtltextureusage/shaderwrite.md)
  An option for writing to the texture in a shader.
- [static var renderTarget: MTLTextureUsage](mtltextureusage/rendertarget.md)
  An option for rendering to the texture in a render pass.
- [static var pixelFormatView: MTLTextureUsage](mtltextureusage/pixelformatview.md)
  An option to create texture views with a different component layout.
### Creating Texture Usage Options
- [init(rawValue: UInt)](mtltextureusage/init(rawvalue:).md)
  Creates new, empty usage options.
### Type Properties
- [static var shaderAtomic: MTLTextureUsage](mtltextureusage/shaderatomic.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var textureType: MTLTextureType](mtltexture/texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](mtltexture/pixelformat.md)
  The format of pixels in the texture.
- [var width: Int](mtltexture/width.md)
  The width of the texture image for the base level mipmap, in pixels.
- [var height: Int](mtltexture/height.md)
  The height of the texture image for the base level mipmap, in pixels.
- [var depth: Int](mtltexture/depth.md)
  The depth of the texture image for the base level mipmap, in pixels.
- [var mipmapLevelCount: Int](mtltexture/mipmaplevelcount.md)
  The number of mipmap levels in the texture.
- [var arrayLength: Int](mtltexture/arraylength.md)
  The number of slices in the texture array.
- [var sampleCount: Int](mtltexture/samplecount.md)
  The number of samples in each pixel.
- [var isFramebufferOnly: Bool](mtltexture/isframebufferonly.md)
  A Boolean value that indicates whether the texture can only be used as a render target.
- [var usage: MTLTextureUsage](mtltexture/usage.md)
  Options that determine how you can use the texture.
- [var allowGPUOptimizedContents: Bool](mtltexture/allowgpuoptimizedcontents.md)
  A Boolean value indicating whether the GPU is allowed to adjust the contents of the texture to improve GPU performance.
- [var isShareable: Bool](mtltexture/isshareable.md)
  A Boolean indicating whether this texture can be shared with other processes.
- [var swizzle: MTLTextureSwizzleChannels](mtltexture/swizzle.md)
  The pattern that the GPU applies to pixels when you read or sample pixels from the texture.
- [enum MTLTextureType](mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureusage)*