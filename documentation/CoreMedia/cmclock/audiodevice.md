# audioDevice()

**Framework**: Core Media  
**Kind**: method

Returns the audio device the clock tracks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
func audioDevice() throws -> (deviceUID: String?, deviceID: AudioDeviceID, trackingDefaultDevice: Bool)
```

## See Also

- [func anchorTime() throws -> (anchorTime: CMTime, referenceTime: CMTime)](cmclock/anchortime.md)
  Returns the current time from a clock and the matching time from the clock’s reference clock.
- [func setAudioDeviceID(AudioDeviceID) throws](cmclock/setaudiodeviceid(_:).md)
  Sets the audio device by using the device identifier.
- [func setAudioDeviceUID(String?) throws](cmclock/setaudiodeviceuid(_:).md)
  Sets the audio device by using the unique device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/audiodevice())*