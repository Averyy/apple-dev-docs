# NSSpeechSynthesizer.Boundary

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) and [`stopSpeaking(at:)`](./stopspeaking%28at%29.md).

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
enum Boundary
```

```c
enum NSSpeechBoundary : NSUInteger;
```

## Topics

### Constants
- [NSSpeechSynthesizer.Boundary.immediateBoundary](./boundary/immediateboundary.md)
  Speech should be paused or stopped immediately.
- [NSSpeechSynthesizer.Boundary.wordBoundary](./boundary/wordboundary.md)
  Speech should be paused or stopped at the end of the word.
- [NSSpeechSynthesizer.Boundary.sentenceBoundary](./boundary/sentenceboundary.md)
  Speech should be paused or stopped at the end of the sentence.
### Initializers
- [init?(rawValue: UInt)](./boundary/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Synthesizing Speech
- [var isSpeaking: Bool](./isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](./startspeaking%28_%29.md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](./startspeaking%28_,to%29.md)
  Begins synthesizing text into a sound (AIFF) file.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](./pausespeaking%28at%29.md)
  Pauses synthesis in progress at a given boundary.
- [func continueSpeaking()](./continuespeaking%28%29.md)
  Resumes synthesis.
- [func stopSpeaking()](./stopspeaking%28%29.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](./stopspeaking%28at%29.md)
  Stops synthesis in progress at a given boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/boundary)*