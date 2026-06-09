# Central Manager State Restoration Options

**Framework**: Core Bluetooth

Restore central manager state in scene-based apps.

#### Overview

In scene-based apps that adopt [`UISceneDelegate`](https://developer.apple.com/documentation/UIKit/UISceneDelegate), the `launchOptions` dictionary is always `nil` on launch, and apps can no longer rely on the system to hand back central manager identifiers at launch.

Instead, generate a stable UID for each [`CBCentralManager`](cbcentralmanager.md), persist it (for example, in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults)) and pass it via [`CBCentralManagerOptionRestoreIdentifierKey`](cbcentralmanageroptionrestoreidentifierkey.md) when creating the manager on every launch. When restoration is available, Core Bluetooth calls [`centralManager(_:willRestoreState:)`](cbcentralmanagerdelegate/centralmanager(_:willrestorestate:).md) and passes the preserved state in the `dict` parameter.

```swift
func makeCentralManager(
    delegate: any CBCentralManagerDelegate
) -> CBCentralManager {
    let defaults = UserDefaults.standard
    let key = "MyCentralManagerUID"
    let uid: String
    if let saved = defaults.string(forKey: key) {
        uid = saved
    } else {
        uid = UUID().uuidString
        defaults.set(uid, forKey: key)
    }
    return CBCentralManager(
        delegate: delegate,
        queue: nil,
        options: [CBCentralManagerOptionRestoreIdentifierKey: uid]
    )
}
```

[`CBCentralManagerRestoredStatePeripheralsKey`](cbcentralmanagerrestoredstateperipheralskey.md) contains peripherals that were connected or had a pending connection when the app stopped. [`CBCentralManagerRestoredStateScanServicesKey`](cbcentralmanagerrestoredstatescanserviceskey.md) contains the service UUIDs your app was scanning for. [`CBCentralManagerRestoredStateScanOptionsKey`](cbcentralmanagerrestoredstatescanoptionskey.md) contains the scan options that were active. If your app also acts as a peripheral, see [`Peripheral Manager State Restoration Options`](peripheral-manager-state-restoration-options.md) for the equivalent pattern using [`CBPeripheralManagerOptionRestoreIdentifierKey`](cbperipheralmanageroptionrestoreidentifierkey.md).

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