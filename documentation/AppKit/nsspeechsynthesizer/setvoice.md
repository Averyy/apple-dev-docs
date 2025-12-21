# setVoice(_:)

**Framework**: AppKit  
**Kind**: method

Sets the receiver’s current voice.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setVoice(_ voice: NSSpeechSynthesizer.VoiceName?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when the receiver is not currently synthesizing speech and the current voice is set successfully, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## Parameters

- `voice`: Identifier of the voice to set at the receiver’s current voice. When  , the receiver sets the default voice as its current voice.

## See Also

- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/defaultvoice.md)
  Provides the identifier of the default voice.
- [var usesFeedbackWindow: Bool](nsspeechsynthesizer/usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](nsspeechsynthesizer/voice.md)
  Returns the identifier of the receiver’s current voice.
- [var rate: Float](nsspeechsynthesizer/rate.md)
  The synthesizer’s speaking rate (words per minute).
- [var volume: Float](nsspeechsynthesizer/volume.md)
  The synthesizer’s speaking volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/setvoice(_:))*