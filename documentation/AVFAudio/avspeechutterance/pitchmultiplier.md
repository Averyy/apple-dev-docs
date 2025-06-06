# pitchMultiplier

**Framework**: AVFAudio  
**Kind**: property

The baseline pitch the speech synthesizer uses when speaking the utterance.

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
var pitchMultiplier: Float { get set }
```

#### Discussion

Before enqueing the utterance, set this property to a value within the range of `0.5` for lower pitch to `2.0` for higher pitch. The default value is `1.0`. Setting this after enqueing the utterance has no effect.

## See Also

- [var voice: AVSpeechSynthesisVoice?](avspeechutterance/voice.md)
  The voice the speech synthesizer uses when speaking the utterance.
- [var volume: Float](avspeechutterance/volume.md)
  The volume the speech synthesizer uses when speaking the utterance.
- [var prefersAssistiveTechnologySettings: Bool](avspeechutterance/prefersassistivetechnologysettings.md)
  A Boolean that specifies whether assistive technology settings take precedence over the property values of this utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/pitchmultiplier)*