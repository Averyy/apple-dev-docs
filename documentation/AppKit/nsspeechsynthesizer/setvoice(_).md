# setVoice(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s current voice.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
func setVoice(_ voice: NSSpeechSynthesizer.VoiceName?) -> Bool
```

```objc
- (BOOL) setVoice:(NSSpeechSynthesizerVoiceName) voice;
```

#### Return Value

[`true`](../../Swift/true.md) when the receiver is not currently synthesizing speech and the current voice is set successfully, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `voice`: Identifier of the voice to set at the receiver’s current voice. When `nil`, the receiver sets the default voice as its current voice.

## See Also

### Related Documentation
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](./defaultvoice.md)
  Provides the identifier of the default voice.
### Configuring Speech Synthesizers
- [var usesFeedbackWindow: Bool](./usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](./voice%28%29.md)
  Returns the identifier of the receiver’s current voice.
- [var rate: Float](./rate.md)
  The synthesizer’s speaking rate (words per minute).
- [var volume: Float](./volume.md)
  The synthesizer’s speaking volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/setvoice(_:))*