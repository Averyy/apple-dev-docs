# CBManagerState.unknown

**Framework**: Core Bluetooth  
**Kind**: case

The manager’s state is unknown.

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
case unknown
```

#### Discussion

This is a temporary state. After Core Bluetooth initializes or resets, it updates the state value.

## See Also

- [CBManagerState.poweredOff](cbmanagerstate/poweredoff.md)
  A state that indicates Bluetooth is currently powered off.
- [CBManagerState.poweredOn](cbmanagerstate/poweredon.md)
  A state that indicates Bluetooth is currently powered on and available to use.
- [CBManagerState.resetting](cbmanagerstate/resetting.md)
  A state that indicates the connection with the system service was momentarily lost.
- [CBManagerState.unauthorized](cbmanagerstate/unauthorized.md)
  A state that indicates the application isn’t authorized to use the Bluetooth low energy role.
- [CBManagerState.unsupported](cbmanagerstate/unsupported.md)
  A state that indicates this device doesn’t support the Bluetooth low energy central or client role.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanagerstate/unknown)*