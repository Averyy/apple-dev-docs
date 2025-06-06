# productID

**Framework**: Core HID  
**Kind**: property

The product ID for the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
final let productID: UInt32
```

#### Discussion

The product ID combines with the [`vendorID`](hiddeviceclient/vendorid.md) to specify the exact product. Without knowing the vendor, the product ID is meaningless. Look for vendor specific documentation for more details on the assigned product IDs for a vendor’s products.

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
- [var serialNumber: String?](hiddeviceclient/serialnumber.md)
  The serial number of the device, if known.
- [var transport: HIDDeviceTransport?](hiddeviceclient/transport.md)
  The data transport for the device.
- [var uniqueID: String?](hiddeviceclient/uniqueid.md)
  A unique ID for the device, if there is one.
- [let vendorID: UInt32](hiddeviceclient/vendorid.md)
  The vendor ID for the device.
- [var versionNumber: UInt64?](hiddeviceclient/versionnumber.md)
  The version of the device, if known.
- [var elements: [HIDElement]](hiddeviceclient/elements.md)
  All HID elements associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/productid)*