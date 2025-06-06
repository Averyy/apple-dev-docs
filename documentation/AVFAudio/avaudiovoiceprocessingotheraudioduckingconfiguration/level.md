# AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level

**Framework**: AVFAudio  
**Kind**: enum

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

## Topics

### Ducking levels
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.default](avaudiovoiceprocessingotheraudioduckingconfiguration/level/default.md)
  The default ducking level for typical voice chat.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.max](avaudiovoiceprocessingotheraudioduckingconfiguration/level/max.md)
  Applies maximum ducking to other audio.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.mid](avaudiovoiceprocessingotheraudioduckingconfiguration/level/mid.md)
  Applies medium ducking to other audio.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.min](avaudiovoiceprocessingotheraudioduckingconfiguration/level/min.md)
  Applies minimum ducking to other audio.
### Initializers
- [init?(rawValue: Int)](avaudiovoiceprocessingotheraudioduckingconfiguration/level/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var enableAdvancedDucking: ObjCBool](avaudiovoiceprocessingotheraudioduckingconfiguration/enableadvancedducking.md)
  Enables advanced ducking which ducks other audio based on the presence of voice activity from local and remote chat participants.
- [var duckingLevel: AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level](avaudiovoiceprocessingotheraudioduckingconfiguration/duckinglevel.md)
  The ducking level of other audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiovoiceprocessingotheraudioduckingconfiguration/level)*