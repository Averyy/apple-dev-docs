# voice()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the identifier of the receiver’s current voice.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
func voice() -> NSSpeechSynthesizer.VoiceName?
```

```objc
- (NSSpeechSynthesizerVoiceName) voice;
```

## Return Value

Identifier of the receiver’s current voice.

## See Also

### Configuring Speech Synthesizers
- [var usesFeedbackWindow: Bool](./usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](./setvoice%28_%29.md)
  Sets the receiver’s current voice.
- [var rate: Float](./rate.md)
  The synthesizer’s speaking rate (words per minute).
- [var volume: Float](./volume.md)
  The synthesizer’s speaking volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voice())*