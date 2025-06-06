# availableEncodeChannelLayoutTags

**Framework**: AVFAudio  
**Kind**: property

An array of all output channel layout tags the codec provides when encoding.

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
var availableEncodeChannelLayoutTags: [NSNumber]? { get }
```

#### Discussion

This property returns `nil` if you’re not encoding.

## See Also

- [var applicableEncodeBitRates: [NSNumber]?](avaudioconverter/applicableencodebitrates.md)
  An array of bit rates the framework applies during encoding according to the current formats and settings.
- [var availableEncodeBitRates: [NSNumber]?](avaudioconverter/availableencodebitrates.md)
  An array of all bit rates the codec provides when encoding.
- [var bitRate: Int](avaudioconverter/bitrate.md)
  The bit rate, in bits per second.
- [var bitRateStrategy: String?](avaudioconverter/bitratestrategy.md)
  A key value constant the framework uses during encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/availableencodechannellayouttags)*