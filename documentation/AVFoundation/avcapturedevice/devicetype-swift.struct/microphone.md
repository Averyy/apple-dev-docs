# microphone

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A microphone device type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
static let microphone: AVCaptureDevice.DeviceType
```

```c
extern AVCaptureDeviceType const AVCaptureDeviceTypeMicrophone;
```

## Discussion

In iOS and tvOS, the system only exposes one capture device of this type. The audio routing subsystem decides which physical microphone to use, be it a built-in microphone, a wired headset, or an external microphone. The microphone device’s [`localizedName`](../localizedname.md) changes as the audio subsystem switches to a different physical device.

## See Also

### Microphones
- [static let builtInMicrophone: AVCaptureDevice.DeviceType](./builtinmicrophone.md)
  A built-in microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/microphone)*