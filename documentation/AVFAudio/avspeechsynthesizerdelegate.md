# AVSpeechSynthesizerDelegate

**Framework**: AVFAudio  
**Kind**: protocol

A delegate protocol that contains optional methods you can implement to respond to events that occur during speech synthesis.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol AVSpeechSynthesizerDelegate : NSObjectProtocol, Sendable
```

#### Overview

A speech synthesizer sends messages to its delegate for three categories of events:

- The synthesizer starts or finishes speaking an utterance.
- Speech pauses or resumes.
- The synthesizer produces each individual unit of speech, which is generally a word.

## Topics

### Responding to speech synthesis events
- [func speechSynthesizer(AVSpeechSynthesizer, didStart: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:didstart:).md)
  Tells the delegate when the synthesizer begins speaking an utterance.
- [func speechSynthesizer(AVSpeechSynthesizer, willSpeakRangeOfSpeechString: NSRange, utterance: AVSpeechUtterance)](avspeechsynthesizerdelegate/speechsynthesizer(_:willspeakrangeofspeechstring:utterance:).md)
  Tells the delegate when the synthesizer is about to speak a portion of an utterance’s text.
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

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any AVSpeechSynthesizerDelegate)?](avspeechsynthesizer/delegate.md)
  The delegate object for the speech synthesizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizerdelegate)*