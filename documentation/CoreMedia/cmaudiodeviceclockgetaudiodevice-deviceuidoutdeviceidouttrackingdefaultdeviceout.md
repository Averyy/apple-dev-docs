# CMAudioDeviceClockGetAudioDevice(_:deviceUIDOut:deviceIDOut:trackingDefaultDeviceOut:)

**Framework**: Core Media  
**Kind**: func

Returns the Core Audio device the clock is tracking.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockGetAudioDevice(_ clock: CMClock, deviceUIDOut: AutoreleasingUnsafeMutablePointer<CFString?>?, deviceIDOut: UnsafeMutablePointer<AudioDeviceID>?, trackingDefaultDeviceOut: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

#### Return Value

A value that indicates the completion status.

## Parameters

- `clock`: The clock from which to retrieve its audio device.
- `deviceUIDOut`: An optional unique device identifier. If you specify a non-  value, this function returns the   and its associated ID, and sets   to  .
- `deviceIDOut`: An optional device identifier. If you specify a non-  value, this function returns a   UID and the device ID, and sets   to  .
- `trackingDefaultDeviceOut`: On return, a Boolean value that indicates whether the audio clock tracks the default audio device.

## See Also

- [func CMAudioDeviceClockSetAudioDeviceUID(CMClock, deviceUID: CFString?) -> OSStatus](cmaudiodeviceclocksetaudiodeviceuid(_:deviceuid:).md)
  Changes the Core Audio device the clock is tracking by specifying a new device unique identifier.
- [func CMAudioDeviceClockSetAudioDeviceID(CMClock, deviceID: AudioDeviceID) -> OSStatus](cmaudiodeviceclocksetaudiodeviceid(_:deviceid:).md)
  Changes the Core Audio device the clock is tracking by specifying a new device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclockgetaudiodevice(_:deviceuidout:deviceidout:trackingdefaultdeviceout:))*