# stopSpeaking(at:)

**Framework**: AVFAudio  
**Kind**: method

Stops speech at the boundary you specify.

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
func stopSpeaking(at boundary: AVSpeechBoundary) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if speech stops; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Unlike pausing a speech synthesizer, which can resume after a pause, stopping the synthesizer immediately cancels speech and removes all unspoken utterances from the synthesizer’s queue.

## Parameters

- `boundary`: An enumeration that describes whether to stop speech immediately or only after the synthesizer finishes speaking the current word.

## See Also

- [func speak(AVSpeechUtterance)](avspeechsynthesizer/speak(_:).md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func continueSpeaking() -> Bool](avspeechsynthesizer/continuespeaking.md)
  Resumes speech from its paused point.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/pausespeaking(at:).md)
  Pauses speech at the boundary you specify.
- [enum AVSpeechBoundary](avspeechboundary.md)
  Specifies when to pause or stop speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/stopspeaking(at:))*