# AVCaptureDevice.Position

**Framework**: AVFoundation  
**Kind**: enum

Constants that indicate the physical position of a capture device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum Position
```

## Topics

### Positions
- [AVCaptureDevice.Position.front](avcapturedevice/position-swift.enum/front.md)
  A position on the user-facing side of an iOS device.
- [AVCaptureDevice.Position.back](avcapturedevice/position-swift.enum/back.md)
  A position on the subject-facing side of an iOS device.
- [AVCaptureDevice.Position.unspecified](avcapturedevice/position-swift.enum/unspecified.md)
  A position that’s unspecified.
### Initializers
- [init?(rawValue: Int)](avcapturedevice/position-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var uniqueID: String](avcapturedevice/uniqueid.md)
  An identifier that uniquely identifies the device.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.enum)*