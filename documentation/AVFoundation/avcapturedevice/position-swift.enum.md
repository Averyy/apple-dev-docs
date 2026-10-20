# AVCaptureDevice.Position

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVCaptureDevicePosition : NSInteger;
```

## Topics

### Positions
- [AVCaptureDevice.Position.front](./position-swift.enum/front.md)
  A position on the user-facing side of an iOS device.
- [AVCaptureDevice.Position.back](./position-swift.enum/back.md)
  A position on the subject-facing side of an iOS device.
- [AVCaptureDevice.Position.unspecified](./position-swift.enum/unspecified.md)
  A position that’s unspecified.
### Initializers
- [init?(rawValue: Int)](./position-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying a device
- [var uniqueID: String](./uniqueid.md)
  An identifier that uniquely identifies the device.
- [var modelID: String](./modelid.md)
  A model identifier for the device.
- [var localizedName: String](./localizedname.md)
  A localized device name for display in the user interface.
- [var manufacturer: String](./manufacturer.md)
  A human-readable string for the manufacturer of the device.
- [var deviceType: AVCaptureDevice.DeviceType](./devicetype-swift.property.md)
  The type of device, such as a built-in microphone or wide-angle camera.
- [AVCaptureDevice.DeviceType](./devicetype-swift.struct.md)
  A structure that defines the device types the framework supports.
- [var position: AVCaptureDevice.Position](./position-swift.property.md)
  The physical position of the capture device hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.enum)*