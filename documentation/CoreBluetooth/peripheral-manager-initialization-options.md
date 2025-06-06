# Peripheral Manager Initialization Options

**Framework**: Core Bluetooth

Keys used to specify options when creating a peripheral manager.

## Topics

### Initialization Options
- [let CBPeripheralManagerOptionShowPowerAlertKey: String](cbperipheralmanageroptionshowpoweralertkey.md)
  A Boolean value specifying whether the system should warn if Bluetooth is in the powered-off state when instantiating the peripheral manager.
- [let CBPeripheralManagerOptionRestoreIdentifierKey: String](cbperipheralmanageroptionrestoreidentifierkey.md)
  A unique identifier (UID) with which to instantiate the peripheral manager.

## See Also

- [convenience init()](cbperipheralmanager/init.md)
  Initializes the peripheral manager without a delegate.
- [convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)](cbperipheralmanager/init(delegate:queue:).md)
  Initializes the peripheral manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbperipheralmanager/init(delegate:queue:options:).md)
  Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.
- [var delegate: (any CBPeripheralManagerDelegate)?](cbperipheralmanager/delegate.md)
  The delegate object specified to receive peripheral events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/peripheral-manager-initialization-options)*