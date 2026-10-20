# init(descriptor:vendorID:productID:transport:product:manufacturer:modelNumber:versionNumber:serialNumber:uniqueID:locationID:localizationCode:extraProperties:)

**Framework**: Core HID  
**Kind**: init  
**Role**: Initializer

Creates a set of properties for a virtual device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(descriptor: Data, vendorID: UInt32, productID: UInt32? = nil, transport: HIDDeviceTransport? = nil, product: String? = nil, manufacturer: String? = nil, modelNumber: String? = nil, versionNumber: UInt64? = nil, serialNumber: String? = nil, uniqueID: String? = nil, locationID: UInt64? = nil, localizationCode: HIDDeviceLocalizationCode? = nil, extraProperties: Dictionary<String, AnyObject>? = nil)
```

## Mentions

- [Creating virtual devices](../../creatingvirtualdevices.md)

#### Discussion

Properties must be specified during the creation of a virtual device using [`init(properties:)`](../init%28properties%29.md).

## Parameters

- `descriptor`: See [`descriptor`](./descriptor.md).
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
- `extraProperties`: A catch-all for uncommon or device specific properties that aren’t listed above. This parameter is typically only for advanced users that need additional control over device functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties/init(descriptor:vendorid:productid:transport:product:manufacturer:modelnumber:versionnumber:serialnumber:uniqueid:locationid:localizationcode:extraproperties:))*