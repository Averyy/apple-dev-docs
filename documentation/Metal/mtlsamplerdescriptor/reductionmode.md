# reductionMode

**Framework**: Metal  
**Kind**: property

Sets the reduction mode for filtering contributing samples.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var reductionMode: MTLSamplerReductionMode { get set }
```

#### Discussion

The property’s default value is `MTLSamplerReductionModeWeightedAverage`. The sampler ignores this property if any of the following property values are equal to a specific value:

- The sampler’s [`mipFilter`](mtlsamplerdescriptor/mipfilter.md) property is equal to `MTLSamplerMipFilterNotMipmapped`.
- The sampler’s [`mipFilter`](mtlsamplerdescriptor/mipfilter.md) property is equal to `MTLSamplerMipFilterNearest`.
- The sampler’s [`minFilter`](mtlsamplerdescriptor/minfilter.md) property is equal to `MTLSamplerMinMagFilterNearest`.
- The sampler’s [`magFilter`](mtlsamplerdescriptor/magfilter.md) property is equal to `MTLSamplerMinMagFilterNearest`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/reductionmode)*