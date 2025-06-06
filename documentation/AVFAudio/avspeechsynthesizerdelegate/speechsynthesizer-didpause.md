# speechSynthesizer(_:didPause:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when the synthesizer pauses while speaking an utterance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didPause utterance: AVSpeechUtterance)
```

#### Discussion

The system only calls this method if a speech synthesizer is speaking an utterance and the system calls its [`pauseSpeaking(at:)`](avspeechsynthesizer/pausespeaking(at:).md) method. The system doesn’t call this method if the synthesizer is in a delay between utterances when speech pauses.

## Parameters

- `synthesizer`: The speech synthesizer that pauses speaking the utterance.
- `utterance`: The utterance that the speech synthesizer pauses speaking.

## See Also

- [func speechSynthesizer(AVSpeechSynthesizer, didStart: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didstart:).md)
  Tells the delegate when the synthesizer begins speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeakRangeOfSpeechString: NSRange, utterance: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:willspeakrangeofspeechstring:utterance:).md)
  Tells the delegate when the synthesizer is about to speak a portion of an utterance’s text.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeak: AVSpeechSynthesisMarker, utterance: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:willspeak:utterance:).md)
  Tells the delegate when the synthesizer is about to speak a marker of an utterance’s text.
- [func speechSynthesizer(AVSpeechSynthesizer, didContinue: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didcontinue:).md)
  Tells the delegate when the synthesizer resumes speaking an utterance after pausing.
- [func speechSynthesizer(AVSpeechSynthesizer, didFinish: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didfinish:).md)
  Tells the delegate when the synthesizer finishes speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didCancel: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didcancel:).md)
  Tells the delegate when the synthesizer cancels speaking an utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate/speechsynthesizer(_:didpause:))*