# transportType

**Framework**: AVFoundation  
**Kind**: property

The transport type of the device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var transportType: Int32 { get }
```

#### Discussion

The value of this property represents a capture device’s transport type, such as USB or PCI. The value is an IOKit framework transport type constant (`kIOAudioDeviceTransportType`).

## See Also

- [var isVirtualDevice: Bool](avcapturedevice/isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [var constituentDevices: [AVCaptureDevice]](avcapturedevice/constituentdevices.md)
  An array of physical devices that make up a virtual device.
- [func hasMediaType(AVMediaType) -> Bool](avcapturedevice/hasmediatype(_:).md)
  Returns a Boolean value that indicates whether the device captures media of a particular type.
- [func supportsSessionPreset(AVCaptureSession.Preset) -> Bool](avcapturedevice/supportssessionpreset(_:).md)
  Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transporttype)*