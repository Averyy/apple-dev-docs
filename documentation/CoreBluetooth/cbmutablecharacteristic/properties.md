# properties

**Framework**: Core Bluetooth  
**Kind**: property

The properties of the characteristic.

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
var properties: CBCharacteristicProperties { get set }
```

#### Discussion

The properties of a characteristic determine the access to and use of the characteristic’s value and descriptors. For a list of the possible values representing the properties of a characteristic, see the [`CBCharacteristicProperties`](cbcharacteristicproperties.md) enumeration in [`CBCharacteristic`](cbcharacteristic.md). However, you can’t use the [`broadcast`](cbcharacteristicproperties/broadcast.md) and [`extendedProperties`](cbcharacteristicproperties/extendedproperties.md) characteristic properties when creating a mutable characteristic.

## See Also

- [var value: Data?](cbmutablecharacteristic/value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](cbmutablecharacteristic/descriptors.md)
  An array of the characteristic’s descriptors.
- [var permissions: CBAttributePermissions](cbmutablecharacteristic/permissions.md)
  The permissions of the characteristic value.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.
- [var subscribedCentrals: [CBCentral]?](cbmutablecharacteristic/subscribedcentrals.md)
  A list of centrals that are currently subscribed to the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/properties)*