# AVAudioVoiceProcessingOtherAudioDuckingConfiguration

**Framework**: AVFAudio  
**Kind**: struct

The configuration of ducking non-voice audio.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct AVAudioVoiceProcessingOtherAudioDuckingConfiguration
```

## Topics

### Configuring ducking
- [var enableAdvancedDucking: ObjCBool](avaudiovoiceprocessingotheraudioduckingconfiguration/enableadvancedducking.md)
  Enables advanced ducking which ducks other audio based on the presence of voice activity from local and remote chat participants.
- [var duckingLevel: AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level](avaudiovoiceprocessingotheraudioduckingconfiguration/duckinglevel.md)
  The ducking level of other audio.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level](avaudiovoiceprocessingotheraudioduckingconfiguration/level.md)
  Constants that define the supported ducking levels.
### Initializers
- [init()](avaudiovoiceprocessingotheraudioduckingconfiguration/init.md)
- [init(enableAdvancedDucking: ObjCBool, duckingLevel: AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level)](avaudiovoiceprocessingotheraudioduckingconfiguration/init(enableadvancedducking:duckinglevel:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isVoiceProcessingInputMuted: Bool](avaudioinputnode/isvoiceprocessinginputmuted.md)
  A Boolean that indicates whether the input of the voice processing unit is in a muted state.
- [var isVoiceProcessingBypassed: Bool](avaudioinputnode/isvoiceprocessingbypassed.md)
  A Boolean that indicates whether the node bypasses all microphone uplink processing of the voice-processing unit.
- [var isVoiceProcessingAGCEnabled: Bool](avaudioinputnode/isvoiceprocessingagcenabled.md)
  A Boolean that indicates whether automatic gain control on the processed microphone uplink signal is active.
- [var voiceProcessingOtherAudioDuckingConfiguration: AVAudioVoiceProcessingOtherAudioDuckingConfiguration](avaudioinputnode/voiceprocessingotheraudioduckingconfiguration.md)
  The ducking configuration of nonvoice audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiovoiceprocessingotheraudioduckingconfiguration)*