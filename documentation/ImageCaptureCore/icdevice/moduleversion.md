# moduleVersion

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The bundle version of the device module associated with this device.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var moduleVersion: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * moduleVersion;
```

#### Discussion

The bundle version may change if an existing device module associated with this device is updated or a new device module for this device is installed.

## See Also

### Inspecting a Device’s Type and Location
- [var type: ICDeviceType](./type.md)
  A combination of the device’s type and its location type.
- [enum ICDeviceType](../icdevicetype.md)
  The type of image capture device.
- [enum ICDeviceTypeMask](../icdevicetypemask.md)
  Masks for detecting different device types.
- [var locationDescription: String?](./locationdescription.md)
  A nonlocalized location description for the device.
- [var modulePath: String](./modulepath.md)
  The file system path of the device module associated with this device.
- [enum ICDeviceLocationType](../icdevicelocationtype.md)
  The location of the image capture device.
- [enum ICDeviceLocationTypeMask](../icdevicelocationtypemask.md)
  Masks for detecting different device locations.
- [struct ICDeviceLocationOptions](../icdevicelocationoptions.md)
  Options for the location of the image capture device.
- [var usbLocationID: Int32](./usblocationid.md)
  The USB location that the device is occupying.
- [var usbProductID: Int32](./usbproductid.md)
  The USB Product ID (PID) associated with the device.
- [var usbVendorID: Int32](./usbvendorid.md)
  The USB Vendor ID (VID) associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/moduleversion)*