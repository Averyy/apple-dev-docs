# CBManagerState

**Framework**: Core Bluetooth  
**Kind**: enum

The possible states of a Core Bluetooth manager.

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
enum CBManagerState
```

## Topics

### Manager States
- [CBManagerState.poweredOff](cbmanagerstate/poweredoff.md)
  A state that indicates Bluetooth is currently powered off.
- [CBManagerState.poweredOn](cbmanagerstate/poweredon.md)
  A state that indicates Bluetooth is currently powered on and available to use.
- [CBManagerState.resetting](cbmanagerstate/resetting.md)
  A state that indicates the connection with the system service was momentarily lost.
- [CBManagerState.unauthorized](cbmanagerstate/unauthorized.md)
  A state that indicates the application isn’t authorized to use the Bluetooth low energy role.
- [CBManagerState.unknown](cbmanagerstate/unknown.md)
  The manager’s state is unknown.
- [CBManagerState.unsupported](cbmanagerstate/unsupported.md)
  A state that indicates this device doesn’t support the Bluetooth low energy central or client role.
### Initializers
- [init?(rawValue: Int)](cbmanagerstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: CBManagerState](cbmanager/state.md)
  The current state of the manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate)*