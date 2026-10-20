# AVAudioSession.PromptStyle

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the prompt style to use.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum PromptStyle
```

```c
enum AVAudioSessionPromptStyle : NSUInteger;
```

## Topics

### Creating a prompt style
- [init?(rawValue: UInt)](./promptstyle-swift.enum/init%28rawvalue%29.md)
### Identifying prompt styles
- [AVAudioSession.PromptStyle.none](./promptstyle-swift.enum/none.md)
  Your app shouldn’t issue prompts at this time.
- [AVAudioSession.PromptStyle.short](./promptstyle-swift.enum/short.md)
  Your app should issue short, nonverbal prompts.
- [AVAudioSession.PromptStyle.normal](./promptstyle-swift.enum/normal.md)
  Your app may use long, verbal prompts.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the audio prompt style
- [var promptStyle: AVAudioSession.PromptStyle](./promptstyle-swift.property.md)
  A hint to audio sessions that use voice prompt mode to alter the type of prompts they issue in response to other system audio, such as Siri and phone calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/promptstyle-swift.enum)*