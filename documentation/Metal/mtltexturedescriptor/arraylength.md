# arrayLength

**Framework**: Metal  
**Kind**: property

The number of array elements for this texture.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var arrayLength: Int { get set }
```

#### Discussion

The value of this property must be between `1` and `2048`, inclusive. The default value is `1`.

This value is `1` if the texture type is not an array.

This value can be between `1` and `2048` if the texture type is one of the following array types:

- [`MTLTextureType.type1DArray`](mtltexturetype/type1darray.md)
- [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md)
- [`MTLTextureType.type2DMultisampleArray`](mtltexturetype/type2dmultisamplearray.md)
- [`MTLTextureType.typeCubeArray`](mtltexturetype/typecubearray.md)

## See Also

- [var textureType: MTLTextureType](mtltexturedescriptor/texturetype.md)
  The dimension and arrangement of texture image data.
- [var pixelFormat: MTLPixelFormat](mtltexturedescriptor/pixelformat.md)
  The size and bit layout of all pixels in the texture.
- [var width: Int](mtltexturedescriptor/width.md)
  The width of the texture image for the base level mipmap, in pixels.
- [var height: Int](mtltexturedescriptor/height.md)
  The height of the texture image for the base level mipmap, in pixels.
- [var depth: Int](mtltexturedescriptor/depth.md)
  The depth of the texture image for the base level mipmap, in pixels.
- [var mipmapLevelCount: Int](mtltexturedescriptor/mipmaplevelcount.md)
  The number of mipmap levels for this texture.
- [var sampleCount: Int](mtltexturedescriptor/samplecount.md)
  The number of samples in each fragment.
- [var resourceOptions: MTLResourceOptions](mtltexturedescriptor/resourceoptions.md)
  The behavior of a new memory allocation.
- [var cpuCacheMode: MTLCPUCacheMode](mtltexturedescriptor/cpucachemode.md)
  The CPU cache mode used for the CPU mapping of the texture.
- [var storageMode: MTLStorageMode](mtltexturedescriptor/storagemode.md)
  The location and access permissions of the texture.
- [var hazardTrackingMode: MTLHazardTrackingMode](mtltexturedescriptor/hazardtrackingmode.md)
  The texture’s hazard tracking mode.
- [var allowGPUOptimizedContents: Bool](mtltexturedescriptor/allowgpuoptimizedcontents.md)
  A Boolean value indicating whether the GPU is allowed to adjust the texture’s contents to improve GPU performance.
- [var usage: MTLTextureUsage](mtltexturedescriptor/usage.md)
  Options that determine how you can use the texture.
- [var swizzle: MTLTextureSwizzleChannels](mtltexturedescriptor/swizzle.md)
  The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.
- [struct MTLTextureSwizzleChannels](mtltextureswizzlechannels.md)
  A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/arraylength)*