# CBCentralManagerState

**Framework**: Core Bluetooth  
**Kind**: enum  
**Role**: Enumeration

Values that represent the current state of a central manager object.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use [`CBManagerState`](./cbmanagerstate.md) instead.

## Declaration

```swift
enum CBCentralManagerState
```

```c
enum CBCentralManagerState : NSInteger;
```

## Topics

### Constants
- [CBCentralManagerState.poweredOff](./cbcentralmanagerstate/poweredoff.md)
  A state that indicates Bluetooth is currently powered off.
- [CBCentralManagerState.poweredOn](./cbcentralmanagerstate/poweredon.md)
  A state that indicates Bluetooth is currently powered on and available to use.
- [CBCentralManagerState.resetting](./cbcentralmanagerstate/resetting.md)
  A state that indicates the connection with the system service was momentarily lost.
- [CBCentralManagerState.unauthorized](./cbcentralmanagerstate/unauthorized.md)
  A state that indicates the application isn’t authorized to use the Bluetooth low energy role.
- [CBCentralManagerState.unknown](./cbcentralmanagerstate/unknown.md)
  The manager’s state is unknown.
- [CBCentralManagerState.unsupported](./cbcentralmanagerstate/unsupported.md)
  A state that indicates this device doesn’t support the Bluetooth low energy central or client role.
### Initializers
- [init?(rawValue: Int)](./cbcentralmanagerstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [enum CBPeripheralManagerState](./cbperipheralmanagerstate.md)
  Values that represent the current state of the peripheral manager.
- [Deprecated Constants](./deprecated-constants.md)
  This document describes the constants found in the Core Bluetooth framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)*