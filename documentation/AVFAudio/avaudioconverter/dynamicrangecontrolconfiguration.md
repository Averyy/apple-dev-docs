# dynamicRangeControlConfiguration

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var dynamicRangeControlConfiguration: AVAudioDynamicRangeControlConfiguration { get set }
```

```objc
@property (nonatomic) AVAudioDynamicRangeControlConfiguration dynamicRangeControlConfiguration;
```

## Discussion

Encoder Dynamic Range Control (DRC) configuration.

When supported by the encoder, this property controls which configuration is applied when a bitstream is generated.  Note: This is only supported when compressing audio to formats which support it.

## See Also

### Managing packet dependencies
- [var audioSyncPacketFrequency: Int](./audiosyncpacketfrequency.md)
- [var contentSource: AVAudioContentSource](./contentsource.md)
- [enum AVAudioContentSource](../avaudiocontentsource.md)
- [enum AVAudioDynamicRangeControlConfiguration](../avaudiodynamicrangecontrolconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/dynamicrangecontrolconfiguration)*