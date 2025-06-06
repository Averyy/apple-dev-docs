# promptStyle

**Framework**: AVFAudio  
**Kind**: property

A hint to audio sessions that use voice prompt mode to alter the type of prompts they issue in response to other system audio, such as Siri and phone calls.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var promptStyle: AVAudioSession.PromptStyle { get }
```

#### Discussion

Apps that issue voice prompts should observe changes in the prompt style and modify their prompts in response. This property is key-value observable.

## See Also

- [AVAudioSession.PromptStyle](avaudiosession/promptstyle-swift.enum.md)
  Constants that indicate the prompt style to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/promptstyle-swift.property)*