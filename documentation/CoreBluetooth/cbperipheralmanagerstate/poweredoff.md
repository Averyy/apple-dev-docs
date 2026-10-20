# CBPeripheralManagerState.poweredOff

**Framework**: Core Bluetooth  
**Kind**: case  
**Role**: Case

A manager state that indicates Bluetooth is currently powered off.

**Availability**:
- iOS 6.0+ - Deprecated in 10.0
- iPadOS 6.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

> **Deprecated**: Use CBManagerState instead

## Declaration

```swift
case poweredOff
```

```c
CBPeripheralManagerStatePoweredOff
```

## See Also

### Constants
- [CBPeripheralManagerState.unknown](./unknown.md)
  A manager state that indicates the current state of the peripheral manager is unknown.
- [CBPeripheralManagerState.resetting](./resetting.md)
  A manager state that indicates the connection with the system service was momentarily lost.
- [CBPeripheralManagerState.unsupported](./unsupported.md)
  A manager state that indicates the platform doesn’t support the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.unauthorized](./unauthorized.md)
  A manager state that indicates the app isn’t authorized to use the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.poweredOn](./poweredon.md)
  A manager state that indicates Bluetooth is currently powered on and is available to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/poweredoff)*