# continueSpeaking()

**Framework**: AVFAudio  
**Kind**: method

Resumes speech from its paused point.

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
func continueSpeaking() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if speech resumes; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method only has an effect if the speech synthesizer is in a paused state.

## See Also

- [func speak(AVSpeechUtterance)](avspeechsynthesizer/speak(_:).md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/pausespeaking(at:).md)
  Pauses speech at the boundary you specify.
- [func stopSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/stopspeaking(at:).md)
  Stops speech at the boundary you specify.
- [enum AVSpeechBoundary](avspeechboundary.md)
  Specifies when to pause or stop speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/continuespeaking())*