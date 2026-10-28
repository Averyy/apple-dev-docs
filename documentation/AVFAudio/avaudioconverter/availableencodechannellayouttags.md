# availableEncodeChannelLayoutTags

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An array of all output channel layout tags the codec provides when encoding.

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
var availableEncodeChannelLayoutTags: [NSNumber]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSNumber *> * availableEncodeChannelLayoutTags;
```

## Discussion

This property returns `nil` if you’re not encoding.

## See Also

### Getting bit rate properties
- [var applicableEncodeBitRates: [NSNumber]?](./applicableencodebitrates.md)
  An array of bit rates the framework applies during encoding according to the current formats and settings.
- [var availableEncodeBitRates: [NSNumber]?](./availableencodebitrates.md)
  An array of all bit rates the codec provides when encoding.
- [var bitRate: Int](./bitrate.md)
  The bit rate, in bits per second.
- [var bitRateStrategy: String?](./bitratestrategy.md)
  A key value constant the framework uses during encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/availableencodechannellayouttags)*