# CBCharacteristic

**Framework**: Core Bluetooth  
**Kind**: class

A characteristic of a remote peripheral’s service.

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
class CBCharacteristic
```

#### Overview

[`CBCharacteristic`](cbcharacteristic.md) and its subclass [`CBMutableCharacteristic`](cbmutablecharacteristic.md) represent further information about a peripheral’s service. In particular, [`CBCharacteristic`](cbcharacteristic.md) objects represent the characteristics of a remote peripheral’s service. A characteristic contains a single value and any number of descriptors describing that value. The properties of a characteristic determine how you can use a characteristic’s value, and how you access the descriptors.

## Topics

### Identifying a Characteristic
- [var service: CBService?](cbcharacteristic/service.md)
  The service to which this characteristic belongs.
### Accessing Characteristic Data
- [var value: Data?](cbcharacteristic/value.md)
  The value of the characteristic.
- [var descriptors: [CBDescriptor]?](cbcharacteristic/descriptors.md)
  A list of the descriptors discovered in this characteristic.
- [var properties: CBCharacteristicProperties](cbcharacteristic/properties.md)
  The properties of the characteristic.
- [struct CBCharacteristicProperties](cbcharacteristicproperties.md)
  Values that represent the possible properties of a characteristic.
- [var isNotifying: Bool](cbcharacteristic/isnotifying.md)
  A Boolean value that indicates whether the characteristic is currently notifying a subscribed central of its value.
- [var isBroadcasted: Bool](cbcharacteristic/isbroadcasted.md)
  A Boolean value that indicates whether the characteristic the service broadcasts this characteristic.

## Relationships

### Inherits From
- [CBAttribute](cbattribute.md)
### Inherited By
- [CBMutableCharacteristic](cbmutablecharacteristic.md)
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
- [class CBMutableCharacteristic](cbmutablecharacteristic.md)
  A characteristic of a local peripheral’s service.
- [class CBDescriptor](cbdescriptor.md)
  An object that provides further information about a remote peripheral’s characteristic.
- [class CBMutableDescriptor](cbmutabledescriptor.md)
  An object that provides additional information about a local peripheral’s characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic)*