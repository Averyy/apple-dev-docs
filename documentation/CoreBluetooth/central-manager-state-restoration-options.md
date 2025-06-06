# Central Manager State Restoration Options

**Framework**: Core Bluetooth

Keys used to pass state restoration options to the central manager initializer.

## Topics

### State Restoration Options
- [let CBCentralManagerRestoredStatePeripheralsKey: String](cbcentralmanagerrestoredstateperipheralskey.md)
  An array of peripherals for use when restoring the state of a central manager.
- [let CBCentralManagerRestoredStateScanServicesKey: String](cbcentralmanagerrestoredstatescanserviceskey.md)
  An array of service IDs for use when restoring state.
- [let CBCentralManagerRestoredStateScanOptionsKey: String](cbcentralmanagerrestoredstatescanoptionskey.md)
  A dictionary of peripheral scan options for use when restoring state.

## See Also

- [convenience init()](cbcentralmanager/init.md)
  Initializes the central manager without a delegate.
- [convenience init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?)](cbcentralmanager/init(delegate:queue:).md)
  Initializes the central manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbcentralmanager/init(delegate:queue:options:).md)
  Initializes the central manager with specified delegate, dispatch queue, and initialization options.
- [Central Manager Initialization Options](central-manager-initialization-options.md)
  Keys used to pass options when initializing a central manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/central-manager-state-restoration-options)*