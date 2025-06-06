# rate

**Framework**: AVFAudio  
**Kind**: property

The rate the speech synthesizer uses when speaking the utterance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rate: Float { get set }
```

#### Discussion

The speech rate is a decimal representation within the range of [`AVSpeechUtteranceMinimumSpeechRate`](avspeechutteranceminimumspeechrate.md) and [`AVSpeechUtteranceMaximumSpeechRate`](avspeechutterancemaximumspeechrate.md). Lower values correspond to slower speech, and higher values correspond to faster speech. The default value is [`AVSpeechUtteranceDefaultSpeechRate`](avspeechutterancedefaultspeechrate.md). Set this property before enqueing the utterance because setting it afterward has no effect.

## See Also

- [let AVSpeechUtteranceMinimumSpeechRate: Float](avspeechutteranceminimumspeechrate.md)
  The minimum rate the speech synthesizer uses when speaking an utterance.
- [let AVSpeechUtteranceMaximumSpeechRate: Float](avspeechutterancemaximumspeechrate.md)
  The maximum rate the speech synthesizer uses when speaking an utterance.
- [let AVSpeechUtteranceDefaultSpeechRate: Float](avspeechutterancedefaultspeechrate.md)
  The default rate the speech synthesizer uses when speaking an utterance.
- [var preUtteranceDelay: TimeInterval](avspeechutterance/preutterancedelay.md)
  The amount of time the speech synthesizer pauses before speaking the utterance.
- [var postUtteranceDelay: TimeInterval](avspeechutterance/postutterancedelay.md)
  The amount of time the speech synthesizer pauses after speaking an utterance before handling the next utterance in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/rate)*