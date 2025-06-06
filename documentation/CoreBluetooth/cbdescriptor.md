# CBDescriptor

**Framework**: Core Bluetooth  
**Kind**: class

An object that provides further information about a remote peripheral’s characteristic.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CBDescriptor
```

#### Overview

[`CBDescriptor`](cbdescriptor.md) and its subclass [`CBMutableDescriptor`](cbmutabledescriptor.md) represent a descriptor of a peripheral’s characteristic. In partcular, [`CBDescriptor`](cbdescriptor.md) objects represent the descriptors of a remote peripheral’s characteristic. Descriptors provide further information about a characteristic’s value. For example, they may describe the value in human-readable form and describe how to format the value for presentation purposes. Characteristic descriptors also indicate whether a characteristic’s value indicates or notifies a client (a central) when the value of the characteristic changes.

[`CBUUID`](cbuuid.md) details six predefined descriptors and their corresponding value types. [`CBDescriptor`](cbdescriptor.md) lists the predefined descriptors and the [`CBUUID`](cbuuid.md) constants that represent them.

| Descriptor type | Descriptor constant |
| --- | --- |
| Characteristic extended properties | [`CBUUIDCharacteristicExtendedPropertiesString`](cbuuidcharacteristicextendedpropertiesstring.md) |
| Characteristic user description | [`CBUUIDCharacteristicUserDescriptionString`](cbuuidcharacteristicuserdescriptionstring.md) |
| Client characteristic configuration | [`CBUUIDClientCharacteristicConfigurationString`](cbuuidclientcharacteristicconfigurationstring.md) |
| Server characteristic configuration | [`CBUUIDServerCharacteristicConfigurationString`](cbuuidservercharacteristicconfigurationstring.md) |
| Characteristic format | [`CBUUIDCharacteristicFormatString`](cbuuidcharacteristicformatstring.md) |
| Characteristic aggregate format | [`CBUUIDCharacteristicAggregateFormatString`](cbuuidcharacteristicaggregateformatstring.md) |

## Topics

### Identifying a Descriptor
- [var characteristic: CBCharacteristic?](cbdescriptor/characteristic.md)
  The characteristic to which this descriptor belongs.
### Accessing Descriptor Data
- [var value: Any?](cbdescriptor/value.md)
  The value of the descriptor.

## Relationships

### Inherits From
- [CBAttribute](cbattribute.md)
### Inherited By
- [CBMutableDescriptor](cbmutabledescriptor.md)
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
- [class CBMutableDescriptor](cbmutabledescriptor.md)
  An object that provides additional information about a local peripheral’s characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbdescriptor)*