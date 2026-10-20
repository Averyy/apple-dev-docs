# enableAdvancedDucking

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Enables advanced ducking which ducks other audio based on the presence of voice activity from local and remote chat participants.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var enableAdvancedDucking: ObjCBool
```

```c
BOOL enableAdvancedDucking;
```

## See Also

### Configuring ducking
- [var duckingLevel: AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level](./duckinglevel.md)
  The ducking level of other audio.
- [AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level](./level.md)
  Constants that define the supported ducking levels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiovoiceprocessingotheraudioduckingconfiguration/enableadvancedducking)*