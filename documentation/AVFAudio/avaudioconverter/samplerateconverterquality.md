# sampleRateConverterQuality

**Framework**: AVFAudio  
**Kind**: property

A sample rate converter algorithm key value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sampleRateConverterQuality: Int { get set }
```

#### Discussion

For information about possible key values, see [`AVSampleRateConverterAlgorithmKey`](avsamplerateconverteralgorithmkey.md).

## See Also

- [var sampleRateConverterAlgorithm: String?](avaudioconverter/samplerateconverteralgorithm.md)
  The priming method the sample rate converter or decoder uses.
- [var applicableEncodeSampleRates: [NSNumber]?](avaudioconverter/applicableencodesamplerates.md)
  An array of output sample rates that the converter applies according to the current formats and settings, when encoding.
- [var availableEncodeSampleRates: [NSNumber]?](avaudioconverter/availableencodesamplerates.md)
  An array of all output sample rates the codec provides when encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/samplerateconverterquality)*