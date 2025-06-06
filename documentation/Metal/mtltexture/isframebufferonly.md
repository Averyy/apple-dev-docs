# isFramebufferOnly

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the texture can only be used as a render target.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var isFramebufferOnly: Bool { get }
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/swift/false), which indicates the use of the texture is not restricted.

If [`true`](https://developer.apple.com/documentation/swift/true), neither [`replace(region:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:)`](mtltexture/replace(region:mipmaplevel:slice:withbytes:bytesperrow:bytesperimage:).md) nor [`getBytes(_:bytesPerRow:bytesPerImage:from:mipmapLevel:slice:)`](mtltexture/getbytes(_:bytesperrow:bytesperimage:from:mipmaplevel:slice:).md) can be used with this texture. Also, this texture can only be used as an attachment for [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) and cannot be a texture argument for [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md), [`MTLBlitCommandEncoder`](mtlblitcommandencoder.md), or [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md).

Textures obtained from a [`CAMetalDrawable`](https://developer.apple.com/documentation/QuartzCore/CAMetalDrawable) object may only be usable as attachments, depending on the value of [`framebufferOnly`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer/framebufferOnly) passed to their parent [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer) object. Textures created directly by the app do not have such restrictions.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/isframebufferonly)*