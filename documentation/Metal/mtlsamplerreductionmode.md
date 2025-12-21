# MTLSamplerReductionMode

**Framework**: Metal  
**Kind**: enum

Configures how the sampler aggregates contributing samples to a final value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MTLSamplerReductionMode
```

## Topics

### Enumeration Cases
- [MTLSamplerReductionMode.maximum](mtlsamplerreductionmode/maximum.md)
  A reduction mode that finds the maximum contributing sample value by separately evaluating each channel.
- [MTLSamplerReductionMode.minimum](mtlsamplerreductionmode/minimum.md)
  A reduction mode that finds the minimum contributing sample value by separately evaluating each channel.
- [MTLSamplerReductionMode.weightedAverage](mtlsamplerreductionmode/weightedaverage.md)
  A reduction mode that adds together the product of each contributing sample value by its weight.
### Initializers
- [init?(rawValue: UInt)](mtlsamplerreductionmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating and sampling textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.
- [protocol MTLSamplerState](mtlsamplerstate.md)
  An instance that defines how a texture should be sampled.
- [class MTLSamplerDescriptor](mtlsamplerdescriptor.md)
  An object that you use to configure a texture sampler.
- [struct MTLSamplePosition](mtlsampleposition.md)
  A subpixel sample position for use in multisample antialiasing (MSAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerreductionmode)*