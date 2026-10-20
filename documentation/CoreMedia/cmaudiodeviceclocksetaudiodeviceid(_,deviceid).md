# CMAudioDeviceClockSetAudioDeviceID(_:deviceID:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Changes the Core Audio device the clock is tracking by specifying a new device identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockSetAudioDeviceID(_ clock: CMClock, deviceID: AudioDeviceID) -> OSStatus
```

```c
extern OSStatus CMAudioDeviceClockSetAudioDeviceID(CMClockRef clock, AudioDeviceID deviceID);
```

## Parameters

- `clock`: The clock to change.
- `deviceID`: The new Core Audio device to track.

## See Also

### Configuring Audio Clocks
- [func CMAudioDeviceClockGetAudioDevice(CMClock, deviceUIDOut: AutoreleasingUnsafeMutablePointer<CFString?>?, deviceIDOut: UnsafeMutablePointer<AudioDeviceID>?, trackingDefaultDeviceOut: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](./cmaudiodeviceclockgetaudiodevice%28_,deviceuidout,deviceidout,trackingdefaultdeviceout%29.md)
  Returns the Core Audio device the clock is tracking.
- [func CMAudioDeviceClockSetAudioDeviceUID(CMClock, deviceUID: CFString?) -> OSStatus](./cmaudiodeviceclocksetaudiodeviceuid%28_,deviceuid%29.md)
  Changes the Core Audio device the clock is tracking by specifying a new device unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclocksetaudiodeviceid(_:deviceid:))*