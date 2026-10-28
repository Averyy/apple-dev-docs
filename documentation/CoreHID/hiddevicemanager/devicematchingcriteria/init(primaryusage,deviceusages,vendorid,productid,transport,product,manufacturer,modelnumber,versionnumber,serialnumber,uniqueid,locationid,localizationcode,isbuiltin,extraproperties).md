# init(primaryUsage:deviceUsages:vendorID:productID:transport:product:manufacturer:modelNumber:versionNumber:serialNumber:uniqueID:locationID:localizationCode:isBuiltIn:extraProperties:)

**Framework**: Core HID  
**Kind**: init  
**Role**: Initializer

Creates one set of matching criteria for HID devices.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(primaryUsage: HIDUsage? = nil, deviceUsages: [HIDUsage]? = nil, vendorID: UInt32? = nil, productID: UInt32? = nil, transport: HIDDeviceTransport? = nil, product: String? = nil, manufacturer: String? = nil, modelNumber: String? = nil, versionNumber: UInt64? = nil, serialNumber: String? = nil, uniqueID: String? = nil, locationID: UInt64? = nil, localizationCode: HIDDeviceLocalizationCode? = nil, isBuiltIn: Bool? = nil, extraProperties: Dictionary<String, AnyObject>? = nil)
```

## Mentions

- [Communicating with human interface devices](../../communicatingwithhiddevices.md)

## Discussion

This `init` method is the only way to create matching criteria for discovering HID devices connected to the system. All parameters are optional; if none are specified, every discoverable device is matched.

Created [`HIDDeviceManager.DeviceMatchingCriteria`](../devicematchingcriteria.md) are used by being passed to [`monitorNotifications(matchingCriteria:)`](../monitornotifications%28matchingcriteria%29.md).

## Parameters

- `primaryUsage`: See [`primaryUsage`](./primaryusage.md).
- `deviceUsages`: See [`deviceUsages`](./deviceusages.md).
- `vendorID`: See [`vendorID`](./vendorid.md).
- `productID`: See [`productID`](./productid.md).
- `transport`: See [`transport`](./transport.md).
- `product`: See [`product`](./product.md).
- `manufacturer`: See [`manufacturer`](./manufacturer.md).
- `modelNumber`: See [`modelNumber`](./modelnumber.md).
- `versionNumber`: See [`versionNumber`](./versionnumber.md).
- `serialNumber`: See [`serialNumber`](./serialnumber.md).
- `uniqueID`: See [`uniqueID`](./uniqueid.md).
- `locationID`: See [`locationID`](./locationid.md).
- `localizationCode`: See [`localizationCode`](./localizationcode.md).
- `isBuiltIn`: See [`isBuiltIn`](./isbuiltin.md).
- `extraProperties`: A catch-all for uncommon or device specific criteria not listed above. This parameter is typically only for advanced users that need additional control over the matching process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria/init(primaryusage:deviceusages:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:isbuiltin:extraproperties:))*