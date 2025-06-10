# MTLTextureType

**Framework**: Metal  
**Kind**: enum

The dimension of each image, including whether multiple images are arranged into an array or a cube.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLTextureType
```

#### Overview

For a `MTLTextureTypeCube` texture, the property values describe one slice, which is any one of its six sides. For example, [`mipmapLevelCount`](mtltexture/mipmaplevelcount.md) is the number of mipmap levels for one slice, not the total sum of mipmap levels in six slices. By definition, the [`width`](mtltexture/width.md) and [`height`](mtltexture/height.md) of a cube texture are the same value.

Each slice of a cube texture maps to a side with a specific orientation.

| Slice index | Slice orientation |
| --- | --- |
| 0 | +X |
| 1 | -X |
| 2 | +Y |
| 3 | -Y |
| 4 | +Z |
| 5 | -Z |

## Topics

### Specifying the Texture Type
- [MTLTextureType.type1D](mtltexturetype/type1d.md)
  A one-dimensional texture image.
- [MTLTextureType.type1DArray](mtltexturetype/type1darray.md)
  An array of one-dimensional texture images.
- [MTLTextureType.type2D](mtltexturetype/type2d.md)
  A two-dimensional texture image.
- [MTLTextureType.type2DArray](mtltexturetype/type2darray.md)
  An array of two-dimensional texture images.
- [MTLTextureType.type2DMultisample](mtltexturetype/type2dmultisample.md)
  A two-dimensional texture image that uses more than one sample for each pixel.
- [MTLTextureType.typeCube](mtltexturetype/typecube.md)
  A cube texture with six two-dimensional images.
- [MTLTextureType.typeCubeArray](mtltexturetype/typecubearray.md)
  An array of cube textures, each with six two-dimensional images.
- [MTLTextureType.type3D](mtltexturetype/type3d.md)
  A three-dimensional texture image.
- [MTLTextureType.type2DMultisampleArray](mtltexturetype/type2dmultisamplearray.md)
  An array of two-dimensional texture images that use more than one sample for each pixel.
- [MTLTextureType.typeTextureBuffer](mtltexturetype/typetexturebuffer.md)
  A texture buffer.
### Initializers
- [init?(rawValue: UInt)](mtltexturetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct MTLTextureUsage](mtltextureusage.md)
  An enumeration for the various options that determine how you can use a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturetype)*