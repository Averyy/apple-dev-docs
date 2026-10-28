# AVAudioSession.PromptStyle.none

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

Your app shouldn’t issue prompts at this time.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case none
```

```c
AVAudioSessionPromptStyleNone
```

## Discussion

This style indicates that another audio session is currently using microphone input, and your app shouldn’t issue prompts at this time.

For example, if Siri is recognizing speech, playing navigation or exercise prompts could interfere with Siri’s ability to accurately recognize the user’s speech. Your app should refrain from playing any prompts while the prompt style equals this value.

## See Also

### Identifying prompt styles
- [AVAudioSession.PromptStyle.short](./short.md)
  Your app should issue short, nonverbal prompts.
- [AVAudioSession.PromptStyle.normal](./normal.md)
  Your app may use long, verbal prompts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/promptstyle-swift.enum/none)*