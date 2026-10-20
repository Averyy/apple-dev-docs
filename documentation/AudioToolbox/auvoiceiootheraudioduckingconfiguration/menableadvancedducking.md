# mEnableAdvancedDucking

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to enable advanced ducking.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var mEnableAdvancedDucking: DarwinBoolean
```

```c
Boolean mEnableAdvancedDucking;
```

#### Discussion

Advanced ducking ducks other non-voice audio based on the presence of voice activity from local and remote chat participants.

The default value is [`false`](../../Swift/false.md).

## See Also

### Inspecting a configuration
- [var mDuckingLevel: AUVoiceIOOtherAudioDuckingLevel](./mduckinglevel.md)
  The ducking level of other non-voice audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auvoiceiootheraudioduckingconfiguration/menableadvancedducking)*