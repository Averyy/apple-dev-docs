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

The property’s default value is [`MTLSamplerReductionMode.weightedAverage`](mtlsamplerreductionmode/weightedaverage.md). The sampler ignores this property if any of the following property values are equal to a specific value:

- The sampler’s [`mipFilter`](mtlsamplerdescriptor/mipfilter.md) property is equal to [`MTLSamplerMipFilter.notMipmapped`](mtlsamplermipfilter/notmipmapped.md).
- The sampler’s [`mipFilter`](mtlsamplerdescriptor/mipfilter.md) property is equal to [`MTLSamplerMipFilter.nearest`](mtlsamplermipfilter/nearest.md).
- The sampler’s [`minFilter`](mtlsamplerdescriptor/minfilter.md) property is equal to [`MTLSamplerMinMagFilter.nearest`](mtlsamplerminmagfilter/nearest.md).
- The sampler’s [`magFilter`](mtlsamplerdescriptor/magfilter.md) property is equal to [`MTLSamplerMinMagFilter.nearest`](mtlsamplerminmagfilter/nearest.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/reductionmode)*