# CMAudioClock APIs

**Framework**: Core Media

A specialized reference clock that synchronizes with audio sources.

#### Overview

An audio clock is a specialized [`CMClock`](cmclock.md) that you use to synchronize with audio sources. For details on clocks and synchronization, see [`CMClock`](cmclock.md).

## Topics

### Creating Audio Clocks
- [func CMAudioClockCreate(allocator: CFAllocator?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudioclockcreate(allocator:clockout:).md)
  Creates a clock that advances at the same rate as audio output.
- [func CMAudioDeviceClockCreate(allocator: CFAllocator?, deviceUID: CFString?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudiodeviceclockcreate(allocator:deviceuid:clockout:).md)
  Creates a clock that tracks playback through a Core Audio device with the specified unique identifier.
- [func CMAudioDeviceClockCreateFromAudioDeviceID(allocator: CFAllocator?, deviceID: AudioDeviceID, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudiodeviceclockcreatefromaudiodeviceid(allocator:deviceid:clockout:).md)
  Creates a clock that tracks playback through a Core Audio device with the specified identifier.
### Configuring Audio Clocks
- [func CMAudioDeviceClockGetAudioDevice(CMClock, deviceUIDOut: AutoreleasingUnsafeMutablePointer<CFString?>?, deviceIDOut: UnsafeMutablePointer<AudioDeviceID>?, trackingDefaultDeviceOut: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](cmaudiodeviceclockgetaudiodevice(_:deviceuidout:deviceidout:trackingdefaultdeviceout:).md)
  Returns the Core Audio device the clock is tracking.
- [func CMAudioDeviceClockSetAudioDeviceUID(CMClock, deviceUID: CFString?) -> OSStatus](cmaudiodeviceclocksetaudiodeviceuid(_:deviceuid:).md)
  Changes the Core Audio device the clock is tracking by specifying a new device unique identifier.
- [func CMAudioDeviceClockSetAudioDeviceID(CMClock, deviceID: AudioDeviceID) -> OSStatus](cmaudiodeviceclocksetaudiodeviceid(_:deviceid:).md)
  Changes the Core Audio device the clock is tracking by specifying a new device identifier.

## See Also

- [CMClock APIs](cmclock-api.md)
  A reference clock you use to synchronize applications and devices.
- [CMTimebase APIs](cmtimebase-api.md)
  A model of a timeline under application control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudioclock-api)*