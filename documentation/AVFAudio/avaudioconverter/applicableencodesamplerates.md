# applicableEncodeSampleRates

**Framework**: AVFAudio  
**Kind**: property

An array of output sample rates that the converter applies according to the current formats and settings, when encoding.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var applicableEncodeSampleRates: [NSNumber]? { get }
```

#### Discussion

This property returns `nil` if you’re not encoding.

## See Also

- [var sampleRateConverterQuality: Int](avaudioconverter/samplerateconverterquality.md)
  A sample rate converter algorithm key value.
- [var sampleRateConverterAlgorithm: String?](avaudioconverter/samplerateconverteralgorithm.md)
  The priming method the sample rate converter or decoder uses.
- [var availableEncodeSampleRates: [NSNumber]?](avaudioconverter/availableencodesamplerates.md)
  An array of all output sample rates the codec provides when encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/applicableencodesamplerates)*