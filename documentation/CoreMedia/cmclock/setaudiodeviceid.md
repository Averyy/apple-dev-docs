# setAudioDeviceID(_:)

**Framework**: Core Media  
**Kind**: method

Sets the audio device by using the device identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
func setAudioDeviceID(_ deviceID: AudioDeviceID) throws
```

## Parameters

- `deviceID`: The device identifier.

## See Also

- [func anchorTime() throws -> (anchorTime: CMTime, referenceTime: CMTime)](cmclock/anchortime.md)
  Returns the current time from a clock and the matching time from the clock’s reference clock.
- [func audioDevice() throws -> (deviceUID: String?, deviceID: AudioDeviceID, trackingDefaultDevice: Bool)](cmclock/audiodevice.md)
  Returns the audio device the clock tracks.
- [func setAudioDeviceUID(String?) throws](cmclock/setaudiodeviceuid(_:).md)
  Sets the audio device by using the unique device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/setaudiodeviceid(_:))*