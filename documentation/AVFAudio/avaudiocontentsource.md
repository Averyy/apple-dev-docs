# AVAudioContentSource

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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
enum AVAudioContentSource
```

```c
enum AVAudioContentSource : NSInteger;
```

## Topics

### Creating a content source
- [init?(rawValue: Int)](./avaudiocontentsource/init%28rawvalue%29.md)
### Identifying audiovisual content
- [AVAudioContentSource.appleAV_Spatial_Live](./avaudiocontentsource/appleav_spatial_live.md)
- [AVAudioContentSource.appleAV_Spatial_Offline](./avaudiocontentsource/appleav_spatial_offline.md)
- [AVAudioContentSource.appleAV_Traditional_Live](./avaudiocontentsource/appleav_traditional_live.md)
- [AVAudioContentSource.appleAV_Traditional_Offline](./avaudiocontentsource/appleav_traditional_offline.md)
- [AVAudioContentSource.av_Spatial_Live](./avaudiocontentsource/av_spatial_live.md)
- [AVAudioContentSource.av_Spatial_Offline](./avaudiocontentsource/av_spatial_offline.md)
- [AVAudioContentSource.av_Traditional_Live](./avaudiocontentsource/av_traditional_live.md)
- [AVAudioContentSource.av_Traditional_Offline](./avaudiocontentsource/av_traditional_offline.md)
### Identifying captured content
- [AVAudioContentSource.appleCapture_Spatial_Enhanced](./avaudiocontentsource/applecapture_spatial_enhanced.md)
- [AVAudioContentSource.appleCapture_Spatial](./avaudiocontentsource/applecapture_spatial.md)
- [AVAudioContentSource.appleCapture_Traditional](./avaudiocontentsource/applecapture_traditional.md)
- [AVAudioContentSource.capture_Spatial_Enhanced](./avaudiocontentsource/capture_spatial_enhanced.md)
- [AVAudioContentSource.capture_Spatial](./avaudiocontentsource/capture_spatial.md)
- [AVAudioContentSource.capture_Traditional](./avaudiocontentsource/capture_traditional.md)
### Identifying music content
- [AVAudioContentSource.appleMusic_Spatial](./avaudiocontentsource/applemusic_spatial.md)
- [AVAudioContentSource.appleMusic_Traditional](./avaudiocontentsource/applemusic_traditional.md)
- [AVAudioContentSource.music_Spatial](./avaudiocontentsource/music_spatial.md)
- [AVAudioContentSource.music_Traditional](./avaudiocontentsource/music_traditional.md)
### Identifying passthrough content
- [AVAudioContentSource.applePassthrough](./avaudiocontentsource/applepassthrough.md)
- [AVAudioContentSource.passthrough](./avaudiocontentsource/passthrough.md)
### Using placeholder values
- [AVAudioContentSource.reserved](./avaudiocontentsource/reserved.md)
- [AVAudioContentSource.unspecified](./avaudiocontentsource/unspecified.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing packet dependencies
- [var audioSyncPacketFrequency: Int](./avaudioconverter/audiosyncpacketfrequency.md)
- [var contentSource: AVAudioContentSource](./avaudioconverter/contentsource.md)
- [var dynamicRangeControlConfiguration: AVAudioDynamicRangeControlConfiguration](./avaudioconverter/dynamicrangecontrolconfiguration.md)
- [enum AVAudioDynamicRangeControlConfiguration](./avaudiodynamicrangecontrolconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocontentsource)*