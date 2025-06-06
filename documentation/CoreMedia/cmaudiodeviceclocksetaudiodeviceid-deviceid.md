# CMAudioDeviceClockSetAudioDeviceID(_:deviceID:)

**Framework**: Core Media  
**Kind**: func

Changes the Core Audio device the clock is tracking by specifying a new device identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockSetAudioDeviceID(_ clock: CMClock, deviceID: AudioDeviceID) -> OSStatus
```

## Parameters

- `clock`: The clock to change.
- `deviceID`: The new Core Audio device to track.

## See Also

- [func CMAudioDeviceClockGetAudioDevice(CMClock, deviceUIDOut: AutoreleasingUnsafeMutablePointer<CFString?>?, deviceIDOut: UnsafeMutablePointer<AudioDeviceID>?, trackingDefaultDeviceOut: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](cmaudiodeviceclockgetaudiodevice(_:deviceuidout:deviceidout:trackingdefaultdeviceout:).md)
  Returns the Core Audio device the clock is tracking.
- [func CMAudioDeviceClockSetAudioDeviceUID(CMClock, deviceUID: CFString?) -> OSStatus](cmaudiodeviceclocksetaudiodeviceuid(_:deviceuid:).md)
  Changes the Core Audio device the clock is tracking by specifying a new device unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclocksetaudiodeviceid(_:deviceid:))*