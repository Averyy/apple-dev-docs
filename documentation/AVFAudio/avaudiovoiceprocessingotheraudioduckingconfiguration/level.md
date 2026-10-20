# AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that define the supported ducking levels.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Level
```

```c
enum AVAudioVoiceProcessingOtherAudioDuckingLevel : NSInteger;
```

## Topics

### Creating a ducking level
- [init?(rawValue: Int)](./level/init%28rawvalue%29.md)
### Choosing a ducking level
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.default](./level/default.md)
  The default ducking level for typical voice chat.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.max](./level/max.md)
  Applies maximum ducking to other audio.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.mid](./level/mid.md)
  Applies medium ducking to other audio.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.min](./level/min.md)
  Applies minimum ducking to other audio.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring ducking
- [var enableAdvancedDucking: ObjCBool](./enableadvancedducking.md)
  Enables advanced ducking which ducks other audio based on the presence of voice activity from local and remote chat participants.
- [var duckingLevel: AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level](./duckinglevel.md)
  The ducking level of other audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiovoiceprocessingotheraudioduckingconfiguration/level)*