# bitRate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The bit rate, in bits per second.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var bitRate: Int { get set }
```

```objc
@property (nonatomic) NSInteger bitRate;
```

#### Discussion

This value only applies when encoding.

## See Also

### Getting bit rate properties
- [var applicableEncodeBitRates: [NSNumber]?](./applicableencodebitrates.md)
  An array of bit rates the framework applies during encoding according to the current formats and settings.
- [var availableEncodeBitRates: [NSNumber]?](./availableencodebitrates.md)
  An array of all bit rates the codec provides when encoding.
- [var availableEncodeChannelLayoutTags: [NSNumber]?](./availableencodechannellayouttags.md)
  An array of all output channel layout tags the codec provides when encoding.
- [var bitRateStrategy: String?](./bitratestrategy.md)
  A key value constant the framework uses during encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/bitrate)*