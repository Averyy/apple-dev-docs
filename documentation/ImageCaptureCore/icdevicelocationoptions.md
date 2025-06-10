# ICDeviceLocationOptions

**Framework**: ImageCaptureCore  
**Kind**: struct

Options for the location of the image capture device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICDeviceLocationOptions
```

## Topics

### Creating Location Options
- [init(rawValue: String)](icdevicelocationoptions/init(rawvalue:).md)
  Creates ImageCaptureCore location options.
### Determining a Location
- [static let descriptionBluetooth: ICDeviceLocationOptions](icdevicelocationoptions/descriptionbluetooth.md)
  A paired Bluetooth device.
- [static let descriptionFireWire: ICDeviceLocationOptions](icdevicelocationoptions/descriptionfirewire.md)
  A device that’s directly attached to the Mac through its FireWire port.
- [static let descriptionMassStorage: ICDeviceLocationOptions](icdevicelocationoptions/descriptionmassstorage.md)
  A mass storage device.
- [static let descriptionUSB: ICDeviceLocationOptions](icdevicelocationoptions/descriptionusb.md)
  A device that’s directly attached to the Mac through its USB port.

## Relationships

### Conforms To
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
- [enum ICDeviceLocationType](icdevicelocationtype.md)
  The location of the image capture device.
- [enum ICDeviceLocationTypeMask](icdevicelocationtypemask.md)
  Masks for detecting different device locations.
- [var usbLocationID: Int32](icdevice/usblocationid.md)
  The USB location that the device is occupying.
- [var usbProductID: Int32](icdevice/usbproductid.md)
  The USB Product ID (PID) associated with the device.
- [var usbVendorID: Int32](icdevice/usbvendorid.md)
  The USB Vendor ID (VID) associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicelocationoptions)*