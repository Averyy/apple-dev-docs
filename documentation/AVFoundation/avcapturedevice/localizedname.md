# localizedName

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A localized device name for display in the user interface.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var localizedName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * localizedName;
```

## See Also

### Identifying a device
- [var uniqueID: String](./uniqueid.md)
  An identifier that uniquely identifies the device.
- [var modelID: String](./modelid.md)
  A model identifier for the device.
- [var manufacturer: String](./manufacturer.md)
  A human-readable string for the manufacturer of the device.
- [var deviceType: AVCaptureDevice.DeviceType](./devicetype-swift.property.md)
  The type of device, such as a built-in microphone or wide-angle camera.
- [AVCaptureDevice.DeviceType](./devicetype-swift.struct.md)
  A structure that defines the device types the framework supports.
- [var position: AVCaptureDevice.Position](./position-swift.property.md)
  The physical position of the capture device hardware.
- [AVCaptureDevice.Position](./position-swift.enum.md)
  Constants that indicate the physical position of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/localizedname)*