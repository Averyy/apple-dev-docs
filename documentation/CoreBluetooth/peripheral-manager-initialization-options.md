# Peripheral Manager Initialization Options

**Framework**: Core Bluetooth  
**Role**: API Collection

Keys used to specify options when creating a peripheral manager.

## Topics

### Initialization Options
- [let CBPeripheralManagerOptionShowPowerAlertKey: String](./cbperipheralmanageroptionshowpoweralertkey.md)
  A Boolean value specifying whether the system should warn if Bluetooth is in the powered-off state when instantiating the peripheral manager.
- [let CBPeripheralManagerOptionRestoreIdentifierKey: String](./cbperipheralmanageroptionrestoreidentifierkey.md)
  A string containing a unique identifier (UID) for the peripheral manager to instantiate.

## See Also

### Initializing a Peripheral Manager
- [convenience init()](./cbperipheralmanager/init%28%29.md)
  Initializes the peripheral manager without a delegate.
- [convenience init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?)](./cbperipheralmanager/init%28delegate,queue%29.md)
  Initializes the peripheral manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBPeripheralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](./cbperipheralmanager/init%28delegate,queue,options%29.md)
  Initializes the peripheral manager with a specified delegate, dispatch queue, and initialization options.
- [var delegate: (any CBPeripheralManagerDelegate)?](./cbperipheralmanager/delegate.md)
  The delegate object specified to receive peripheral events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/peripheral-manager-initialization-options)*