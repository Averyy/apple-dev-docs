# MTLTextureSwizzle

**Framework**: Metal  
**Kind**: enum

A set of options to choose from when creating a texture swizzle pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLTextureSwizzle
```

## Topics

### Specifying swizzle channels
- [MTLTextureSwizzle.alpha](mtltextureswizzle/alpha.md)
  The alpha channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzle.blue](mtltextureswizzle/blue.md)
  The blue channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzle.green](mtltextureswizzle/green.md)
  The green channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzle.red](mtltextureswizzle/red.md)
  The red channel of the source pixel is copied to the destination channel.
- [MTLTextureSwizzle.one](mtltextureswizzle/one.md)
  A value of `1.0` is copied to the destination channel.
- [MTLTextureSwizzle.zero](mtltextureswizzle/zero.md)
  A value of `0.0` is copied to the destination channel.
### Initializers
- [init?(rawValue: UInt8)](mtltextureswizzle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var arrayLength: Int](mtltexturedescriptor/arraylength.md)
  The number of array elements for this texture.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltextureswizzle)*