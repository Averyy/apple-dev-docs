# CBAttribute

**Framework**: Core Bluetooth  
**Kind**: class

A representation of common aspects of services offered by a peripheral.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CBAttribute
```

#### Overview

Concrete subclasses of [`CBAttribute`](cbattribute.md) (and their mutable counterparts) represent the services a peripheral offers, the characteristics of those services, and the descriptors attached to those characteristics. The concrete subclasses are:

- [`CBService`](cbservice.md)
- [`CBCharacteristic`](cbcharacteristic.md)
- [`CBDescriptor`](cbdescriptor.md)

## Topics

### Identifying an Attribute
- [var uuid: CBUUID](cbattribute/uuid.md)
  The Bluetooth-specific UUID of the attribute.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CBCharacteristic](cbcharacteristic.md)
- [CBDescriptor](cbdescriptor.md)
- [CBService](cbservice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBPeripheral](cbperipheral.md)
  A remote peripheral device.
- [protocol CBPeripheralDelegate](cbperipheraldelegate.md)
  A protocol that provides updates on the use of a peripheral’s services.
- [class CBPeripheralManager](cbperipheralmanager.md)
  An object that manages and advertises peripheral services exposed by this app.
- [protocol CBPeripheralManagerDelegate](cbperipheralmanagerdelegate.md)
  A protocol that provides updates for local peripheral state and interactions with remote central devices.
- [struct CBAttributePermissions](cbattributepermissions.md)
  Values that represent the read, write, and encryption permissions for a characteristic’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattribute)*