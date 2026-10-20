# anchorTime()

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns the current time from a clock and the matching time from the clock’s reference clock.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func anchorTime() throws -> (anchorTime: CMTime, referenceTime: CMTime)
```

## See Also

### Getting Time and Devices
- [func audioDevice() throws -> (deviceUID: String?, deviceID: AudioDeviceID, trackingDefaultDevice: Bool)](./audiodevice%28%29.md)
  Returns the audio device the clock tracks.
- [func setAudioDeviceID(AudioDeviceID) throws](./setaudiodeviceid%28_%29.md)
  Sets the audio device by using the device identifier.
- [func setAudioDeviceUID(String?) throws](./setaudiodeviceuid%28_%29.md)
  Sets the audio device by using the unique device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmclock/anchortime())*