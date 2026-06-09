# centralManager(_:willRestoreState:)

**Framework**: Core Bluetooth  
**Kind**: method

Tells the delegate the system is about to restore the central manager.

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
optional func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : Any])
```

#### Discussion

This method only applies to your app if it opts in to state restoration by providing [`CBCentralManagerOptionRestoreIdentifierKey`](cbcentralmanageroptionrestoreidentifierkey.md) when initializing a [`CBCentralManager`](cbcentralmanager.md). The system invokes this method when relaunching your app to service active or pending connections and scans that were in progress when your app stopped.

If the system calls this method but the parameters are missing (for example, if your app stopped before establishing peripherals and services), your app is responsible for restoring its previous state. Initialize any peripherals and services your app requires, and resume any activities from where they stopped.

```swift
func centralManager(_ central: CBCentralManager, willRestoreState dict: [String : Any]) {
    if let peripherals = dict[CBCentralManagerRestoredStatePeripheralsKey] as? [CBPeripheral] {
        // Use the restored peripherals.
    } else {
        // Reconnect to known devices, for example from `UserDefaults`.
    }

    if let services = dict[CBCentralManagerRestoredStateScanServicesKey] as? [CBUUID] {
        // Resume scanning for the restored services.
    } else {
        // Start scanning with your default services.
        let heartRateService = CBUUID(string: "180D")
        central.scanForPeripherals(withServices: [heartRateService])
    }
}
```

## Parameters

- `central`: The central manager that provides this information.
- `dict`: A dictionary that contains information about the central manager that the system preserved when your app stopped. For the available keys, see [`Central Manager State Restoration Options`](central-manager-state-restoration-options.md).

## See Also

- [func centralManagerDidUpdateState(CBCentralManager)](cbcentralmanagerdelegate/centralmanagerdidupdatestate(_:).md)
  Tells the delegate the central manager’s state updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate/centralmanager(_:willrestorestate:))*