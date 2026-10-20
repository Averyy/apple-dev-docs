# AVSpeechBoundary

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Specifies when to pause or stop speech.

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
enum AVSpeechBoundary
```

```c
enum AVSpeechBoundary : NSInteger;
```

## Topics

### Creating a speech boundary
- [init?(rawValue: Int)](./avspeechboundary/init%28rawvalue%29.md)
### Choosing a speech boundary
- [AVSpeechBoundary.immediate](./avspeechboundary/immediate.md)
  Indicates to pause or stop speech immediately.
- [AVSpeechBoundary.word](./avspeechboundary/word.md)
  Indicates to pause or stop speech after the synthesizer finishes speaking the current word.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling speech
- [func speak(AVSpeechUtterance)](./avspeechsynthesizer/speak%28_%29.md)
  Adds the utterance you specify to the speech synthesizer’s queue.
- [func continueSpeaking() -> Bool](./avspeechsynthesizer/continuespeaking%28%29.md)
  Resumes speech from its paused point.
- [func pauseSpeaking(at: AVSpeechBoundary) -> Bool](./avspeechsynthesizer/pausespeaking%28at%29.md)
  Pauses speech at the boundary you specify.
- [func stopSpeaking(at: AVSpeechBoundary) -> Bool](./avspeechsynthesizer/stopspeaking%28at%29.md)
  Stops speech at the boundary you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechboundary)*