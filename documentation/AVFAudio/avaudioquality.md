# AVAudioQuality

**Framework**: AVFAudio  
**Kind**: enum

The values that specify the sample rate audio quality for encoding and conversion.

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
enum AVAudioQuality
```

#### Overview

You use this value with [`AVEncoderAudioQualityKey`](avencoderaudioqualitykey.md) and [`AVSampleRateConverterAudioQualityKey`](avsamplerateconverteraudioqualitykey.md).

## Topics

### Constants
- [AVAudioQuality.min](avaudioquality/min.md)
  A value that represents a minimum audio quality for encoding and conversion.
- [AVAudioQuality.low](avaudioquality/low.md)
  A value that represents a low audio quality for encoding and conversion.
- [AVAudioQuality.medium](avaudioquality/medium.md)
  A value that represents a medium audio quality for encoding and conversion.
- [AVAudioQuality.high](avaudioquality/high.md)
  A value that represents a high audio quality for encoding and conversion.
- [AVAudioQuality.max](avaudioquality/max.md)
  A value that represents a maximum audio quality for encoding and conversion.
### Initializers
- [init?(rawValue: Int)](avaudioquality/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Sample Rate Conversion Settings](sample-rate-conversion-settings.md)
  The constants that define sample rate converter audio quality settings.
- [let AVEncoderAudioQualityKey: String](avencoderaudioqualitykey.md)
  A constant that represents an integer from the audio quality enumeration.
- [Encoder Settings](encoder-settings.md)
  The constants that define the audio encoder settings for the audio recorder class.
- [Time pitch algorithm settings](../AVFoundation/time-pitch-algorithm-settings.md)
  The constants that define the values for the time pitch algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioquality)*