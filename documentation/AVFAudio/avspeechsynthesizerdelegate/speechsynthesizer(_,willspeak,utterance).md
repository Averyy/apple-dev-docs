# speechSynthesizer(_:willSpeak:utterance:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) speechSynthesizer:(AVSpeechSynthesizer *) synthesizer willSpeakMarker:(AVSpeechSynthesisMarker *) marker utterance:(AVSpeechUtterance *) utterance;
```

## Parameters

- `synthesizer`: The speech synthesizer that’s about to speak a marker of an utterance.
- `marker`: The synthesized audio that the speech synthesizer is about to speak.
- `utterance`: The utterance that the speech synthesizer pauses speaking.

## See Also

### Responding to speech synthesis events
- [func speechSynthesizer(AVSpeechSynthesizer, didStart: AVSpeechUtterance)](./speechsynthesizer%28_,didstart%29.md)
  Tells the delegate when the synthesizer begins speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeakRangeOfSpeechString: NSRange, utterance: AVSpeechUtterance)](./speechsynthesizer%28_,willspeakrangeofspeechstring,utterance%29.md)
  Tells the delegate when the synthesizer is about to speak a portion of an utterance’s text.
- [func speechSynthesizer(AVSpeechSynthesizer, didPause: AVSpeechUtterance)](./speechsynthesizer%28_,didpause%29.md)
  Tells the delegate when the synthesizer pauses while speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didContinue: AVSpeechUtterance)](./speechsynthesizer%28_,didcontinue%29.md)
  Tells the delegate when the synthesizer resumes speaking an utterance after pausing.
- [func speechSynthesizer(AVSpeechSynthesizer, didFinish: AVSpeechUtterance)](./speechsynthesizer%28_,didfinish%29.md)
  Tells the delegate when the synthesizer finishes speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didCancel: AVSpeechUtterance)](./speechsynthesizer%28_,didcancel%29.md)
  Tells the delegate when the synthesizer cancels speaking an utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate/speechsynthesizer(_:willspeak:utterance:))*