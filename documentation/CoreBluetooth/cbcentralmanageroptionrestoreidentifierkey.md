# CBCentralManagerOptionRestoreIdentifierKey

**Framework**: Core Bluetooth  
**Kind**: var  
**Role**: Global Variable

A string containing a unique identifier (UID) for the central manager to instantiate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let CBCentralManagerOptionRestoreIdentifierKey: String
```

```c
extern NSString * const CBCentralManagerOptionRestoreIdentifierKey;
```

#### Discussion

The value for this key is an [`NSString`](../Foundation/nsstring.md). The system uses this UID to identify a specific [`CBCentralManager`](./cbcentralmanager.md), so the UID must be identical across executions of the app.

In scene-based apps that adopt [`UISceneDelegate`](../UIKit/uiscenedelegate.md), `launchOptions` is always `nil` on launch, so `UIApplicationLaunchOptionsBluetoothCentralsKey` is not available to deliver identifiers. Persist the UID yourself (for example, in [`UserDefaults`](../Foundation/userdefaults.md)) and pass it to [`init(delegate:queue:options:)`](./cbcentralmanager/init%28delegate,queue,options%29.md) on every launch.

Providing this key causes Core Bluetooth to call [`centralManager(_:willRestoreState:)`](./cbcentralmanagerdelegate/centralmanager%28_,willrestorestate%29.md) with the preserved state when restoration is available. For a description of the state dictionary keys your delegate receives, see [Central Manager State Restoration Options](./central-manager-state-restoration-options.md).

## See Also

### Constants
- [let CBCentralManagerOptionShowPowerAlertKey: String](./cbcentralmanageroptionshowpoweralertkey.md)
  A Boolean value that specifies whether the system warns the user if the app instantiates the central manager when Bluetooth service isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanageroptionrestoreidentifierkey)*