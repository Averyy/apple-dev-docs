# AVAudioUnitTimeEffect

**Framework**: AVFAudio  
**Kind**: class

An object that processes audio in nonreal time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitTimeEffect
```

#### Overview

A time effect audio unit represents an [`AVAudioUnit`](avaudiounit.md) with a type `kAudioUnitType_FormatConverter` (`aufc)`. These effects don’t process audio in real time. The [`AVAudioUnitVarispeed`](avaudiounitvarispeed.md) class is an example of a time effect unit.

## Topics

### Creating a time effect
- [init(audioComponentDescription: AudioComponentDescription)](avaudiounittimeeffect/init(audiocomponentdescription:).md)
  Creates a time effect audio unit with the specified description.
### Getting and setting the time effect
- [var bypass: Bool](avaudiounittimeeffect/bypass.md)
  The bypass state of the audio unit.

## Relationships

### Inherits From
- [AVAudioUnit](avaudiounit.md)
### Inherited By
- [AVAudioUnitTimePitch](avaudiounittimepitch.md)
- [AVAudioUnitVarispeed](avaudiounitvarispeed.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioUnitTimePitch](avaudiounittimepitch.md)
  An object that provides a good-quality playback rate and pitch shifting independently of each other.
- [class AVAudioUnitVarispeed](avaudiounitvarispeed.md)
  An object that allows control of the playback rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimeeffect)*