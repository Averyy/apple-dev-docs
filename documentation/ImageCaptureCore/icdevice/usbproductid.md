# usbProductID

**Framework**: ImageCaptureCore  
**Kind**: property

The USB Product ID (PID) associated with the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var usbProductID: Int32 { get }
```

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
- [struct ICDeviceLocationOptions](icdevicelocationoptions.md)
  Options for the location of the image capture device.
- [var usbLocationID: Int32](icdevice/usblocationid.md)
  The USB location that the device is occupying.
- [var usbVendorID: Int32](icdevice/usbvendorid.md)
  The USB Vendor ID (VID) associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/usbproductid)*