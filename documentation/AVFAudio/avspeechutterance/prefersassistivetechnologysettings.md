# prefersAssistiveTechnologySettings

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean that specifies whether assistive technology settings take precedence over the property values of this utterance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var prefersAssistiveTechnologySettings: Bool { get set }
```

```objc
@property (nonatomic) BOOL prefersAssistiveTechnologySettings;
```

## Discussion

If this property is `true`, but no assistive technology, such as VoiceOver, is on, the speech synthesizer uses the utterance property values.

## See Also

### Configuring an utterance
- [var voice: AVSpeechSynthesisVoice?](./voice.md)
  The voice the speech synthesizer uses when speaking the utterance.
- [var pitchMultiplier: Float](./pitchmultiplier.md)
  The baseline pitch the speech synthesizer uses when speaking the utterance.
- [var volume: Float](./volume.md)
  The volume the speech synthesizer uses when speaking the utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/prefersassistivetechnologysettings)*