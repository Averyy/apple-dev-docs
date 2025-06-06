# voice

**Framework**: AVFAudio  
**Kind**: property

The voice the speech synthesizer uses when speaking the utterance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var voice: AVSpeechSynthesisVoice? { get set }
```

#### Discussion

If you don’t specify a voice, the speech synthesizer uses the system’s default voice to speak the utterance.

## See Also

- [var pitchMultiplier: Float](avspeechutterance/pitchmultiplier.md)
  The baseline pitch the speech synthesizer uses when speaking the utterance.
- [var volume: Float](avspeechutterance/volume.md)
  The volume the speech synthesizer uses when speaking the utterance.
- [var prefersAssistiveTechnologySettings: Bool](avspeechutterance/prefersassistivetechnologysettings.md)
  A Boolean that specifies whether assistive technology settings take precedence over the property values of this utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/voice)*