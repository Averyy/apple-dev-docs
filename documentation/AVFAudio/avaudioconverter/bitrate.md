# bitRate

**Framework**: AVFAudio  
**Kind**: property

The bit rate, in bits per second.

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
var bitRate: Int { get set }
```

#### Discussion

This value only applies when encoding.

## See Also

- [var applicableEncodeBitRates: [NSNumber]?](avaudioconverter/applicableencodebitrates.md)
  An array of bit rates the framework applies during encoding according to the current formats and settings.
- [var availableEncodeBitRates: [NSNumber]?](avaudioconverter/availableencodebitrates.md)
  An array of all bit rates the codec provides when encoding.
- [var availableEncodeChannelLayoutTags: [NSNumber]?](avaudioconverter/availableencodechannellayouttags.md)
  An array of all output channel layout tags the codec provides when encoding.
- [var bitRateStrategy: String?](avaudioconverter/bitratestrategy.md)
  A key value constant the framework uses during encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/bitrate)*