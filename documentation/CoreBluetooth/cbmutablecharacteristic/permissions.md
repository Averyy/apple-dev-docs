# permissions

**Framework**: Core Bluetooth  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, readwrite) CBAttributePermissions permissions;
```

## Discussion

Characteristic permissions represent the read, write, and encryption permissions for a characteristic’s value. For a complete list and discussion of the available characteristic permissions, see [`CBAttributePermissions`](../cbattributepermissions.md).

## See Also

### Managing a Mutable Characteristic
- [var value: Data?](./value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](./descriptors.md)
  An array of the characteristic’s descriptors.
- [var properties: CBCharacteristicProperties](./properties.md)
  The properties of the characteristic.
- [struct CBAttributePermissions](../cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.
- [var subscribedCentrals: [CBCentral]?](./subscribedcentrals.md)
  A list of centrals that are currently subscribed to the characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic/permissions)*