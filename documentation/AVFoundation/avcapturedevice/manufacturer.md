# manufacturer

**Framework**: AVFoundation  
**Kind**: property

A human-readable string for the manufacturer of the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
var manufacturer: String { get }
```

#### Discussion

You can use this property to identify capture devices by manufacturer. For all Apple devices, the value of this property is `Apple Inc.`

> 💡 **Tip**:  Devices from third-party manufacturers may not provide identifying text, in which case the value of this property is an empty string.

## See Also

- [var uniqueID: String](avcapturedevice/uniqueid.md)
  An identifier that uniquely identifies the device.
- [var modelID: String](avcapturedevice/modelid.md)
  A model identifier for the device.
- [var localizedName: String](avcapturedevice/localizedname.md)
  A localized device name for display in the user interface.
- [var deviceType: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.property.md)
  The type of device, such as a built-in microphone or wide-angle camera.
- [AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct.md)
  A structure that defines the device types the framework supports.
- [var position: AVCaptureDevice.Position](avcapturedevice/position-swift.property.md)
  The physical position of the capture device hardware.
- [AVCaptureDevice.Position](avcapturedevice/position-swift.enum.md)
  Constants that indicate the physical position of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/manufacturer)*