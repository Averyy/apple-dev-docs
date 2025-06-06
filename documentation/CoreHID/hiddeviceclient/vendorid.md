# vendorID

**Framework**: Core HID  
**Kind**: property

The vendor ID for the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
final let vendorID: UInt32
```

#### Discussion

The vendor ID designates the vendor that produced the device. It can be combined with [`productID`](hiddeviceclient/productid.md) to determine the exact device.

More information about vendor IDs can be found online. The vendor ID associated with a HID device is typically a USB vendor ID (see [`Information for Developers`](https://developer.apple.comhttps://www.usb.org/developers)), but can be something else, such as a Bluetooth vendor ID (see [`Assigned Numbers`](https://developer.apple.comhttps://www.bluetooth.com/specifications/assigned-numbers/) in the Bluetooth specification).

## See Also

- [var descriptor: Data](hiddeviceclient/descriptor.md)
  The HID specification compliant report descriptor for the associated HID device.
- [var deviceUsages: [HIDUsage]](hiddeviceclient/deviceusages.md)
  A convenient list of all the usages that the device supports.
- [var isBuiltIn: Bool](hiddeviceclient/isbuiltin.md)
  A Boolean value that determines whether the device is built-in to the system or an external peripheral.
- [var localizationCode: HIDDeviceLocalizationCode](hiddeviceclient/localizationcode.md)
  A location code that specifies the HID compliant localization code, if there is one.
- [var locationID: UInt64?](hiddeviceclient/locationid.md)
  The location ID for the device, if there is one.
- [var manufacturer: String?](hiddeviceclient/manufacturer.md)
  The manufacturer of the device, if known.
- [var modelNumber: String?](hiddeviceclient/modelnumber.md)
  The model number for the device, if known.
- [let primaryUsage: HIDUsage](hiddeviceclient/primaryusage.md)
  The HID specification compliant usage for the device.
- [var product: String?](hiddeviceclient/product.md)
  The product name for the device, if known.
- [let productID: UInt32](hiddeviceclient/productid.md)
  The product ID for the device.
- [var serialNumber: String?](hiddeviceclient/serialnumber.md)
  The serial number of the device, if known.
- [var transport: HIDDeviceTransport?](hiddeviceclient/transport.md)
  The data transport for the device.
- [var uniqueID: String?](hiddeviceclient/uniqueid.md)
  A unique ID for the device, if there is one.
- [var versionNumber: UInt64?](hiddeviceclient/versionnumber.md)
  The version of the device, if known.
- [var elements: [HIDElement]](hiddeviceclient/elements.md)
  All HID elements associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/vendorid)*