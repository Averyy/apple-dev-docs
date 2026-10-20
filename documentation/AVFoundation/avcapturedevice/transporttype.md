# transportType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The transport type of the device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var transportType: Int32 { get }
```

```objc
@property (nonatomic, readonly) int32_t transportType;
```

#### Discussion

The value of this property represents a capture device’s transport type, such as USB or PCI. The value is an IOKit framework transport type constant (`kIOAudioDeviceTransportType`).

## See Also

### Inspecting device characteristics
- [var isVirtualDevice: Bool](./isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [var constituentDevices: [AVCaptureDevice]](./constituentdevices.md)
  An array of physical devices that make up a virtual device.
- [func hasMediaType(AVMediaType) -> Bool](./hasmediatype%28_%29.md)
  Returns a Boolean value that indicates whether the device captures media of a particular type.
- [func supportsSessionPreset(AVCaptureSession.Preset) -> Bool](./supportssessionpreset%28_%29.md)
  Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/transporttype)*