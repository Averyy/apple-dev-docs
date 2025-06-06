# kAudioUnitSubType_VoiceProcessingIO

**Framework**: Audio Toolbox  
**Kind**: var

An audio unit that interfaces to the audio inputs and outputs of iOS devices and provides voice processing features.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitSubType_VoiceProcessingIO: UInt32 { get }
```

#### Discussion

Bus 0 provides output to hardware and bus 1 accepts input from hardware. See [`Audio Unit Voice I/O`](audio-unit-voice-i-o.md) for the identifiers for this audio unit’s properties.

## See Also

- [var kAudioUnitSubType_GenericOutput: UInt32](kaudiounitsubtype_genericoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_voiceprocessingio)*