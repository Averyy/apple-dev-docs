# rate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The synthesizer’s speaking rate (words per minute).

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

## Declaration

```swift
var rate: Float { get set }
```

```objc
@property float rate;
```

## Discussion

The range of supported rates is not predefined by the Speech Synthesis framework; but the synthesizer may only respond to a limited range of speech rates. Average human speech occurs at a rate of 180 to 220 words per minute.

## See Also

### Configuring Speech Synthesizers
- [var usesFeedbackWindow: Bool](./usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](./voice%28%29.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](./setvoice%28_%29.md)
  Sets the receiver’s current voice.
- [var volume: Float](./volume.md)
  The synthesizer’s speaking volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/rate)*