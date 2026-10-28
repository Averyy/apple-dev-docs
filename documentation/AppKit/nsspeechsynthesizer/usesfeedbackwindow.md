# usesFeedbackWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the receiver uses the speech feedback window.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
var usesFeedbackWindow: Bool { get set }
```

```objc
@property BOOL usesFeedbackWindow;
```

## Discussion

[`true`](../../Swift/true.md) when the receiver uses the speech feedback window, [`false`](../../Swift/false.md) otherwise.

See the class description for details on the `UsesFeedbackWindow` attribute.

> ❗ **Important**:  The delegate only receives the [`speechSynthesizer(_:didFinishSpeaking:)`](../nsspeechsynthesizerdelegate/speechsynthesizer%28_,didfinishspeaking%29.md) message when speaking occurs through the feedback window.

## See Also

### Configuring Speech Synthesizers
- [func voice() -> NSSpeechSynthesizer.VoiceName?](./voice%28%29.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](./setvoice%28_%29.md)
  Sets the receiver’s current voice.
- [var rate: Float](./rate.md)
  The synthesizer’s speaking rate (words per minute).
- [var volume: Float](./volume.md)
  The synthesizer’s speaking volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/usesfeedbackwindow)*