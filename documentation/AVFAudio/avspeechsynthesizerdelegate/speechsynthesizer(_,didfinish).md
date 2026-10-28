# speechSynthesizer(_:didFinish:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the synthesizer finishes speaking an utterance.

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
optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance)
```

```objc
- (void) speechSynthesizer:(AVSpeechSynthesizer *) synthesizer didFinishSpeechUtterance:(AVSpeechUtterance *) utterance;
```

## Discussion

The system ignores the final utterance’s [`postUtteranceDelay`](../avspeechutterance/postutterancedelay.md) and calls this method immediately when speech ends.

## Parameters

- `synthesizer`: The speech synthesizer that finishes speaking the utterance.
- `utterance`: The utterance that the speech synthesizer finishes speaking.

## See Also

### Responding to speech synthesis events
- [func speechSynthesizer(AVSpeechSynthesizer, didStart: AVSpeechUtterance)](./speechsynthesizer%28_,didstart%29.md)
  Tells the delegate when the synthesizer begins speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeakRangeOfSpeechString: NSRange, utterance: AVSpeechUtterance)](./speechsynthesizer%28_,willspeakrangeofspeechstring,utterance%29.md)
  Tells the delegate when the synthesizer is about to speak a portion of an utterance’s text.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeak: AVSpeechSynthesisMarker, utterance: AVSpeechUtterance)](./speechsynthesizer%28_,willspeak,utterance%29.md)
  Tells the delegate when the synthesizer is about to speak a marker of an utterance’s text.
- [func speechSynthesizer(AVSpeechSynthesizer, didPause: AVSpeechUtterance)](./speechsynthesizer%28_,didpause%29.md)
  Tells the delegate when the synthesizer pauses while speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didContinue: AVSpeechUtterance)](./speechsynthesizer%28_,didcontinue%29.md)
  Tells the delegate when the synthesizer resumes speaking an utterance after pausing.
- [func speechSynthesizer(AVSpeechSynthesizer, didCancel: AVSpeechUtterance)](./speechsynthesizer%28_,didcancel%29.md)
  Tells the delegate when the synthesizer cancels speaking an utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate/speechsynthesizer(_:didfinish:))*