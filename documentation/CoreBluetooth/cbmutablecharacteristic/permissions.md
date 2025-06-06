# permissions

**Framework**: Core Bluetooth  
**Kind**: property

The permissions of the characteristic value.

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
var permissions: CBAttributePermissions { get set }
```

#### Discussion

Characteristic permissions represent the read, write, and encryption permissions for a characteristic’s value. For a complete list and discussion of the available characteristic permissions, see [`CBAttributePermissions`](cbattributepermissions.md).

## See Also

- [var value: Data?](cbmutablecharacteristic/value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](cbmutablecharacteristic/descriptors.md)
  An array of the characteristic’s descriptors.
- [var properties: CBCharacteristicProperties](cbmutablecharacteristic/properties.md)
  The properties of the characteristic.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.
- [var subscribedCentrals: [CBCentral]?](cbmutablecharacteristic/subscribedcentrals.md)
  A list of centrals that are currently subscribed to the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/permissions)*