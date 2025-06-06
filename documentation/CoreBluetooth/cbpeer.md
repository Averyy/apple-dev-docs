# CBPeer

**Framework**: Core Bluetooth  
**Kind**: class

An object that represents a remote device.

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
class CBPeer
```

#### Overview

The [`CBPeer`](cbpeer.md) class is an abstract base class that defines common behavior for objects representing remote devices. You typically don’t create instances of either [`CBPeer`](cbpeer.md) or its concrete subclasses. Instead, the system creates them for you during the process of peer discovery.

Your app takes the role of either a central (by creating an instance of [`CBCentralManager`](cbcentralmanager.md)) or a peripheral (by creating an instance of [`CBPeripheralManager`](cbperipheralmanager.md)), and interacts through the manager with remote devices in the opposite role. During the process of peer discovery, where a central device scans for peripherals advertising services, the system creates objects from the concrete subclasses of [`CBPeer`](cbpeer.md) to represent discovered remote devices. The concrete subclasses of [`CBPeer`](cbpeer.md) are [`CBPeripheral`](cbperipheral.md) and [`CBCentral`](cbcentral.md).

## Topics

### Identifying a Peer
- [var identifier: UUID](cbpeer/identifier.md)
  The UUID associated with the peer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CBCentral](cbcentral.md)
- [CBPeripheral](cbperipheral.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBManager](cbmanager.md)
  The abstract base class that manages central and peripheral objects.
- [class CBATTRequest](cbattrequest.md)
  A request that uses the Attribute Protocol (ATT).
- [class CBUUID](cbuuid.md)
  A universally unique identifier, as defined by Bluetooth standards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbpeer)*