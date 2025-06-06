# mipFilter

**Framework**: Metal  
**Kind**: property

The filtering option for combining pixels between two mipmap levels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var mipFilter: MTLSamplerMipFilter { get set }
```

## Mentions

- [Adding Mipmap Filtering to Samplers](adding-mipmap-filtering-to-samplers.md)

#### Discussion

The default value is [`MTLSamplerMipFilter.notMipmapped`](mtlsamplermipfilter/notmipmapped.md).

## See Also

- [var minFilter: MTLSamplerMinMagFilter](mtlsamplerdescriptor/minfilter.md)
  The filtering option for combining pixels within one mipmap level when the sample footprint is larger than a pixel (minification).
- [var magFilter: MTLSamplerMinMagFilter](mtlsamplerdescriptor/magfilter.md)
  The filtering operation for combining pixels within one mipmap level when the sample footprint is smaller than a pixel (magnification).
- [var lodMinClamp: Float](mtlsamplerdescriptor/lodminclamp.md)
  The minimum level of detail (LOD) to use when sampling from a texture.
- [var lodMaxClamp: Float](mtlsamplerdescriptor/lodmaxclamp.md)
  The maximum level of detail (LOD) to use when sampling from a texture.
- [var lodAverage: Bool](mtlsamplerdescriptor/lodaverage.md)
  A Boolean value that specifies whether the GPU can use an average level of detail (LOD) when sampling from a texture.
- [var maxAnisotropy: Int](mtlsamplerdescriptor/maxanisotropy.md)
  The number of samples that can be taken to improve the quality of sample footprints that are anisotropic.
- [enum MTLSamplerMinMagFilter](mtlsamplerminmagfilter.md)
  Filtering options for determining which pixel value is returned within a mipmap level.
- [enum MTLSamplerMipFilter](mtlsamplermipfilter.md)
  Filtering options for determining what pixel value is returned with multiple mipmap levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/mipfilter)*