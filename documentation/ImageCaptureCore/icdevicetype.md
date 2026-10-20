# ICDeviceType

**Framework**: ImageCaptureCore  
**Kind**: enum  
**Role**: Enumeration

The type of image capture device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
enum ICDeviceType
```

```c
enum ICDeviceType : NSUInteger;
```

## Topics

### Constants
- [ICDeviceType.camera](./icdevicetype/camera.md)
  The device is a camera.
- [ICDeviceType.scanner](./icdevicetype/scanner.md)
  The device is a scanner.
### Initializers
- [init?(rawValue: UInt)](./icdevicetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting a Device’s Type and Location
- [var type: ICDeviceType](./icdevice/type.md)
  A combination of the device’s type and its location type.
- [enum ICDeviceTypeMask](./icdevicetypemask.md)
  Masks for detecting different device types.
- [var locationDescription: String?](./icdevice/locationdescription.md)
  A nonlocalized location description for the device.
- [var modulePath: String](./icdevice/modulepath.md)
  The file system path of the device module associated with this device.
- [var moduleVersion: String?](./icdevice/moduleversion.md)
  The bundle version of the device module associated with this device.
- [enum ICDeviceLocationType](./icdevicelocationtype.md)
  The location of the image capture device.
- [enum ICDeviceLocationTypeMask](./icdevicelocationtypemask.md)
  Masks for detecting different device locations.
- [struct ICDeviceLocationOptions](./icdevicelocationoptions.md)
  Options for the location of the image capture device.
- [var usbLocationID: Int32](./icdevice/usblocationid.md)
  The USB location that the device is occupying.
- [var usbProductID: Int32](./icdevice/usbproductid.md)
  The USB Product ID (PID) associated with the device.
- [var usbVendorID: Int32](./icdevice/usbvendorid.md)
  The USB Vendor ID (VID) associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicetype)*