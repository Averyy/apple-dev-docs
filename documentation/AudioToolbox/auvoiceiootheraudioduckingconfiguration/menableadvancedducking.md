# mEnableAdvancedDucking

**Framework**: Audio Toolbox  
**Kind**: property

A Boolean value that specifies whether to enable advanced ducking.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var mEnableAdvancedDucking: DarwinBoolean
```

#### Discussion

Advanced ducking ducks other non-voice audio based on the presence of voice activity from local and remote chat participants.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var mDuckingLevel: AUVoiceIOOtherAudioDuckingLevel](auvoiceiootheraudioduckingconfiguration/mduckinglevel.md)
  The ducking level of other non-voice audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auvoiceiootheraudioduckingconfiguration/menableadvancedducking)*