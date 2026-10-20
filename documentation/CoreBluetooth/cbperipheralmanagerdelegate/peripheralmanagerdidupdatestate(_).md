# peripheralManagerDidUpdateState(_:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Required**: Yes

Tells the delegate the peripheral manager’s state updated.

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
func peripheralManagerDidUpdateState(_ peripheral: CBPeripheralManager)
```

#### Discussion

You implement this required method to ensure that Bluetooth low energy is available to use on the local peripheral device.

Issue commands to the peripheral manager only when the peripheral manager is in the powered-on state, as indicated by the [`CBPeripheralManagerState.poweredOn`](cbperipheralmanagerstate/poweredon.md) constant. A state with a value lower than [`CBPeripheralManagerState.poweredOn`](cbperipheralmanagerstate/poweredon.md) implies that advertising has stopped and that any connected centrals have been disconnected. If the state moves below [`CBPeripheralManagerState.poweredOff`](cbperipheralmanagerstate/poweredoff.md), advertising has stopped you must explicitly restart it. In addition, the powered off state clears the local database; in this case you must explicitly re-add all services. For a complete list and discussion of the possible values representing the state of the peripheral manager, see the [`CBPeripheralManagerState`](cbperipheralmanagerstate.md) enumeration in [`CBPeripheralManager`](cbperipheralmanager.md).

For more information, see [`Core Bluetooth Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/CoreBluetooth_concepts/AboutCoreBluetooth/Introduction.html#//apple_ref/doc/uid/TP40013257).

## Parameters

- `peripheral`: The peripheral manager whose state has changed.

## See Also

- [func peripheralManager(CBPeripheralManager, willRestoreState: [String : Any])](cbperipheralmanagerdelegate/peripheralmanager(_:willrestorestate:).md)
  Tells the delegate the system is about to restore the peripheral manager.
- [Peripheral Manager State Restoration Options](peripheral-manager-state-restoration-options.md)
  Keys used to specify options when restoring the state of a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate(_:))*