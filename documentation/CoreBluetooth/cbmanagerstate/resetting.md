# CBManagerState.resetting

**Framework**: Core Bluetooth  
**Kind**: case  
**Role**: Case

A state that indicates the connection with the system service was momentarily lost.

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
case resetting
```

```c
CBManagerStateResetting
```

#### Discussion

This state indicates that Bluetooth is trying to reconnect. After it reconnects, Core Bluetooth updates the state value.

## See Also

### Manager States
- [CBManagerState.poweredOff](./poweredoff.md)
  A state that indicates Bluetooth is currently powered off.
- [CBManagerState.poweredOn](./poweredon.md)
  A state that indicates Bluetooth is currently powered on and available to use.
- [CBManagerState.unauthorized](./unauthorized.md)
  A state that indicates the application isn’t authorized to use the Bluetooth low energy role.
- [CBManagerState.unknown](./unknown.md)
  The manager’s state is unknown.
- [CBManagerState.unsupported](./unsupported.md)
  A state that indicates this device doesn’t support the Bluetooth low energy central or client role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/resetting)*