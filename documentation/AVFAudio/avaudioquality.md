# AVAudioQuality

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The values that specify the sample rate audio quality for encoding and conversion.

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
enum AVAudioQuality
```

```c
enum AVAudioQuality : NSInteger;
```

## Overview

You use this value with [`AVEncoderAudioQualityKey`](./avencoderaudioqualitykey.md) and [`AVSampleRateConverterAudioQualityKey`](./avsamplerateconverteraudioqualitykey.md).

## Topics

### Creating a quality level
- [init?(rawValue: Int)](./avaudioquality/init%28rawvalue%29.md)
### Choosing a quality level
- [AVAudioQuality.min](./avaudioquality/min.md)
  A value that represents a minimum audio quality for encoding and conversion.
- [AVAudioQuality.low](./avaudioquality/low.md)
  A value that represents a low audio quality for encoding and conversion.
- [AVAudioQuality.medium](./avaudioquality/medium.md)
  A value that represents a medium audio quality for encoding and conversion.
- [AVAudioQuality.high](./avaudioquality/high.md)
  A value that represents a high audio quality for encoding and conversion.
- [AVAudioQuality.max](./avaudioquality/max.md)
  A value that represents a maximum audio quality for encoding and conversion.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Encoder and processing settings
- [Sample rate conversion settings](./sample-rate-conversion-settings.md)
  The constants that define sample rate converter audio quality settings.
- [Encoder settings](./encoder-settings.md)
  The constants that define the audio encoder settings for the audio recorder class.
- [Time pitch algorithm settings](../AVFoundation/time-pitch-algorithm-settings.md)
  The constants that define the values for the time pitch algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioquality)*