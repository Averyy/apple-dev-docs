# isFramebufferOnly

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the texture can only be used as a render target.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isFramebufferOnly: Bool { get }
```

```objc
@property (readonly, getter=isFramebufferOnly) BOOL framebufferOnly;
```

#### Discussion

The default is [`false`](../../Swift/false.md), which indicates the use of the texture is not restricted.

If [`true`](../../Swift/true.md), neither [`replace(region:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:)`](./replace%28region,mipmaplevel,slice,withbytes,bytesperrow,bytesperimage%29.md) nor [`getBytes(_:bytesPerRow:bytesPerImage:from:mipmapLevel:slice:)`](./getbytes%28_,bytesperrow,bytesperimage,from,mipmaplevel,slice%29.md) can be used with this texture. Also, this texture can only be used as an attachment for [`MTLRenderPassDescriptor`](../mtlrenderpassdescriptor.md) and cannot be a texture argument for [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md), [`MTLBlitCommandEncoder`](../mtlblitcommandencoder.md), or [`MTLComputeCommandEncoder`](../mtlcomputecommandencoder.md).

Textures you obtain from a [`CAMetalDrawable`](../../QuartzCore/cametaldrawable.md) instance are only usable as attachments, depending on the value of [`framebufferOnly`](../../QuartzCore/cametallayer/framebufferonly.md) passed to their parent [`CAMetalLayer`](../../QuartzCore/cametallayer.md) instance. These restrictions don’t apply to textures that your app creates directly.

## See Also

### Querying texture attributes
- [var textureType: MTLTextureType](./texturetype.md)
  The dimension and arrangement of the texture image data.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The format of pixels in the texture.
- [var width: Int](./width.md)
  The width of the texture image for the base level mipmap, in pixels.
- [var height: Int](./height.md)
  The height of the texture image for the base level mipmap, in pixels.
- [var depth: Int](./depth.md)
  The depth of the texture image for the base level mipmap, in pixels.
- [var mipmapLevelCount: Int](./mipmaplevelcount.md)
  The number of mipmap levels in the texture.
- [var arrayLength: Int](./arraylength.md)
  The number of slices in the texture array.
- [var sampleCount: Int](./samplecount.md)
  The number of samples in each pixel.
- [var usage: MTLTextureUsage](./usage.md)
  Options that determine how you can use the texture.
- [var allowGPUOptimizedContents: Bool](./allowgpuoptimizedcontents.md)
  A Boolean value indicating whether the GPU is allowed to adjust the contents of the texture to improve GPU performance.
- [var isShareable: Bool](./isshareable.md)
  A Boolean indicating whether this texture can be shared with other processes.
- [var swizzle: MTLTextureSwizzleChannels](./swizzle.md)
  The pattern that the GPU applies to pixels when you read or sample pixels from the texture.
- [enum MTLTextureType](../mtltexturetype.md)
  The dimension of each image, including whether multiple images are arranged into an array or a cube.
- [struct MTLTextureUsage](../mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/isframebufferonly)*