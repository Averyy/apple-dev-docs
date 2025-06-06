# Peripheral Manager State Restoration Options

**Framework**: Core Bluetooth

Keys used to specify options when restoring the state of a peripheral manager.

## Topics

### State Restoration Dictionary Keys
- [let CBPeripheralManagerRestoredStateServicesKey: String](cbperipheralmanagerrestoredstateserviceskey.md)
  An array of restored peripheral services.
- [let CBPeripheralManagerRestoredStateAdvertisementDataKey: String](cbperipheralmanagerrestoredstateadvertisementdatakey.md)
  A dictionary of restored advertising data.

## See Also

- [func peripheralManagerDidUpdateState(CBPeripheralManager)](cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate(_:).md)
  Tells the delegate the peripheral manager’s state updated.
- [func peripheralManager(CBPeripheralManager, willRestoreState: [String : Any])](cbperipheralmanagerdelegate/peripheralmanager(_:willrestorestate:).md)
  Tells the delegate the system is about to restore the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/peripheral-manager-state-restoration-options)*