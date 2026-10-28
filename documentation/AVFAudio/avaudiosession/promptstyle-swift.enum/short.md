# AVAudioSession.PromptStyle.short

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

Your app should issue short, nonverbal prompts.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case short
```

```c
AVAudioSessionPromptStyleShort
```

## Discussion

The audio session’s prompt style is short when Siri is active but not recording, when a voicemail is playing back, or when a voice call is active.

## See Also

### Identifying prompt styles
- [AVAudioSession.PromptStyle.none](./none.md)
  Your app shouldn’t issue prompts at this time.
- [AVAudioSession.PromptStyle.normal](./normal.md)
  Your app may use long, verbal prompts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/promptstyle-swift.enum/short)*