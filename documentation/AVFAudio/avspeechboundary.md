# AVSpeechBoundary

**Framework**: AVFAudio  
**Kind**: enum

Specifies when to pause or stop speech.

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
enum AVSpeechBoundary
```

## Topics

### Speech boundaries
- [AVSpeechBoundary.immediate](avspeechboundary/immediate.md)
  Indicates to pause or stop speech immediately.
- [AVSpeechBoundary.word](avspeechboundary/word.md)
  Indicates to pause or stop speech after the synthesizer finishes speaking the current word.
### Initializers
- [init?(rawValue: Int)](avspeechboundary/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func speak(AVSpeechUtterance)](avspeechsynthesizer/speak(_:).md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func continueSpeaking() -> Bool](avspeechsynthesizer/continuespeaking.md)
  Resumes speech from its paused point.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/pausespeaking(at:).md)
  Pauses speech at the boundary you specify.
- [func stopSpeaking(at: AVSpeechBoundary) -> Bool](avspeechsynthesizer/stopspeaking(at:).md)
  Stops speech at the boundary you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechboundary)*