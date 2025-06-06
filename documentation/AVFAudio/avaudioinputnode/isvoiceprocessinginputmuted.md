# isVoiceProcessingInputMuted

**Framework**: AVFAudio  
**Kind**: property

A Boolean that indicates whether the input of the voice processing unit is in a muted state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isVoiceProcessingInputMuted: Bool { get set }
```

## See Also

- [var isVoiceProcessingBypassed: Bool](avaudioinputnode/isvoiceprocessingbypassed.md)
  A Boolean that indicates whether the node bypasses all microphone uplink processing of the voice-processing unit.
- [var isVoiceProcessingAGCEnabled: Bool](avaudioinputnode/isvoiceprocessingagcenabled.md)
  A Boolean that indicates whether automatic gain control on the processed microphone uplink signal is active.
- [var voiceProcessingOtherAudioDuckingConfiguration: AVAudioVoiceProcessingOtherAudioDuckingConfiguration](avaudioinputnode/voiceprocessingotheraudioduckingconfiguration.md)
  The ducking configuration of nonvoice audio.
- [struct AVAudioVoiceProcessingOtherAudioDuckingConfiguration](avaudiovoiceprocessingotheraudioduckingconfiguration.md)
  The configuration of ducking non-voice audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioinputnode/isvoiceprocessinginputmuted)*