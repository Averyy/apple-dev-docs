# audioDevice()

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns the audio device the clock tracks.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func audioDevice() throws -> (deviceUID: String?, deviceID: AudioDeviceID, trackingDefaultDevice: Bool)
```

## See Also

### Getting Time and Devices
- [func anchorTime() throws -> (anchorTime: CMTime, referenceTime: CMTime)](./anchortime%28%29.md)
  Returns the current time from a clock and the matching time from the clock’s reference clock.
- [func setAudioDeviceID(AudioDeviceID) throws](./setaudiodeviceid%28_%29.md)
  Sets the audio device by using the device identifier.
- [func setAudioDeviceUID(String?) throws](./setaudiodeviceuid%28_%29.md)
  Sets the audio device by using the unique device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/audiodevice())*