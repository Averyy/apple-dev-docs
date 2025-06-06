# pauseSpeaking(at:)

**Framework**: AVFAudio  
**Kind**: method

Pauses speech at the boundary you specify.

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
func pauseSpeaking(at boundary: AVSpeechBoundary) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if speech pauses; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The `boundary` parameter also affects how the speech synthesizer resumes speaking text after a pause and call to [`continueSpeaking()`](avspeechsynthesizer/continuespeaking().md). If the boundary is [`AVSpeechBoundary.immediate`](avspeechboundary/immediate.md), speech resumes from the exact point where it pauses, even if that point occurs in the middle of speaking a word. If the boundary is [`AVSpeechBoundary.word`](avspeechboundary/word.md), speech resumes from the word that follows the last spoken word where it pauses.

## Parameters

- `boundary`: An enumeration that describes whether to pause speech immediately or only after the synthesizer finishes speaking the current word.

## See Also

- [func speak(AVSpeechUtterance)](avspeechsynthesizer/speak(_:).md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func continueSpeaking() -> Bool](avspeechsynthesizer/continuespeaking.md)
  Resumes speech from its paused point.
- [func stopSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/stopspeaking(at:).md)
  Stops speech at the boundary you specify.
- [enum AVSpeechBoundary](avspeechboundary.md)
  Specifies when to pause or stop speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/pausespeaking(at:))*