# descriptors

**Framework**: Core Bluetooth  
**Kind**: property

An array of the characteristic’s descriptors.

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
var descriptors: [CBDescriptor]? { get set }
```

#### Discussion

The value of this property is an array of [`CBDescriptor`](cbdescriptor.md) objects that provide more information about a characteristic’s value. For example, they may describe the value in human-readable form and describe how to format the value for presentation purposes. For more information about characteristic descriptors, see [`CBDescriptor`](cbdescriptor.md).

## See Also

- [var value: Data?](cbmutablecharacteristic/value.md)
  The value of the characteristic.
- [var properties: CBCharacteristicProperties](cbmutablecharacteristic/properties.md)
  The properties of the characteristic.
- [var permissions: CBAttributePermissions](cbmutablecharacteristic/permissions.md)
  The permissions of the characteristic value.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.
- [var subscribedCentrals: [CBCentral]?](cbmutablecharacteristic/subscribedcentrals.md)
  A list of centrals that are currently subscribed to the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/descriptors)*