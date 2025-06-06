# AVAudioTime

**Framework**: AVFAudio  
**Kind**: class

An object you use to represent a moment in time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioTime
```

#### Overview

The `AVAudioTime` object represents a single moment in time in two ways:

- As host time, using the system’s basic clock with `mach_absolute_time()`
- As audio samples at a particular sample rate

A single `AVAudioTime` instance contains either or both representations, meaning it might represent only a sample time, a host time, or both.

Instances of this class are immutable.

## Topics

### Creating an Audio Time Instance
- [init(audioTimeStamp: UnsafePointer<AudioTimeStamp>, sampleRate: Double)](avaudiotime/init(audiotimestamp:samplerate:).md)
  Creates an audio time object with the specified timestamp and sample rate.
- [init(hostTime: UInt64)](avaudiotime/init(hosttime:).md)
  Creates an audio time object with the specified host time.
- [init(hostTime: UInt64, sampleTime: AVAudioFramePosition, atRate: Double)](avaudiotime/init(hosttime:sampletime:atrate:).md)
  Creates an audio time object with the specified host time, sample time, and sample rate.
- [init(sampleTime: AVAudioFramePosition, atRate: Double)](avaudiotime/init(sampletime:atrate:).md)
  Creates an audio time object with the specified timestamp and sample rate.
- [func extrapolateTime(fromAnchor: AVAudioTime) -> AVAudioTime?](avaudiotime/extrapolatetime(fromanchor:).md)
  Creates an audio time object by converting between host time and sample time.
### Manipulating Host Time
- [var hostTime: UInt64](avaudiotime/hosttime.md)
  The host time.
- [var isHostTimeValid: Bool](avaudiotime/ishosttimevalid.md)
  A Boolean value that indicates whether the host time value is valid.
- [class func hostTime(forSeconds: TimeInterval) -> UInt64](avaudiotime/hosttime(forseconds:).md)
  Converts seconds to host time.
- [class func seconds(forHostTime: UInt64) -> TimeInterval](avaudiotime/seconds(forhosttime:).md)
  Converts host time to seconds.
### Getting Sample Rate Information
- [var sampleRate: Double](avaudiotime/samplerate.md)
  The sampling rate that the sample time property expresses.
- [var sampleTime: AVAudioFramePosition](avaudiotime/sampletime.md)
  The time as a number of audio samples that the current audio device tracks.
- [var isSampleTimeValid: Bool](avaudiotime/issampletimevalid.md)
  A Boolean value that indicates whether the sample time and sample rate properties are in a valid state.
### Getting the Core Audio Time Stamp
- [var audioTimeStamp: AudioTimeStamp](avaudiotime/audiotimestamp.md)
  The time as an audio timestamp.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVAudioBuffer](avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [class AVAudioFile](avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiotime)*