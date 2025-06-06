# AVAudioUnitTimePitch

**Framework**: AVFAudio  
**Kind**: class

An object that provides a good-quality playback rate and pitch shifting independently of each other.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitTimePitch
```

## Topics

### Getting and setting time pitch values
- [var overlap: Float](avaudiounittimepitch/overlap.md)
  The amount of overlap between segments of the input audio signal.
- [var pitch: Float](avaudiounittimepitch/pitch.md)
  The amount to use to pitch shift the input signal.
- [var rate: Float](avaudiounittimepitch/rate.md)
  The playback rate of the input signal.

## Relationships

### Inherits From
- [AVAudioUnitTimeEffect](avaudiounittimeeffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioUnitTimeEffect](avaudiounittimeeffect.md)
  An object that processes audio in nonreal time.
- [class AVAudioUnitVarispeed](avaudiounitvarispeed.md)
  An object that allows control of the playback rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimepitch)*