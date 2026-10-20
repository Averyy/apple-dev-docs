# bitRateStrategy

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A key value constant the framework uses during encoding.

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
var bitRateStrategy: String? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSString * bitRateStrategy;
```

#### Discussion

This property returns `nil` if you’re not encoding. For information about possible values, see [`AVEncoderBitRateStrategyKey`](../avencoderbitratestrategykey.md).

## See Also

### Getting bit rate properties
- [var applicableEncodeBitRates: [NSNumber]?](./applicableencodebitrates.md)
  An array of bit rates the framework applies during encoding according to the current formats and settings.
- [var availableEncodeBitRates: [NSNumber]?](./availableencodebitrates.md)
  An array of all bit rates the codec provides when encoding.
- [var availableEncodeChannelLayoutTags: [NSNumber]?](./availableencodechannellayouttags.md)
  An array of all output channel layout tags the codec provides when encoding.
- [var bitRate: Int](./bitrate.md)
  The bit rate, in bits per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/bitratestrategy)*