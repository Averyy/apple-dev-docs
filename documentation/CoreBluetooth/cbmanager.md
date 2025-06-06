# CBManager

**Framework**: Core Bluetooth  
**Kind**: class

The abstract base class that manages central and peripheral objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CBManager
```

## Topics

### Accessing the Manager’s Properties
- [var state: CBManagerState](cbmanager/state.md)
  The current state of the manager.
- [enum CBManagerState](cbmanagerstate.md)
  The possible states of a Core Bluetooth manager.
### Determining Authorization State
- [class var authorization: CBManagerAuthorization](cbmanager/authorization-swift.type.property.md)
  The current authorization status for using Bluetooth.
- [enum CBManagerAuthorization](cbmanagerauthorization.md)
  The current authorization state of a Core Bluetooth manager.
### Deprecated Properties
- [var authorization: CBManagerAuthorization](cbmanager/authorization-swift.property.md)
  The current authorization status for using Bluetooth.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CBCentralManager](cbcentralmanager.md)
- [CBPeripheralManager](cbperipheralmanager.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CBATTRequest](cbattrequest.md)
  A request that uses the Attribute Protocol (ATT).
- [class CBPeer](cbpeer.md)
  An object that represents a remote device.
- [class CBUUID](cbuuid.md)
  A universally unique identifier, as defined by Bluetooth standards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanager)*