# AVAudioUnitTimePitch

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioUnitTimePitch : AVAudioUnitTimeEffect
```

## Topics

### Adjusting pitch and rate
- [var overlap: Float](./avaudiounittimepitch/overlap.md)
  The amount of overlap between segments of the input audio signal.
- [var pitch: Float](./avaudiounittimepitch/pitch.md)
  The amount to use to pitch shift the input signal.
- [var rate: Float](./avaudiounittimepitch/rate.md)
  The playback rate of the input signal.

## Relationships

### Inherits From
- [AVAudioUnitTimeEffect](./avaudiounittimeeffect.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Time effects
- [class AVAudioUnitVarispeed](./avaudiounitvarispeed.md)
  An object that allows control of the playback rate.
- [class AVAudioUnitTimeEffect](./avaudiounittimeeffect.md)
  An object that processes audio in nonreal time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounittimepitch)*