# sampleRateConverterAlgorithm

**Framework**: AVFAudio  
**Kind**: property

The priming method the sample rate converter or decoder uses.

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
var sampleRateConverterAlgorithm: String? { get set }
```

## Topics

### Algorithms
- [let AVSampleRateConverterAlgorithm_Normal: String](avsamplerateconverteralgorithm_normal.md)
  The usual encoder bit rate strategy.
- [let AVSampleRateConverterAlgorithm_MinimumPhase: String](avsamplerateconverteralgorithm_minimumphase.md)
  The minimum phase encoder bit rate strategy.
- [let AVSampleRateConverterAlgorithm_Mastering: String](avsamplerateconverteralgorithm_mastering.md)
  The mastering encoder bit rate strategy.

## See Also

- [var sampleRateConverterQuality: Int](avaudioconverter/samplerateconverterquality.md)
  A sample rate converter algorithm key value.
- [var applicableEncodeSampleRates: [NSNumber]?](avaudioconverter/applicableencodesamplerates.md)
  An array of output sample rates that the converter applies according to the current formats and settings, when encoding.
- [var availableEncodeSampleRates: [NSNumber]?](avaudioconverter/availableencodesamplerates.md)
  An array of all output sample rates the codec provides when encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/samplerateconverteralgorithm)*