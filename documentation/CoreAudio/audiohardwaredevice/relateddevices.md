# relatedDevices

**Framework**: Core Audio  
**Kind**: property

An array of AudioHardwareDevices for devices related to the device. For IOAudio-based devices, devices are related if they share the same IOAudioDevice object.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
var relatedDevices: [AudioHardwareDevice] { get throws }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice/relateddevices)*