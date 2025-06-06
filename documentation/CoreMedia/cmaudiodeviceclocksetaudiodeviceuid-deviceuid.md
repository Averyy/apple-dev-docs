# CMAudioDeviceClockSetAudioDeviceUID(_:deviceUID:)

**Framework**: Core Media  
**Kind**: func

Changes the Core Audio device the clock is tracking by specifying a new device unique identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockSetAudioDeviceUID(_ clock: CMClock, deviceUID: CFString?) -> OSStatus
```

#### Discussion

Pass `NULL` for `deviceUID` to make the clock track the default device.

## Parameters

- `clock`: The clock to change.
- `deviceUID`: The UID of the Core Audio device to track.

## See Also

- [func CMAudioDeviceClockGetAudioDevice(CMClock, deviceUIDOut: AutoreleasingUnsafeMutablePointer<CFString?>?, deviceIDOut: UnsafeMutablePointer<AudioDeviceID>?, trackingDefaultDeviceOut: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](cmaudiodeviceclockgetaudiodevice(_:deviceuidout:deviceidout:trackingdefaultdeviceout:).md)
  Returns the Core Audio device the clock is tracking.
- [func CMAudioDeviceClockSetAudioDeviceID(CMClock, deviceID: AudioDeviceID) -> OSStatus](cmaudiodeviceclocksetaudiodeviceid(_:deviceid:).md)
  Changes the Core Audio device the clock is tracking by specifying a new device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclocksetaudiodeviceuid(_:deviceuid:))*