# init(primaryUsage:deviceUsages:vendorID:productID:transport:product:manufacturer:modelNumber:versionNumber:serialNumber:uniqueID:locationID:localizationCode:isBuiltIn:extraProperties:)

**Framework**: Core HID  
**Kind**: init

Creates one set of matching criteria for HID devices.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(primaryUsage: HIDUsage? = nil, deviceUsages: [HIDUsage]? = nil, vendorID: UInt32? = nil, productID: UInt32? = nil, transport: HIDDeviceTransport? = nil, product: String? = nil, manufacturer: String? = nil, modelNumber: String? = nil, versionNumber: UInt64? = nil, serialNumber: String? = nil, uniqueID: String? = nil, locationID: UInt64? = nil, localizationCode: HIDDeviceLocalizationCode? = nil, isBuiltIn: Bool? = nil, extraProperties: Dictionary<String, AnyObject>? = nil)
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Discussion

This `init` method is the only way to create matching criteria for discovering HID devices connected to the system. All parameters are optional; if none are specified, every discoverable device is matched.

Created [`HIDDeviceManager.DeviceMatchingCriteria`](hiddevicemanager/devicematchingcriteria.md) are used by being passed to [`monitorNotifications(matchingCriteria:)`](hiddevicemanager/monitornotifications(matchingcriteria:).md).

## Parameters

- `primaryUsage`: See  .
- `deviceUsages`: See  .
- `vendorID`: See  .
- `productID`: See  .
- `transport`: See  .
- `product`: See  .
- `manufacturer`: See  .
- `modelNumber`: See  .
- `versionNumber`: See  .
- `serialNumber`: See  .
- `uniqueID`: See  .
- `locationID`: See  .
- `localizationCode`: See  .
- `isBuiltIn`: See  .
- `extraProperties`: A catch-all for uncommon or device specific criteria not listed above. This parameter is typically only for advanced users that need additional control over the matching process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria/init(primaryusage:deviceusages:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:isbuiltin:extraproperties:))*