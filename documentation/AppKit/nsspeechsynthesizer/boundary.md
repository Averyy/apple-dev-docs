# NSSpeechSynthesizer.Boundary

**Framework**: AppKit  
**Kind**: enum

These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) and [`stopSpeaking(at:)`](nsspeechsynthesizer/stopspeaking(at:).md).

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum Boundary
```

## Topics

### Constants
- [NSSpeechSynthesizer.Boundary.immediateBoundary](nsspeechsynthesizer/boundary/immediateboundary.md)
  Speech should be paused or stopped immediately.
- [NSSpeechSynthesizer.Boundary.wordBoundary](nsspeechsynthesizer/boundary/wordboundary.md)
  Speech should be paused or stopped at the end of the word.
- [NSSpeechSynthesizer.Boundary.sentenceBoundary](nsspeechsynthesizer/boundary/sentenceboundary.md)
  Speech should be paused or stopped at the end of the sentence.
### Initializers
- [init?(rawValue: UInt)](nsspeechsynthesizer/boundary/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var isSpeaking: Bool](nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](nsspeechsynthesizer/startspeaking(_:to:).md)
  Begins synthesizing text into a sound (AIFF) file.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/pausespeaking(at:).md)
  Pauses synthesis in progress at a given boundary.
- [func continueSpeaking()](nsspeechsynthesizer/continuespeaking.md)
  Resumes synthesis.
- [func stopSpeaking()](nsspeechsynthesizer/stopspeaking.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/stopspeaking(at:).md)
  Stops synthesis in progress at a given boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/boundary)*