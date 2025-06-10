# CBCentralManagerState

**Framework**: Core Bluetooth  
**Kind**: enum

Values that represent the current state of a central manager object.

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
enum CBCentralManagerState
```

## Topics

### Constants
- [CBCentralManagerState.poweredOff](cbcentralmanagerstate/poweredoff.md)
  A state that indicates Bluetooth is currently powered off.
- [CBCentralManagerState.poweredOn](cbcentralmanagerstate/poweredon.md)
  A state that indicates Bluetooth is currently powered on and available to use.
- [CBCentralManagerState.resetting](cbcentralmanagerstate/resetting.md)
  A state that indicates the connection with the system service was momentarily lost.
- [CBCentralManagerState.unauthorized](cbcentralmanagerstate/unauthorized.md)
  A state that indicates the application isn’t authorized to use the Bluetooth low energy role.
- [CBCentralManagerState.unknown](cbcentralmanagerstate/unknown.md)
  The manager’s state is unknown.
- [CBCentralManagerState.unsupported](cbcentralmanagerstate/unsupported.md)
  A state that indicates this device doesn’t support the Bluetooth low energy central or client role.
### Initializers
- [init?(rawValue: Int)](cbcentralmanagerstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CBPeripheralManagerState](cbperipheralmanagerstate.md)
  Values that represent the current state of the peripheral manager.
- [Deprecated Constants](deprecated-constants.md)
  This document describes the constants found in the Core Bluetooth framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate)*