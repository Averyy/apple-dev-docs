# CBManagerState.unauthorized

**Framework**: Core Bluetooth  
**Kind**: case  
**Role**: Case

A state that indicates the application isn’t authorized to use the Bluetooth low energy role.

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
case unauthorized
```

```c
CBManagerStateUnauthorized
```

## See Also

### Manager States
- [CBManagerState.poweredOff](./poweredoff.md)
  A state that indicates Bluetooth is currently powered off.
- [CBManagerState.poweredOn](./poweredon.md)
  A state that indicates Bluetooth is currently powered on and available to use.
- [CBManagerState.resetting](./resetting.md)
  A state that indicates the connection with the system service was momentarily lost.
- [CBManagerState.unknown](./unknown.md)
  The manager’s state is unknown.
- [CBManagerState.unsupported](./unsupported.md)
  A state that indicates this device doesn’t support the Bluetooth low energy central or client role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/unauthorized)*