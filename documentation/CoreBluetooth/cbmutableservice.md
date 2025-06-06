# CBMutableService

**Framework**: Core Bluetooth  
**Kind**: class

A service with writeable property values.

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
class CBMutableService
```

#### Overview

The [`CBMutableService`](cbmutableservice.md) class adds write access to all of the properties in the [`CBService`](cbservice.md) class it inherits from. You use this class to create a service or an included service on a local peripheral device (represented by a [`CBPeripheralManager`](cbperipheralmanager.md) object). After creating a service, you can add it to the peripheral’s local database using the [`add(_:)`](cbperipheralmanager/add(_:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class. After you add a service to the peripheral’s local database, Core Bluetooth caches the service and you can no longer make changes to it.

## Topics

### Creating a Mutable Service
- [init(type: CBUUID, primary: Bool)](cbmutableservice/init(type:primary:).md)
  Creates a newly initialized mutable service specified by UUID and service type.
### Managing a Mutable Service
- [var characteristics: [CBCharacteristic]?](cbmutableservice/characteristics.md)
  A list of characteristics of a service.
- [var includedServices: [CBService]?](cbmutableservice/includedservices.md)
  A list of included services.

## Relationships

### Inherits From
- [CBService](cbservice.md)
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
- [class CBCharacteristic](cbcharacteristic.md)
  A characteristic of a remote peripheral’s service.
- [class CBMutableCharacteristic](cbmutablecharacteristic.md)
  A characteristic of a local peripheral’s service.
- [class CBDescriptor](cbdescriptor.md)
  An object that provides further information about a remote peripheral’s characteristic.
- [class CBMutableDescriptor](cbmutabledescriptor.md)
  An object that provides additional information about a local peripheral’s characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutableservice)*