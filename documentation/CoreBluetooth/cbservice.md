# CBService

**Framework**: Core Bluetooth  
**Kind**: class

A collection of data and associated behaviors that accomplish a function or feature of a device.

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
class CBService
```

#### Overview

[`CBService`](cbservice.md) objects represent services of a remote peripheral. Services are either primary or secondary and may contain multiple characteristics or included services (references to other services).

## Topics

### Identifying a Service
- [var peripheral: CBPeripheral?](cbservice/peripheral.md)
  The peripheral to which this service belongs.
- [var isPrimary: Bool](cbservice/isprimary.md)
  A Boolean value that indicates whether the type of service is primary or secondary.
### Accessing Service Data
- [var characteristics: [CBCharacteristic]?](cbservice/characteristics.md)
  A list of characteristics discovered in this service.
- [var includedServices: [CBService]?](cbservice/includedservices.md)
  A list of included services discovered in this service.

## Relationships

### Inherits From
- [CBAttribute](cbattribute.md)
### Inherited By
- [CBMutableService](cbmutableservice.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBMutableService](cbmutableservice.md)
  A service with writeable property values.
- [class CBCharacteristic](cbcharacteristic.md)
  A characteristic of a remote peripheral’s service.
- [class CBMutableCharacteristic](cbmutablecharacteristic.md)
  A characteristic of a local peripheral’s service.
- [class CBDescriptor](cbdescriptor.md)
  An object that provides further information about a remote peripheral’s characteristic.
- [class CBMutableDescriptor](cbmutabledescriptor.md)
  An object that provides additional information about a local peripheral’s characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbservice)*