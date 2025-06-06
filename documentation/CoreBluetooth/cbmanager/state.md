# state

**Framework**: Core Bluetooth  
**Kind**: property

The current state of the manager.

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
var state: CBManagerState { get }
```

#### Discussion

This state is initially set to [`CBManagerState.unknown`](cbmanagerstate/unknown.md). When the state updates, the manager calls its delegate’s [`centralManagerDidUpdateState(_:)`](cbcentralmanagerdelegate/centralmanagerdidupdatestate(_:).md) method.

## See Also

- [enum CBManagerState](cbmanagerstate.md)
  The possible states of a Core Bluetooth manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanager/state)*