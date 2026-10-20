# Central Manager Initialization Options

**Framework**: Core Bluetooth  
**Role**: API Collection

Keys used to pass options when initializing a central manager.

## Topics

### Constants
- [let CBCentralManagerOptionShowPowerAlertKey: String](./cbcentralmanageroptionshowpoweralertkey.md)
  A Boolean value that specifies whether the system warns the user if the app instantiates the central manager when Bluetooth service isn’t available.
- [let CBCentralManagerOptionRestoreIdentifierKey: String](./cbcentralmanageroptionrestoreidentifierkey.md)
  A string containing a unique identifier (UID) for the central manager to instantiate.

## See Also

### Initializing a Central Manager
- [convenience init()](./cbcentralmanager/init%28%29.md)
  Initializes the central manager without a delegate.
- [convenience init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?)](./cbcentralmanager/init%28delegate,queue%29.md)
  Initializes the central manager with a specified delegate and dispatch queue.
- [init(delegate: (any CBCentralManagerDelegate)?, queue: dispatch_queue_t?, options: [String : Any]?)](./cbcentralmanager/init%28delegate,queue,options%29.md)
  Initializes the central manager with specified delegate, dispatch queue, and initialization options.
- [Central Manager State Restoration Options](./central-manager-state-restoration-options.md)
  Restore central manager state in scene-based apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/central-manager-initialization-options)*