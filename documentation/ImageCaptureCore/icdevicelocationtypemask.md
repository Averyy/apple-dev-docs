# ICDeviceLocationTypeMask

**Framework**: ImageCaptureCore  
**Kind**: enum

Masks for detecting different device locations.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
enum ICDeviceLocationTypeMask
```

## Topics

### Constants
- [ICDeviceLocationTypeMask.bluetooth](icdevicelocationtypemask/bluetooth.md)
  A mask for detecting a paired Bluetooth device.
- [ICDeviceLocationTypeMask.bonjour](icdevicelocationtypemask/bonjour.md)
  A mask for detecting a network device that publishes a Bonjour service.
- [ICDeviceLocationTypeMask.local](icdevicelocationtypemask/local.md)
  A mask for detecting a local device, such as USB or FireWire.
- [ICDeviceLocationTypeMask.remote](icdevicelocationtypemask/remote.md)
  A mask for detecting a remote device, such as a shared, Bonjour, or Bluetooth device.
- [ICDeviceLocationTypeMask.shared](icdevicelocationtypemask/shared.md)
  A mask for detecting a device shared by another Mac host.
### Initializers
- [init?(rawValue: UInt)](icdevicelocationtypemask/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [enum ICDeviceLocationType](icdevicelocationtype.md)
  The location of the image capture device.
- [struct ICDeviceLocationOptions](icdevicelocationoptions.md)
  Options for the location of the image capture device.
- [var usbLocationID: Int32](icdevice/usblocationid.md)
  The USB location that the device is occupying.
- [var usbProductID: Int32](icdevice/usbproductid.md)
  The USB Product ID (PID) associated with the device.
- [var usbVendorID: Int32](icdevice/usbvendorid.md)
  The USB Vendor ID (VID) associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicelocationtypemask)*