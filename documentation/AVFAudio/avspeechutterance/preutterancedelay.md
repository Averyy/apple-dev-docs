# preUtteranceDelay

**Framework**: AVFAudio  
**Kind**: property

The amount of time the speech synthesizer pauses before speaking the utterance.

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
var preUtteranceDelay: TimeInterval { get set }
```

#### Discussion

When multiple utterances exist in the queue, the speech synthesizer pauses a minimum amount of time equal to the sum of the current utterance’s [`postUtteranceDelay`](avspeechutterance/postutterancedelay.md) and the next utterance’s `preUtteranceDelay`.

## See Also

- [var rate: Float](avspeechutterance/rate.md)
  The rate the speech synthesizer uses when speaking the utterance.
- [let AVSpeechUtteranceMinimumSpeechRate: Float](avspeechutteranceminimumspeechrate.md)
  The minimum rate the speech synthesizer uses when speaking an utterance.
- [let AVSpeechUtteranceMaximumSpeechRate: Float](avspeechutterancemaximumspeechrate.md)
  The maximum rate the speech synthesizer uses when speaking an utterance.
- [let AVSpeechUtteranceDefaultSpeechRate: Float](avspeechutterancedefaultspeechrate.md)
  The default rate the speech synthesizer uses when speaking an utterance.
- [var postUtteranceDelay: TimeInterval](avspeechutterance/postutterancedelay.md)
  The amount of time the speech synthesizer pauses after speaking an utterance before handling the next utterance in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/preutterancedelay)*