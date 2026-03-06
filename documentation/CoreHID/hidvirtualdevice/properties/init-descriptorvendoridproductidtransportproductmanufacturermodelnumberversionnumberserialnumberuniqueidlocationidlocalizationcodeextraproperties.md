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

- `descriptor`: See [`descriptor`](hidvirtualdevice/properties/descriptor.md).
- `vendorID`: See [`vendorID`](hidvirtualdevice/properties/vendorid.md).
- `productID`: See [`productID`](hidvirtualdevice/properties/productid.md).
- `transport`: See [`transport`](hidvirtualdevice/properties/transport.md).
- `product`: See [`product`](hidvirtualdevice/properties/product.md).
- `manufacturer`: See [`manufacturer`](hidvirtualdevice/properties/manufacturer.md).
- `modelNumber`: See [`modelNumber`](hidvirtualdevice/properties/modelnumber.md).
- `versionNumber`: See [`versionNumber`](hidvirtualdevice/properties/versionnumber.md).
- `serialNumber`: See [`serialNumber`](hidvirtualdevice/properties/serialnumber.md).
- `uniqueID`: See [`uniqueID`](hidvirtualdevice/properties/uniqueid.md).
- `locationID`: See [`locationID`](hidvirtualdevice/properties/locationid.md).
- `localizationCode`: See [`localizationCode`](hidvirtualdevice/properties/localizationcode.md).
- `extraProperties`: A catch-all for uncommon or device specific properties that aren’t listed above. This parameter is typically only for advanced users that need additional control over device functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties/init(descriptor:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:extraproperties:))*