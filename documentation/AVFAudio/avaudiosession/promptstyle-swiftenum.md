# AVAudioSession.PromptStyle

**Framework**: AVFAudio  
**Kind**: enum

Constants that indicate the prompt style to use.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum PromptStyle
```

## Topics

### Prompt Styles
- [AVAudioSession.PromptStyle.none](avaudiosession/promptstyle-swift.enum/none.md)
  Your app shouldn’t issue prompts at this time.
- [AVAudioSession.PromptStyle.short](avaudiosession/promptstyle-swift.enum/short.md)
  Your app should issue short, nonverbal prompts.
- [AVAudioSession.PromptStyle.normal](avaudiosession/promptstyle-swift.enum/normal.md)
  Your app may use long, verbal prompts.
### Initializers
- [init?(rawValue: UInt)](avaudiosession/promptstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var promptStyle: AVAudioSession.PromptStyle](avaudiosession/promptstyle-swift.property.md)
  A hint to audio sessions that use voice prompt mode to alter the type of prompts they issue in response to other system audio, such as Siri and phone calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/promptstyle-swift.enum)*