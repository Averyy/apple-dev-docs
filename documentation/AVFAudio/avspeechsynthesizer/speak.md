# speak(_:)

**Framework**: AVFAudio  
**Kind**: method

Adds the utterance you specify to the speech synthesizer’s queue.

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
func speak(_ utterance: AVSpeechUtterance)
```

#### Discussion

> ⚠️ **Warning**:  Attempting to enqueue the same utterance more than once throws an exception.

 Attempting to enqueue the same utterance more than once throws an exception.

## Parameters

- `utterance`: An   instance that contains text to speak.

## See Also

- [func continueSpeaking() -> Bool](avspeechsynthesizer/continuespeaking.md)
  Resumes speech from its paused point.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/pausespeaking(at:).md)
  Pauses speech at the boundary you specify.
- [func stopSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/stopspeaking(at:).md)
  Stops speech at the boundary you specify.
- [enum AVSpeechBoundary](avspeechboundary.md)
  Specifies when to pause or stop speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/speak(_:))*