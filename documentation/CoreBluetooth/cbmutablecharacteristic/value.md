# value

**Framework**: Core Bluetooth  
**Kind**: property

The value of the characteristic.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var value: Data? { get set }
```

#### Discussion

This property contains the value of the characteristic. For example, a temperature measurement characteristic of a health thermometer service may have a value that indicates a temperature in Celsius.

## See Also

- [var descriptors: [CBDescriptor]?](cbmutablecharacteristic/descriptors.md)
  An array of the characteristic’s descriptors.
- [var properties: CBCharacteristicProperties](cbmutablecharacteristic/properties.md)
  The properties of the characteristic.
- [var permissions: CBAttributePermissions](cbmutablecharacteristic/permissions.md)
  The permissions of the characteristic value.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.
- [var subscribedCentrals: [CBCentral]?](cbmutablecharacteristic/subscribedcentrals.md)
  A list of centrals that are currently subscribed to the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/value)*