# uniqueID

**Framework**: AVFoundation  
**Kind**: property

An identifier that uniquely identifies the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var uniqueID: String { get }
```

#### Discussion

Capture devices have a unique identifier that persists on one system across device connections and disconnections, application restarts, and reboots of the system itself. You can store the value returned by this property to recall or track the status of a specific device in the future.

## See Also

- [var modelID: String](avcapturedevice/modelid.md)
  A model identifier for the device.
- [var localizedName: String](avcapturedevice/localizedname.md)
  A localized device name for display in the user interface.
- [var manufacturer: String](avcapturedevice/manufacturer.md)
  A human-readable string for the manufacturer of the device.
- [var deviceType: AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.property.md)
  The type of device, such as a built-in microphone or wide-angle camera.
- [AVCaptureDevice.DeviceType](avcapturedevice/devicetype-swift.struct.md)
  A structure that defines the device types the framework supports.
- [var position: AVCaptureDevice.Position](avcapturedevice/position-swift.property.md)
  The physical position of the capture device hardware.
- [AVCaptureDevice.Position](avcapturedevice/position-swift.enum.md)
  Constants that indicate the physical position of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/uniqueid)*