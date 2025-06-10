# ICDeviceLocationType

**Framework**: ImageCaptureCore  
**Kind**: enum

The location of the image capture device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
enum ICDeviceLocationType
```

## Topics

### Constants
- [ICDeviceLocationType.bluetooth](icdevicelocationtype/bluetooth.md)
  A paired Bluetooth device.
- [ICDeviceLocationType.bonjour](icdevicelocationtype/bonjour.md)
  A supported Bonjour services device.
- [ICDeviceLocationType.local](icdevicelocationtype/local.md)
  A device that’s directly attached to the Mac through its USB or FireWire port.
- [ICDeviceLocationType.shared](icdevicelocationtype/shared.md)
  A device that’s shared by other Mac hosts.
### Initializers
- [init?(rawValue: UInt)](icdevicelocationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: ICDeviceType](icdevice/type.md)
  A combination of the device’s type and its location type.
- [enum ICDeviceType](icdevicetype.md)
  The type of image capture device.
- [enum ICDeviceTypeMask](icdevicetypemask.md)
  Masks for detecting different device types.
- [var locationDescription: String?](icdevice/locationdescription.md)
  A nonlocalized location description for the device.
- [var modulePath: String](icdevice/modulepath.md)
  The file system path of the device module associated with this device.
- [var moduleVersion: String?](icdevice/moduleversion.md)
  The bundle version of the device module associated with this device.
- [enum ICDeviceLocationTypeMask](icdevicelocationtypemask.md)
  Masks for detecting different device locations.
- [struct ICDeviceLocationOptions](icdevicelocationoptions.md)
  Options for the location of the image capture device.
- [var usbLocationID: Int32](icdevice/usblocationid.md)
  The USB location that the device is occupying.
- [var usbProductID: Int32](icdevice/usbproductid.md)
  The USB Product ID (PID) associated with the device.
- [var usbVendorID: Int32](icdevice/usbvendorid.md)
  The USB Vendor ID (VID) associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicelocationtype)*