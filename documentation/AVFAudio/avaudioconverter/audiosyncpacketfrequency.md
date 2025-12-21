# audioSyncPacketFrequency

**Framework**: AVFAudio  
**Kind**: property

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
var audioSyncPacketFrequency: Int { get set }
```

#### Discussion

Number of packets between consecutive sync packets.

A sync packet is an independently-decodable packet that completely refreshes the decoder without needing to decode other packets.  When compressing to a format which supports it (such as APAC), the audio sync packet frequency indicates the distance in packets between two sync packets, with non-sync packets between.  This is useful to set when saving compressed packets to a file and efficient random access is desired.  Note: Separating sync packets by at least one second of encoded audio (e.g. 75 packets) is recommended.

## See Also

- [var contentSource: AVAudioContentSource](avaudioconverter/contentsource.md)
- [enum AVAudioContentSource](avaudiocontentsource.md)
- [var dynamicRangeControlConfiguration: AVAudioDynamicRangeControlConfiguration](avaudioconverter/dynamicrangecontrolconfiguration.md)
- [enum AVAudioDynamicRangeControlConfiguration](avaudiodynamicrangecontrolconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter/audiosyncpacketfrequency)*