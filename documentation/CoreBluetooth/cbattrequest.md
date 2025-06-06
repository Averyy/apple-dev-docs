# CBATTRequest

**Framework**: Core Bluetooth  
**Kind**: class

A request that uses the Attribute Protocol (ATT).

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
class CBATTRequest
```

#### Overview

The [`CBATTRequest`](cbattrequest.md) class represents Attribute Protocol (ATT) read and write requests from remote central devices (represented by [`CBCentral`](cbcentral.md) objects). Remote centrals use these ATT requests to read and write characteristic values on local peripherals (represented by [`CBPeripheralManager`](cbperipheralmanager.md) objects). Local peripherals, on the other hand, use the properties of [`CBATTRequest`](cbattrequest.md) objects to respond to the read and write requests appropriately, using the [`respond(to:withResult:)`](cbperipheralmanager/respond(to:withresult:).md) method of the [`CBPeripheralManager`](cbperipheralmanager.md) class.

## Topics

### Requesting to Read and Write Characteristic Values
- [var central: CBCentral](cbattrequest/central.md)
  The remote central device that originated the request.
- [var characteristic: CBCharacteristic](cbattrequest/characteristic.md)
  The characteristic to read or write the value of.
- [var value: Data?](cbattrequest/value.md)
  The data that the central reads from or writes to the peripheral.
- [var offset: Int](cbattrequest/offset.md)
  The zero-based index of the first byte for the read or write request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBManager](cbmanager.md)
  The abstract base class that manages central and peripheral objects.
- [class CBPeer](cbpeer.md)
  An object that represents a remote device.
- [class CBUUID](cbuuid.md)
  A universally unique identifier, as defined by Bluetooth standards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbattrequest)*