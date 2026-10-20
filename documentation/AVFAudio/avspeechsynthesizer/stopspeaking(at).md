# stopSpeaking(at:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Stops speech at the boundary you specify.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stopSpeaking(at boundary: AVSpeechBoundary) -> Bool
```

```objc
- (BOOL) stopSpeakingAtBoundary:(AVSpeechBoundary) boundary;
```

#### Return Value

[`true`](../../Swift/true.md) if speech stops; otherwise, [`false`](../../Swift/false.md).

#### Discussion

Unlike pausing a speech synthesizer, which can resume after a pause, stopping the synthesizer immediately cancels speech and removes all unspoken utterances from the synthesizer’s queue.

## Parameters

- `boundary`: An enumeration that describes whether to stop speech immediately or only after the synthesizer finishes speaking the current word.

## See Also

### Controlling speech
- [func speak(AVSpeechUtterance)](./speak%28_%29.md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func continueSpeaking() -> Bool](./continuespeaking%28%29.md)
  Resumes speech from its paused point.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](./pausespeaking%28at%29.md)
  Pauses speech at the boundary you specify.
- [enum AVSpeechBoundary](../avspeechboundary.md)
  Specifies when to pause or stop speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/stopspeaking(at:))*