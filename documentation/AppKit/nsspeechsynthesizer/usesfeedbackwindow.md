# usesFeedbackWindow

**Framework**: AppKit  
**Kind**: property

Indicates whether the receiver uses the speech feedback window.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var usesFeedbackWindow: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) when the receiver uses the speech feedback window, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

See the class description for details on the `UsesFeedbackWindow` attribute.

> ❗ **Important**:  The delegate only receives the [`speechSynthesizer(_:didFinishSpeaking:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md) message when speaking occurs through the feedback window.

## See Also

- [func voice() -> NSSpeechSynthesizer.VoiceName?](nsspeechsynthesizer/voice.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](nsspeechsynthesizer/setvoice(_:).md)
  Sets the receiver’s current voice.
- [var rate: Float](nsspeechsynthesizer/rate.md)
  The synthesizer’s speaking rate (words per minute).
- [var volume: Float](nsspeechsynthesizer/volume.md)
  The synthesizer’s speaking volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/usesfeedbackwindow)*