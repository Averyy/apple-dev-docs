# AVAudioConverterPrimeMethod

**Framework**: AVFAudio  
**Kind**: enum

Options for the prime method property.

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
enum AVAudioConverterPrimeMethod
```

#### Overview

For more information, see [`AVAudioConverterPrimeInfo`](avaudioconverterprimeinfo.md).

## Topics

### Options
- [AVAudioConverterPrimeMethod.pre](avaudioconverterprimemethod/pre.md)
  An option to prime with leading and trailing input frames.
- [AVAudioConverterPrimeMethod.normal](avaudioconverterprimemethod/normal.md)
  An option to prime with trailing (zero latency) frames where the converter assumes the leading frames are silence.
- [AVAudioConverterPrimeMethod.none](avaudioconverterprimemethod/none.md)
  An option to prime the converter assumes leading and trailing frames are silence.
### Initializers
- [init?(rawValue: Int)](avaudioconverterprimemethod/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var primeInfo: AVAudioConverterPrimeInfo](avaudioconverter/primeinfo.md)
  The number of priming frames the converter uses.
- [var primeMethod: AVAudioConverterPrimeMethod](avaudioconverter/primemethod.md)
  The priming method the sample rate converter or decoder uses.
- [struct AVAudioConverterPrimeInfo](avaudioconverterprimeinfo.md)
  Priming information for audio conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterprimemethod)*