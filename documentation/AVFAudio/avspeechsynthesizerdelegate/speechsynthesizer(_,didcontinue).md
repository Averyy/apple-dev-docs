# speechSynthesizer(_:didContinue:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the synthesizer resumes speaking an utterance after pausing.

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
optional func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didContinue utterance: AVSpeechUtterance)
```

```objc
- (void) speechSynthesizer:(AVSpeechSynthesizer *) synthesizer didContinueSpeechUtterance:(AVSpeechUtterance *) utterance;
```

## Discussion

The system only calls this method if a speech synthesizer pauses speaking and the system calls its [`pauseSpeaking(at:)`](../avspeechsynthesizer/pausespeaking%28at%29.md) method. The system doesn’t call this method if the synthesizer pauses while in a delay between utterances.

## Parameters

- `synthesizer`: The speech synthesizer that resumes speaking the utterance.
- `utterance`: The utterance that the speech synthesizer resumes speaking.

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
- [func speechSynthesizer(AVSpeechSynthesizer, didFinish: AVSpeechUtterance)](./speechsynthesizer%28_,didfinish%29.md)
  Tells the delegate when the synthesizer finishes speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, didCancel: AVSpeechUtterance)](./speechsynthesizer%28_,didcancel%29.md)
  Tells the delegate when the synthesizer cancels speaking an utterance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate/speechsynthesizer(_:didcontinue:))*