# CBPeripheralManagerOptionRestoreIdentifierKey

**Framework**: Core Bluetooth  
**Kind**: var

A string containing a unique identifier (UID) for the peripheral manager to instantiate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBPeripheralManagerOptionRestoreIdentifierKey: String
```

#### Discussion

The value associated with this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString). The system uses this UID to identify a specific [`CBPeripheralManager`](cbperipheralmanager.md), so the UID must be identical across executions of the app. If your app creates multiple [`CBPeripheralManager`](cbperipheralmanager.md) instances, assign each a distinct UID to prevent state from being mixed up between them.

In scene-based apps that adopt [`UISceneDelegate`](https://developer.apple.com/documentation/UIKit/UISceneDelegate), `launchOptions` is always `nil` on launch, so `UIApplicationLaunchOptionsBluetoothPeripheralsKey` is not available to deliver identifiers. Persist the UID yourself (for example, in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults)) and pass it to [`init(delegate:queue:options:)`](cbperipheralmanager/init(delegate:queue:options:).md) on every launch.

Providing this key causes Core Bluetooth to call [`peripheralManager(_:willRestoreState:)`](cbperipheralmanagerdelegate/peripheralmanager(_:willrestorestate:).md) with the preserved state when restoration is available. For a description of the state dictionary keys your delegate receives, see [`Peripheral Manager State Restoration Options`](peripheral-manager-state-restoration-options.md).

## See Also

- [let CBPeripheralManagerOptionShowPowerAlertKey: String](cbperipheralmanageroptionshowpoweralertkey.md)
  A Boolean value specifying whether the system should warn if Bluetooth is in the powered-off state when instantiating the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanageroptionrestoreidentifierkey)*