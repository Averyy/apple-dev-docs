# rate

**Framework**: AppKit  
**Kind**: property

The synthesizer’s speaking rate (words per minute).

**Availability**:
- macOS 10.5+

## Declaration

```swift
var rate: Float { get set }
```

#### Discussion

The range of supported rates is not predefined by the Speech Synthesis framework; but the synthesizer may only respond to a limited range of speech rates. Average human speech occurs at a rate of 180 to 220 words per minute.

## See Also

- [var usesFeedbackWindow: Bool](nsspeechsynthesizer/usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](nsspeechsynthesizer/voice.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](nsspeechsynthesizer/setvoice(_:).md)
  Sets the receiver’s current voice.
- [var volume: Float](nsspeechsynthesizer/volume.md)
  The synthesizer’s speaking volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/rate)*