# sampleCount

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The number of samples in each pixel.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var sampleCount: Int { get }
```

#### Discussion

If [`textureType`](mtltexture/texturetype.md) is not [`MTLTextureType.type2DMultisample`](mtltexturetype/type2dmultisample.md), this value is `1`.

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
- [struct MTLTextureUsage](mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/samplecount)*