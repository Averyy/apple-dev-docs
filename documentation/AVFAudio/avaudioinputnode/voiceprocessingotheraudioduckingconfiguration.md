# voiceProcessingOtherAudioDuckingConfiguration

**Framework**: AVFAudio  
**Kind**: property

The ducking configuration of nonvoice audio.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var voiceProcessingOtherAudioDuckingConfiguration: AVAudioVoiceProcessingOtherAudioDuckingConfiguration { get set }
```

#### Discussion

Use this property to configures the ducking of nonvoice audio, including advanced enablement and ducking level. Typically, when playing other audio during voice chat, applying a higher level of ducking can increase the intelligibility of the voice chat.

If not set, the default behavior is to disable advanced ducking, with a ducking level set to [`AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level.default`](avaudiovoiceprocessingotheraudioduckingconfiguration/level/default.md).

## See Also

- [var isVoiceProcessingInputMuted: Bool](avaudioinputnode/isvoiceprocessinginputmuted.md)
  A Boolean that indicates whether the input of the voice processing unit is in a muted state.
- [var isVoiceProcessingBypassed: Bool](avaudioinputnode/isvoiceprocessingbypassed.md)
  A Boolean that indicates whether the node bypasses all microphone uplink processing of the voice-processing unit.
- [var isVoiceProcessingAGCEnabled: Bool](avaudioinputnode/isvoiceprocessingagcenabled.md)
  A Boolean that indicates whether automatic gain control on the processed microphone uplink signal is active.
- [struct AVAudioVoiceProcessingOtherAudioDuckingConfiguration](avaudiovoiceprocessingotheraudioduckingconfiguration.md)
  The configuration of ducking non-voice audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioinputnode/voiceprocessingotheraudioduckingconfiguration)*