# CBPeripheralManagerState

**Framework**: Core Bluetooth  
**Kind**: enum

Values that represent the current state of the peripheral manager.

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
enum CBPeripheralManagerState
```

## Topics

### Constants
- [CBPeripheralManagerState.unknown](cbperipheralmanagerstate/unknown.md)
  A manager state that indicates the current state of the peripheral manager is unknown.
- [CBPeripheralManagerState.resetting](cbperipheralmanagerstate/resetting.md)
  A manager state that indicates the connection with the system service was momentarily lost.
- [CBPeripheralManagerState.unsupported](cbperipheralmanagerstate/unsupported.md)
  A manager state that indicates the platform doesn’t support the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.unauthorized](cbperipheralmanagerstate/unauthorized.md)
  A manager state that indicates the app isn’t authorized to use the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.poweredOff](cbperipheralmanagerstate/poweredoff.md)
  A manager state that indicates Bluetooth is currently powered off.
- [CBPeripheralManagerState.poweredOn](cbperipheralmanagerstate/poweredon.md)
  A manager state that indicates Bluetooth is currently powered on and is available to use.
### Initializers
- [init?(rawValue: Int)](cbperipheralmanagerstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CBCentralManagerState](cbcentralmanagerstate.md)
  Values that represent the current state of a central manager object.
- [Deprecated Constants](deprecated-constants.md)
  This document describes the constants found in the Core Bluetooth framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate)*