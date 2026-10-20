# Peripheral Manager State Restoration Options

**Framework**: Core Bluetooth  
**Role**: API Collection

Keys used to specify options when restoring the state of a peripheral manager.

## Topics

### State Restoration Dictionary Keys
- [let CBPeripheralManagerRestoredStateServicesKey: String](./cbperipheralmanagerrestoredstateserviceskey.md)
  An array of restored peripheral services.
- [let CBPeripheralManagerRestoredStateAdvertisementDataKey: String](./cbperipheralmanagerrestoredstateadvertisementdatakey.md)
  A dictionary of restored advertising data.

## See Also

### Monitoring Changes to the Peripheral Manager’s State
- [func peripheralManagerDidUpdateState(CBPeripheralManager)](./cbperipheralmanagerdelegate/peripheralmanagerdidupdatestate%28_%29.md)
  Tells the delegate the peripheral manager’s state updated.
- [func peripheralManager(CBPeripheralManager, willRestoreState: [String : Any])](./cbperipheralmanagerdelegate/peripheralmanager%28_,willrestorestate%29.md)
  Tells the delegate the system is about to restore the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/peripheral-manager-state-restoration-options)*