# volume

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The volume the speech synthesizer uses when speaking the utterance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var volume: Float { get set }
```

```objc
@property (nonatomic) float volume;
```

#### Discussion

Before enqueing the utterance, set this property to a value within the range of `0.0` for silent to `1.0` for loudest volume. The default value is `1.0`. Setting this after enqueing the utterance has no effect.

## See Also

### Configuring an utterance
- [var voice: AVSpeechSynthesisVoice?](./voice.md)
  The voice the speech synthesizer uses when speaking the utterance.
- [var pitchMultiplier: Float](./pitchmultiplier.md)
  The baseline pitch the speech synthesizer uses when speaking the utterance.
- [var prefersAssistiveTechnologySettings: Bool](./prefersassistivetechnologysettings.md)
  A Boolean that specifies whether assistive technology settings take precedence over the property values of this utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/volume)*