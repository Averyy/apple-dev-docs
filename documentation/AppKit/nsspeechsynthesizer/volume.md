# volume

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The synthesizer’s speaking volume.

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

## Declaration

```swift
var volume: Float { get set }
```

```objc
@property float volume;
```

#### Discussion

Volumes are expressed in floating-point units ranging from 0.0 through 1.0. A value of 0.0 corresponds to silence, and a value of 1.0 corresponds to the maximum possible volume. Volume units lie on a scale that is linear with amplitude or voltage. A doubling of perceived loudness corresponds to a doubling of the volume. Setting a value outside this range is undefined.

## See Also

### Configuring Speech Synthesizers
- [var usesFeedbackWindow: Bool](./usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](./voice%28%29.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](./setvoice%28_%29.md)
  Sets the receiver’s current voice.
- [var rate: Float](./rate.md)
  The synthesizer’s speaking rate (words per minute).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/volume)*