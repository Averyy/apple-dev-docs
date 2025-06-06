# speechSynthesizer(_:willSpeakRangeOfSpeechString:utterance:)

**Framework**: AVFAudio  
**Kind**: method

Tells the delegate when the synthesizer is about to speak a portion of an utterance’s text.

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
optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, willSpeakRangeOfSpeechString characterRange: NSRange, utterance: AVSpeechUtterance)
```

#### Discussion

The system calls this method once for each unit of speech in the utterance’s text, which is generally a word.

> 💡 **Tip**:  Implement this method if you want to provide a user interface to visually highlight each word as the synthesizer speaks it.

 Implement this method if you want to provide a user interface to visually highlight each word as the synthesizer speaks it.

## Parameters

- `synthesizer`: The speech synthesizer that’s about to speak an utterance.
- `characterRange`: The range of characters in the utterance’s   that correspond to the unit of speech the synthesizer is about to speak.
- `utterance`: The utterance that the speech synthesizer is about to speak.

## See Also

- [func speechSynthesizer(AVSpeechSynthesizer, didStart: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didstart:).md)
  Tells the delegate when the synthesizer begins speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeak: AVSpeechSynthesisMarker, utterance: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:willspeak:utterance:).md)
  Tells the delegate when the synthesizer is about to speak a marker of an utterance’s text.
- [func speechSynthesizer(AVSpeechSynthesizer, didPause: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didpause:).md)
  Tells the delegate when the synthesizer pauses while speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didContinue: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didcontinue:).md)
  Tells the delegate when the synthesizer resumes speaking an utterance after pausing.
- [func speechSynthesizer(AVSpeechSynthesizer, didFinish: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didfinish:).md)
  Tells the delegate when the synthesizer finishes speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didCancel: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didcancel:).md)
  Tells the delegate when the synthesizer cancels speaking an utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate/speechsynthesizer(_:willspeakrangeofspeechstring:utterance:))*