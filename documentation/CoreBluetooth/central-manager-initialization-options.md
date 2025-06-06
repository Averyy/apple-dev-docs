# Central Manager Initialization Options

**Framework**: Core Bluetooth

Keys used to pass options when initializing a central manager.

## Topics

### Constants
- [let CBCentralManagerOptionShowPowerAlertKey: String](cbcentralmanageroptionshowpoweralertkey.md)
  A Boolean value that specifies whether the system warns the user if the app instantiates the central manager when Bluetooth service isn’t available.
- [let CBCentralManagerOptionRestoreIdentifierKey: String](cbcentralmanageroptionrestoreidentifierkey.md)
  A string containing a unique identifier (UID) for the central manager to instantiate.

## See Also

- [convenience init()](cbcentralmanager/init.md)
  Initializes the central manager without a delegate.
- [convenience init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?)](cbcentralmanager/init(delegate:queue:).md)
  Initializes the central manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](cbcentralmanager/init(delegate:queue:options:).md)
  Initializes the central manager with specified delegate, dispatch queue, and initialization options.
- [Central Manager State Restoration Options](central-manager-state-restoration-options.md)
  Keys used to pass state restoration options to the central manager initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/central-manager-initialization-options)*