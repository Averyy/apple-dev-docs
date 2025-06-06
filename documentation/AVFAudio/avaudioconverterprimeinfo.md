# AVAudioConverterPrimeInfo

**Framework**: AVFAudio  
**Kind**: struct

Priming information for audio conversion.

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
struct AVAudioConverterPrimeInfo
```

## Topics

### Creating Priming Information
- [init()](avaudioconverterprimeinfo/init.md)
  Creates a priming information instance.
- [init(leadingFrames: AVAudioFrameCount, trailingFrames: AVAudioFrameCount)](avaudioconverterprimeinfo/init(leadingframes:trailingframes:).md)
  Creates a priming information instance with the specified leading and trailing frames.
### Getting Frame Properties
- [var leadingFrames: AVAudioFrameCount](avaudioconverterprimeinfo/leadingframes.md)
  The number of leading (previous) input frames the converter requires to perform a high-quality conversion.
- [var trailingFrames: AVAudioFrameCount](avaudioconverterprimeinfo/trailingframes.md)
  The number of trailing input frames, past the end input frame, the converter requires to perform a high-quality conversion.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var primeInfo: AVAudioConverterPrimeInfo](avaudioconverter/primeinfo.md)
  The number of priming frames the converter uses.
- [var primeMethod: AVAudioConverterPrimeMethod](avaudioconverter/primemethod.md)
  The priming method the sample rate converter or decoder uses.
- [enum AVAudioConverterPrimeMethod](avaudioconverterprimemethod.md)
  Options for the prime method property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterprimeinfo)*