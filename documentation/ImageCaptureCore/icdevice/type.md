# type

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A combination of the device’s type and its location type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var type: ICDeviceType { get }
```

```objc
@property (nonatomic, readonly) ICDeviceType type;
```

#### Discussion

This property combines the device’s type, for example [`ICDeviceType.camera`](../icdevicetype/camera.md), with its location type, for example [`ICDeviceLocationType.bluetooth`](../icdevicelocationtype/bluetooth.md).

To isolate the device’s type, perform bitwise `AND` on this property with an [`ICDeviceTypeMask`](../icdevicetypemask.md).

To isolate the device’s location type, perform bitwise `AND` on this property with an [`ICDeviceLocationTypeMask`](../icdevicelocationtypemask.md).

## See Also

### Inspecting a Device’s Type and Location
- [enum ICDeviceType](../icdevicetype.md)
  The type of image capture device.
- [enum ICDeviceTypeMask](../icdevicetypemask.md)
  Masks for detecting different device types.
- [var locationDescription: String?](./locationdescription.md)
  A nonlocalized location description for the device.
- [var modulePath: String](./modulepath.md)
  The file system path of the device module associated with this device.
- [var moduleVersion: String?](./moduleversion.md)
  The bundle version of the device module associated with this device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/type)*