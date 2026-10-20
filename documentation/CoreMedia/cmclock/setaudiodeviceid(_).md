# setAudioDeviceID(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Sets the audio device by using the device identifier.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func setAudioDeviceID(_ deviceID: AudioDeviceID) throws
```

## Parameters

- `deviceID`: The device identifier.

## See Also

### Getting Time and Devices
- [func anchorTime() throws -> (anchorTime: CMTime, referenceTime: CMTime)](./anchortime%28%29.md)
  Returns the current time from a clock and the matching time from the clock’s reference clock.
- [func audioDevice() throws -> (deviceUID: String?, deviceID: AudioDeviceID, trackingDefaultDevice: Bool)](./audiodevice%28%29.md)
  Returns the audio device the clock tracks.
- [func setAudioDeviceUID(String?) throws](./setaudiodeviceuid%28_%29.md)
  Sets the audio device by using the unique device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/setaudiodeviceid(_:))*