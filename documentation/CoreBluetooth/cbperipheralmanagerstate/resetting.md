# CBPeripheralManagerState.resetting

**Framework**: Core Bluetooth  
**Kind**: case

A manager state that indicates the connection with the system service was momentarily lost.

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
case resetting
```

#### Discussion

When the manager is in this state, an update is imminent.

## See Also

- [CBPeripheralManagerState.unknown](cbperipheralmanagerstate/unknown.md)
  A manager state that indicates the current state of the peripheral manager is unknown.
- [CBPeripheralManagerState.unsupported](cbperipheralmanagerstate/unsupported.md)
  A manager state that indicates the platform doesn’t support the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.unauthorized](cbperipheralmanagerstate/unauthorized.md)
  A manager state that indicates the app isn’t authorized to use the Bluetooth low energy peripheral/server role.
- [CBPeripheralManagerState.poweredOff](cbperipheralmanagerstate/poweredoff.md)
  A manager state that indicates Bluetooth is currently powered off.
- [CBPeripheralManagerState.poweredOn](cbperipheralmanagerstate/poweredon.md)
  A manager state that indicates Bluetooth is currently powered on and is available to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate/resetting)*