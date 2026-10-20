# CBPeripheralManagerState

**Framework**: Core Bluetooth  
**Kind**: enum  
**Role**: Enumeration

Values that represent the current state of the peripheral manager.

**Availability**:
- iOS 6.0+ - Deprecated in 10.0
- iPadOS 6.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use [`CBManagerState`](./cbmanagerstate.md) instead.

## Declaration

```swift
enum CBPeripheralManagerState
```

```c
enum CBPeripheralManagerState : NSInteger;
```

## Topics

### Constants
- [CBPeripheralManagerState.unknown](./cbperipheralmanagerstate/unknown.md)
  A manager state that indicates the current state of the peripheral manager is unknown.
- [CBPeripheralManagerState.resetting](./cbperipheralmanagerstate/resetting.md)
  A manager state that indicates the connection with the system service was momentarily lost.
- [CBPeripheralManagerState.unsupported](./cbperipheralmanagerstate/unsupported.md)
  A manager state that indicates the platform doesn’t support the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.unauthorized](./cbperipheralmanagerstate/unauthorized.md)
  A manager state that indicates the app isn’t authorized to use the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.poweredOff](./cbperipheralmanagerstate/poweredoff.md)
  A manager state that indicates Bluetooth is currently powered off.
- [CBPeripheralManagerState.poweredOn](./cbperipheralmanagerstate/poweredon.md)
  A manager state that indicates Bluetooth is currently powered on and is available to use.
### Initializers
- [init?(rawValue: Int)](./cbperipheralmanagerstate/init%28rawvalue%29.md)

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
- [enum CBCentralManagerState](./cbcentralmanagerstate.md)
  Values that represent the current state of a central manager object.
- [Deprecated Constants](./deprecated-constants.md)
  This document describes the constants found in the Core Bluetooth framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate)*