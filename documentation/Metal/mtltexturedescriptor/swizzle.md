# swizzle

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The pattern you want the GPU to apply to pixels when you read or sample pixels from the texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var swizzle: MTLTextureSwizzleChannels { get set }
```

```objc
@property (nonatomic, readwrite) MTLTextureSwizzleChannels swizzle;
```

#### Discussion

The default value does not apply a transformation to pixels sampled or read from the texture.

## See Also

### Specifying texture attributes
- [var textureType: MTLTextureType](./texturetype.md)
  The dimension and arrangement of texture image data.
- [var pixelFormat: MTLPixelFormat](./pixelformat.md)
  The size and bit layout of all pixels in the texture.
- [var width: Int](./width.md)
  The width of the texture image for the base level mipmap, in pixels.
- [var height: Int](./height.md)
  The height of the texture image for the base level mipmap, in pixels.
- [var depth: Int](./depth.md)
  The depth of the texture image for the base level mipmap, in pixels.
- [var mipmapLevelCount: Int](./mipmaplevelcount.md)
  The number of mipmap levels for this texture.
- [var sampleCount: Int](./samplecount.md)
  The number of samples in each fragment.
- [var arrayLength: Int](./arraylength.md)
  The number of array elements for this texture.
- [var resourceOptions: MTLResourceOptions](./resourceoptions.md)
  The behavior of a new memory allocation.
- [var cpuCacheMode: MTLCPUCacheMode](./cpucachemode.md)
  The CPU cache mode used for the CPU mapping of the texture.
- [var storageMode: MTLStorageMode](./storagemode.md)
  The location and access permissions of the texture.
- [var hazardTrackingMode: MTLHazardTrackingMode](./hazardtrackingmode.md)
  The texture’s hazard tracking mode.
- [var allowGPUOptimizedContents: Bool](./allowgpuoptimizedcontents.md)
  A Boolean value indicating whether the GPU is allowed to adjust the texture’s contents to improve GPU performance.
- [var usage: MTLTextureUsage](./usage.md)
  Options that determine how you can use the texture.
- [struct MTLTextureSwizzleChannels](../mtltextureswizzlechannels.md)
  A pattern that modifies the data read or sampled from a texture by rearranging or duplicating the elements of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturedescriptor/swizzle)*