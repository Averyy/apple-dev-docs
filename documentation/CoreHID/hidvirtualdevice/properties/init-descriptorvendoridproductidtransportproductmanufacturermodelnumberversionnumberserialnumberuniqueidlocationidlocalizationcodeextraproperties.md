# init(descriptor:vendorID:productID:transport:product:manufacturer:modelNumber:versionNumber:serialNumber:uniqueID:locationID:localizationCode:extraProperties:)

**Framework**: Core HID  
**Kind**: init

Creates a set of properties for a virtual device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(descriptor: Data, vendorID: UInt32, productID: UInt32? = nil, transport: HIDDeviceTransport? = nil, product: String? = nil, manufacturer: String? = nil, modelNumber: String? = nil, versionNumber: UInt64? = nil, serialNumber: String? = nil, uniqueID: String? = nil, locationID: UInt64? = nil, localizationCode: HIDDeviceLocalizationCode? = nil, extraProperties: Dictionary<String, AnyObject>? = nil)
```

## Mentions

- [Creating virtual devices](creatingvirtualdevices.md)

#### Discussion

Properties must be specified during the creation of a virtual device using [`init(properties:)`](hidvirtualdevice/init(properties:).md).

## Parameters

- `descriptor`: See  .
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
- `extraProperties`: A catch-all for uncommon or device specific properties that aren’t listed above. This parameter is typically only for advanced users that need additional control over device functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties/init(descriptor:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:extraproperties:))*