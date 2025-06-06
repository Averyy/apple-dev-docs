# CBMutableDescriptor

**Framework**: Core Bluetooth  
**Kind**: class

An object that provides additional information about a local peripheral’s characteristic.

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
class CBMutableDescriptor
```

#### Overview

You use the [`CBMutableDescriptor`](cbmutabledescriptor.md) class to create a local characteristic descriptor. After you create a descriptor and associate it with a local characteristic, you can publish it to the peripheral’s local database using the [`add(_:)`](cbperipheralmanager/add(_:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class. This also publishes the characteristic and local service to which the descriptor belongs. After you publish a local descriptor, Core Bluetooth caches the descriptor and you can no longer make changes to it.

[`CBUUID`](cbuuid.md) details predefined descriptor types and their corresponding value types. That said, only two of these are currently supported when creating local, mutable descriptors: the characteristic user description descriptor and the characteristic format descriptor. [`CBUUID`](cbuuid.md) declares these as the constants [`CBUUIDCharacteristicUserDescriptionString`](cbuuidcharacteristicuserdescriptionstring.md) and [`CBUUIDCharacteristicFormatString`](cbuuidcharacteristicformatstring.md), respectively. The system automatically creates the extended properties descriptor and the client configuration descriptor, depending on the properties of the characteristic to which the descriptor belongs.

## Topics

### Creating a Mutable Descriptor
- [init(type: CBUUID, value: Any?)](cbmutabledescriptor/init(type:value:).md)
  Creates a mutable descriptor with a specified value.

## Relationships

### Inherits From
- [CBDescriptor](cbdescriptor.md)
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
- [class CBMutableCharacteristic](cbmutablecharacteristic.md)
  A characteristic of a local peripheral’s service.
- [class CBDescriptor](cbdescriptor.md)
  An object that provides further information about a remote peripheral’s characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor)*