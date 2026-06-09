# peripheralManager(_:willRestoreState:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate the system is about to restore the peripheral manager.

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
optional func peripheralManager(_ peripheral: CBPeripheralManager, willRestoreState dict: [String : Any])
```

#### Discussion

This method only applies to your app if it opts in to state restoration by providing [`CBPeripheralManagerOptionRestoreIdentifierKey`](cbperipheralmanageroptionrestoreidentifierkey.md) when initializing a [`CBPeripheralManager`](cbperipheralmanager.md). The system invokes this method when relaunching your app to handle active advertising or peripheral operations in progress when your app stopped.

If the system calls this method but the parameters are missing, your app is responsible for restoring its previous state. Initialize any services and characteristics your app requires, and resume any activities from where they stopped.

## Parameters

- `peripheral`: The peripheral manager undergoing state restoration.
- `dict`: A dictionary containing information about the peripheral manager that the system preserved when your app stopped. For the available keys to this dictionary, see [`Peripheral Manager State Restoration Options`](peripheral-manager-state-restoration-options.md).

## See Also

- [func peripheralManagerDidUpdateState(CBPeripheralManager)](cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate(_:).md)
  Tells the delegate the peripheral manager’s state updated.
- [Peripheral Manager State Restoration Options](peripheral-manager-state-restoration-options.md)
  Keys used to specify options when restoring the state of a peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate/peripheralmanager(_:willrestorestate:))*