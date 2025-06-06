# CBMutableCharacteristic

**Framework**: Core Bluetooth  
**Kind**: class

A characteristic of a local peripheral’s service.

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
class CBMutableCharacteristic
```

#### Overview

[`CBMutableCharacteristic`](cbmutablecharacteristic.md) objects represent the characteristics of a local peripheral’s service. This class adds write access to many of the properties in the [`CBCharacteristic`](cbcharacteristic.md) class, which it inherits from.

You use this class to create a characteristic and to set its properties and permissions as desired. After you create and add a characteristic to a local service, you can publish it (and the service) to the peripheral’s local database with the [`add(_:)`](cbperipheralmanager/add(_:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class. After you publish a characteristic, Core Bluetooth caches the characteristic and you can’t make changes to it.

## Topics

### Creating a Mutable Characteristic
- [init(type: CBUUID, properties: CBCharacteristicProperties, value: Data?, permissions: CBAttributePermissions)](cbmutablecharacteristic/init(type:properties:value:permissions:).md)
  Creates a mutable characteristic with specified permissions, properties, and value.
### Managing a Mutable Characteristic
- [var value: Data?](cbmutablecharacteristic/value.md)
  The value of the characteristic.
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

## Relationships

### Inherits From
- [CBCharacteristic](cbcharacteristic.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBService](cbservice.md)
  A collection of data and associated behaviors that accomplish a function or feature of a device.
- [class CBMutableService](cbmutableservice.md)
  A service with writeable property values.
- [class CBCharacteristic](cbcharacteristic.md)
  A characteristic of a remote peripheral’s service.
- [class CBDescriptor](cbdescriptor.md)
  An object that provides further information about a remote peripheral’s characteristic.
- [class CBMutableDescriptor](cbmutabledescriptor.md)
  An object that provides additional information about a local peripheral’s characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic)*