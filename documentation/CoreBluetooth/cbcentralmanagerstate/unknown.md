# CBCentralManagerState.unknown

**Framework**: Core Bluetooth  
**Kind**: case  
**Role**: Case

The manager’s state is unknown.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use CBManagerState instead

## Declaration

```swift
case unknown
```

```c
CBCentralManagerStateUnknown
```

## Discussion

This is a temporary state. Once Core Bluetooth initializes or resets, it updates the state value.

## See Also

### Constants
- [CBCentralManagerState.poweredOff](./poweredoff.md)
  A state that indicates Bluetooth is currently powered off.
- [CBCentralManagerState.poweredOn](./poweredon.md)
  A state that indicates Bluetooth is currently powered on and available to use.
- [CBCentralManagerState.resetting](./resetting.md)
  A state that indicates the connection with the system service was momentarily lost.
- [CBCentralManagerState.unauthorized](./unauthorized.md)
  A state that indicates the application isn’t authorized to use the Bluetooth low energy role.
- [CBCentralManagerState.unsupported](./unsupported.md)
  A state that indicates this device doesn’t support the Bluetooth low energy central or client role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate/unknown)*