# speechSynthesizer(_:willSpeak:utterance:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when the synthesizer is about to speak a marker of an utterance’s text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, willSpeak marker: AVSpeechSynthesisMarker, utterance: AVSpeechUtterance)
```

## Parameters

- `synthesizer`: The speech synthesizer that’s about to speak a marker of an utterance.
- `marker`: The synthesized audio that the speech synthesizer is about to speak.
- `utterance`: The utterance that the speech synthesizer pauses speaking.

## See Also

- [func speechSynthesizer(AVSpeechSynthesizer, didStart: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didstart:).md)
  Tells the delegate when the synthesizer begins speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeakRangeOfSpeechString: NSRange, utterance: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:willspeakrangeofspeechstring:utterance:).md)
  Tells the delegate when the synthesizer is about to speak a portion of an utterance’s text.
- [func speechSynthesizer(AVSpeechSynthesizer, didPause: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didpause:).md)
  Tells the delegate when the synthesizer pauses while speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didContinue: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didcontinue:).md)
  Tells the delegate when the synthesizer resumes speaking an utterance after pausing.
- [func speechSynthesizer(AVSpeechSynthesizer, didFinish: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didfinish:).md)
  Tells the delegate when the synthesizer finishes speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didCancel: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didcancel:).md)
  Tells the delegate when the synthesizer cancels speaking an utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate/speechsynthesizer(_:willspeak:utterance:))*