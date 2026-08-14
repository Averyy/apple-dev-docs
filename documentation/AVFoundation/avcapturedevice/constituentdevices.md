# constituentDevices

**Framework**: AVFoundation  
**Kind**: property

An array of physical devices that make up a virtual device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var constituentDevices: [AVCaptureDevice] { get }
```

#### Discussion

The value of this property is an empty array when called on a device whose [`isVirtualDevice`](avcapturedevice/isvirtualdevice.md) property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isVirtualDevice: Bool](avcapturedevice/isvirtualdevice.md)
  A Boolean value that indicates whether the device consists of two or more physical devices.
- [func hasMediaType(AVMediaType) -> Bool](avcapturedevice/hasmediatype(_:).md)
  Returns a Boolean value that indicates whether the device captures media of a particular type.
- [var transportType: Int32](avcapturedevice/transporttype.md)
  The transport type of the device.
- [func supportsSessionPreset(AVCaptureSession.Preset) -> Bool](avcapturedevice/supportssessionpreset(_:).md)
  Returns a Boolean value that indicates whether you can use the device with capture session configured with the specified preset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/constituentdevices)*