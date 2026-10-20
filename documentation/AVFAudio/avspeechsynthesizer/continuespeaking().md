# continueSpeaking()

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Resumes speech from its paused point.

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
func continueSpeaking() -> Bool
```

```objc
- (BOOL) continueSpeaking;
```

#### Return Value

[`true`](../../Swift/true.md) if speech resumes; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method only has an effect if the speech synthesizer is in a paused state.

## See Also

### Controlling speech
- [func speak(AVSpeechUtterance)](./speak%28_%29.md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](./pausespeaking%28at%29.md)
  Pauses speech at the boundary you specify.
- [func stopSpeaking(at: AVSpeechBoundary) -> Bool](./stopspeaking%28at%29.md)
  Stops speech at the boundary you specify.
- [enum AVSpeechBoundary](../avspeechboundary.md)
  Specifies when to pause or stop speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesizer/continuespeaking())*