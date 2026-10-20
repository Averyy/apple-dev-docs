# isVoiceProcessingAGCEnabled

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether automatic gain control on the processed microphone uplink signal is active.

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
var isVoiceProcessingAGCEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isVoiceProcessingAGCEnabled) BOOL voiceProcessingAGCEnabled;
```

#### Discussion

This property is in an enabled state by default.

## See Also

### Configuring voice processing
- [var isVoiceProcessingInputMuted: Bool](./isvoiceprocessinginputmuted.md)
  A Boolean that indicates whether the input of the voice processing unit is in a muted state.
- [var isVoiceProcessingBypassed: Bool](./isvoiceprocessingbypassed.md)
  A Boolean that indicates whether the node bypasses all microphone uplink processing of the voice-processing unit.
- [var voiceProcessingOtherAudioDuckingConfiguration: AVAudioVoiceProcessingOtherAudioDuckingConfiguration](./voiceprocessingotheraudioduckingconfiguration.md)
  The ducking configuration of nonvoice audio.
- [struct AVAudioVoiceProcessingOtherAudioDuckingConfiguration](../avaudiovoiceprocessingotheraudioduckingconfiguration.md)
  The configuration of ducking non-voice audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioinputnode/isvoiceprocessingagcenabled)*