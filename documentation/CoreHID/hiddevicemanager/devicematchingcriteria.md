# HIDDeviceManager.DeviceMatchingCriteria

**Framework**: Core HID  
**Kind**: struct

Matching criteria used to filter HID devices.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct DeviceMatchingCriteria
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

Use this class to filter the HID devices on the system using common properties, such as [`HIDUsage`](hidusage.md). All matching parameters are specified using [`init(primaryUsage:deviceUsages:vendorID:productID:transport:product:manufacturer:modelNumber:versionNumber:serialNumber:uniqueID:locationID:localizationCode:isBuiltIn:extraProperties:)`](hiddevicemanager/devicematchingcriteria/init(primaryusage:deviceusages:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:isbuiltin:extraproperties:).md).

Uncommon criteria not available as properties can be specified in the `extraProperties` parameter of `init`.

## Topics

### Initializers
- [init(primaryUsage: HIDUsage?, deviceUsages: [HIDUsage]?, vendorID: UInt32?, productID: UInt32?, transport: HIDDeviceTransport?, product: String?, manufacturer: String?, modelNumber: String?, versionNumber: UInt64?, serialNumber: String?, uniqueID: String?, locationID: UInt64?, localizationCode: HIDDeviceLocalizationCode?, isBuiltIn: Bool?, extraProperties: Dictionary<String, AnyObject>?)](hiddevicemanager/devicematchingcriteria/init(primaryusage:deviceusages:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:isbuiltin:extraproperties:).md)
  Creates one set of matching criteria for HID devices.
### Instance Properties
- [var deviceUsages: [HIDUsage]?](hiddevicemanager/devicematchingcriteria/deviceusages.md)
  A list of usages supported by the device.
- [var isBuiltIn: Bool?](hiddevicemanager/devicematchingcriteria/isbuiltin.md)
  A Boolean value that indicates whether the device is built-in to the system or external.
- [var localizationCode: HIDDeviceLocalizationCode?](hiddevicemanager/devicematchingcriteria/localizationcode.md)
  A localization code that specifies the HID compliant localization code.
- [var locationID: UInt64?](hiddevicemanager/devicematchingcriteria/locationid.md)
  The location ID for the device.
- [var manufacturer: String?](hiddevicemanager/devicematchingcriteria/manufacturer.md)
  The manufacturer of the device.
- [var modelNumber: String?](hiddevicemanager/devicematchingcriteria/modelnumber.md)
  The model number for the device.
- [var primaryUsage: HIDUsage?](hiddevicemanager/devicematchingcriteria/primaryusage.md)
  The HID specification compliant usage for the device.
- [var product: String?](hiddevicemanager/devicematchingcriteria/product.md)
  The product name for the device.
- [var productID: UInt32?](hiddevicemanager/devicematchingcriteria/productid.md)
  The product ID for the device.
- [var serialNumber: String?](hiddevicemanager/devicematchingcriteria/serialnumber.md)
  The serial number of the device.
- [var transport: HIDDeviceTransport?](hiddevicemanager/devicematchingcriteria/transport.md)
  The data transport for the device.
- [var uniqueID: String?](hiddevicemanager/devicematchingcriteria/uniqueid.md)
  A unique ID for the device.
- [var vendorID: UInt32?](hiddevicemanager/devicematchingcriteria/vendorid.md)
  The vendor ID for the device.
- [var versionNumber: UInt64?](hiddevicemanager/devicematchingcriteria/versionnumber.md)
  The version of the device.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Discovering HID devices from Terminal](discoveringhiddevicesfromterminal.md)
  Identify devices connected to your Mac from the command line.
- [actor HIDDeviceManager](hiddevicemanager.md)
  A helper for discovering human interface devices (HID) connected to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria)*