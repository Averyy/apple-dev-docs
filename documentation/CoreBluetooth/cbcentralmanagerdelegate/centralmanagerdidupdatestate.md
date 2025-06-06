# centralManagerDidUpdateState(_:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Required**: Yes

Tells the delegate the central manager’s state updated.

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
func centralManagerDidUpdateState(_ central: CBCentralManager)
```

#### Discussion

You implement this required method to ensure that the central device supports Bluetooth low energy and that it’s available to use. You should issue commands to the central manager only when the central manager’s [`state`](cbmanager/state.md) indicates it’s powered on. A state with a value lower than [`CBManagerState.poweredOn`](cbmanagerstate/poweredon.md) implies that scanning has stopped, which in turn disconnects any previously-connected peripherals. If the state moves below [`CBManagerState.poweredOff`](cbmanagerstate/poweredoff.md), all [`CBPeripheral`](cbperipheral.md) objects obtained from this central manager become invalid; you must retrieve or discover these peripherals again. For a complete list of possible states, see [`CBManagerState`](cbmanagerstate.md).

## Parameters

- `central`: The central manager whose state has changed.

## See Also

- [func centralManager(CBCentralManager, willRestoreState: [String : Any])](cbcentralmanagerdelegate/centralmanager(_:willrestorestate:).md)
  Tells the delegate the system is about to restore the central manager, as part of relaunching the app into the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanagerdidupdatestate(_:))*