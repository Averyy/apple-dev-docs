# deviceType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The type of device, such as a built-in microphone or wide-angle camera.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var deviceType: AVCaptureDevice.DeviceType { get }
```

```objc
@property (nonatomic, readonly) AVCaptureDeviceType deviceType;
```

#### Discussion

Use the [`default(_:for:position:)`](./default%28_,for,position%29.md) method or the [`AVCaptureDevice.DiscoverySession`](./discoverysession.md) class to find capture devices by device type.

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
- [AVCaptureDevice.DeviceType](./devicetype-swift.struct.md)
  A structure that defines the device types the framework supports.
- [var position: AVCaptureDevice.Position](./position-swift.property.md)
  The physical position of the capture device hardware.
- [AVCaptureDevice.Position](./position-swift.enum.md)
  Constants that indicate the physical position of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.property)*