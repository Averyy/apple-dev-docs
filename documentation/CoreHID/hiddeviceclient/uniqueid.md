# uniqueID

**Framework**: Core HID  
**Kind**: property  
**Role**: Instance Property

A unique ID for the device, if there is one.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var uniqueID: String? { get }
```

## Discussion

This ID is software based, and isn’t associated with the device itself. It is typically set to help facilitate driver or client matching.

## See Also

### Get device information
- [let descriptor: Data](./descriptor.md)
  The HID specification compliant report descriptor for the associated HID device.
- [let deviceUsages: [HIDUsage]](./deviceusages.md)
  A convenient list of all the usages that the device supports.
- [var isBuiltIn: Bool](./isbuiltin.md)
  A Boolean value that determines whether the device is built-in to the system or an external peripheral.
- [var localizationCode: HIDDeviceLocalizationCode](./localizationcode.md)
  A location code that specifies the HID compliant localization code, if there is one.
- [var locationID: UInt64?](./locationid.md)
  The location ID for the device, if there is one.
- [var manufacturer: String?](./manufacturer.md)
  The manufacturer of the device, if known.
- [var modelNumber: String?](./modelnumber.md)
  The model number for the device, if known.
- [let primaryUsage: HIDUsage](./primaryusage.md)
  The HID specification compliant usage for the device.
- [var product: String?](./product.md)
  The product name for the device, if known.
- [let productID: UInt32](./productid.md)
  The product ID for the device.
- [var serialNumber: String?](./serialnumber.md)
  The serial number of the device, if known.
- [var transport: HIDDeviceTransport?](./transport.md)
  The data transport for the device.
- [let vendorID: UInt32](./vendorid.md)
  The vendor ID for the device.
- [var versionNumber: UInt64?](./versionnumber.md)
  The version of the device, if known.
- [var elements: [HIDElement]](./elements.md)
  All HID elements associated with the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/uniqueid)*