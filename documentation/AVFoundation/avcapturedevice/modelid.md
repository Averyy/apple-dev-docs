# modelID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A model identifier for the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
var modelID: String { get }
```

```objc
@property (nonatomic, readonly) NSString * modelID;
```

## Discussion

The value of this property is an identifier unique to all devices of the same model. The value is persistent across device connections and disconnections, and across different systems. For example, the model identifier of a built-in camera on two identical iPhone models is the same even though they’re different physical devices.

## See Also

### Identifying a device
- [var uniqueID: String](./uniqueid.md)
  An identifier that uniquely identifies the device.
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
- [AVCaptureDevice.Position](./position-swift.enum.md)
  Constants that indicate the physical position of a capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/modelid)*