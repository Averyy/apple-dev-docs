# volume

**Framework**: AppKit  
**Kind**: property

The synthesizer’s speaking volume.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var volume: Float { get set }
```

#### Discussion

Volumes are expressed in floating-point units ranging from 0.0 through 1.0. A value of 0.0 corresponds to silence, and a value of 1.0 corresponds to the maximum possible volume. Volume units lie on a scale that is linear with amplitude or voltage. A doubling of perceived loudness corresponds to a doubling of the volume. Setting a value outside this range is undefined.

## See Also

- [var usesFeedbackWindow: Bool](nsspeechsynthesizer/usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](nsspeechsynthesizer/voice.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](nsspeechsynthesizer/setvoice(_:).md)
  Sets the receiver’s current voice.
- [var rate: Float](nsspeechsynthesizer/rate.md)
  The synthesizer’s speaking rate (words per minute).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/volume)*