# AUVoiceIOOtherAudioDuckingConfiguration

**Framework**: Audio Toolbox  
**Kind**: struct

A structure that you use to configure ducking of other non-voice audio in a voice chat.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AUVoiceIOOtherAudioDuckingConfiguration
```

#### Overview

Use this structure to specify whether to enable advanced ducking and set the ducking level of other non-voice audio in a voice chat. Advanced ducking ducks other non-voice audio based on the presence of voice activity from local and remote chat participants. Setting a higher level of ducking could increase the clarity of voice chat.

If you don’t set this value, the default ducking configuration disables advanced ducking and sets the ducking level to [`AUVoiceIOOtherAudioDuckingLevel.default`](auvoiceiootheraudioduckinglevel/default.md).

## Topics

### Creating an audio ducking configuration
- [enum AUVoiceIOOtherAudioDuckingLevel](auvoiceiootheraudioduckinglevel.md)
  The ducking level to apply to other non-voice audio.
### Inspecting a configuration
- [var mEnableAdvancedDucking: DarwinBoolean](auvoiceiootheraudioduckingconfiguration/menableadvancedducking.md)
  A Boolean value that specifies whether to enable advanced ducking.
- [var mDuckingLevel: AUVoiceIOOtherAudioDuckingLevel](auvoiceiootheraudioduckingconfiguration/mduckinglevel.md)
  The ducking level of other non-voice audio.
### Initializers
- [init()](auvoiceiootheraudioduckingconfiguration/init.md)
  Creates a new ducking configuration for other non-voice audio with advanced ducking disabled and the default ducking level.
- [init(mEnableAdvancedDucking: DarwinBoolean, mDuckingLevel: AUVoiceIOOtherAudioDuckingLevel)](auvoiceiootheraudioduckingconfiguration/init(menableadvancedducking:mduckinglevel:).md)
  Creates a new ducking configuration in which you specify whether to enable advanced ducking and the ducking level of other non-voice audio.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auvoiceiootheraudioduckingconfiguration)*