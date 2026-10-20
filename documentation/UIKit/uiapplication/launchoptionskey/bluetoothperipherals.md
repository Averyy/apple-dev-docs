# bluetoothPeripherals

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key indicating that the app should continue actions associated with its Bluetooth peripheral objects.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Store restoration identifiers and reinstantiate peripheral managers with those identifiers on app launch to resume previous functionality.

## Declaration

```swift
static let bluetoothPeripherals: UIApplication.LaunchOptionsKey
```

```c
extern UIApplicationLaunchOptionsKey const UIApplicationLaunchOptionsBluetoothPeripheralsKey;
```

#### Discussion

The presence of this key indicates that the app previously had one or more [`CBPeripheralManager`](../../../CoreBluetooth/cbperipheralmanager.md) objects and was relaunched by the Bluetooth system to continue actions associated with those objects. The value of this key is an [`NSArray`](../../../Foundation/nsarray.md) object containing one or more [`NSString`](../../../Foundation/nsstring.md) objects.

Each string in the array represents the restoration identifier for a peripheral manager object. This is the same string you assigned to the [`CBPeripheralManagerOptionRestoreIdentifierKey`](../../../CoreBluetooth/cbperipheralmanageroptionrestoreidentifierkey.md) key when you initialized the peripheral manager object previously. The system provides the restoration identifiers only for peripheral managers that had published or advertised services.

## See Also

### Deprecated constants
- [static let bluetoothCentrals: UIApplication.LaunchOptionsKey](./bluetoothcentrals.md)
  A key indicating that the app was relaunched to handle Bluetooth-related events.
- [static let cloudKitShareMetadata: UIApplication.LaunchOptionsKey](./cloudkitsharemetadata.md)
  A key indicating that the app received a CloudKit share invitation.
- [static let eventAttribution: UIApplication.LaunchOptionsKey](./eventattribution.md)
  UserInfo contains a [`UIEventAttribution`](../../uieventattribution.md) to go along with a URL open on launch
- [static let location: UIApplication.LaunchOptionsKey](./location.md)
  A key indicating that the app was launched to handle an incoming location event.
- [static let newsstandDownloads: UIApplication.LaunchOptionsKey](./newsstanddownloads.md)
  A key indicating that the app was launched to process newly downloaded Newsstand assets.
- [static let remoteNotification: UIApplication.LaunchOptionsKey](./remotenotification.md)
  A key indicating that a remote notification is available for the app to process.
- [static let shortcutItem: UIApplication.LaunchOptionsKey](./shortcutitem.md)
  A key indicating that the app was launched in response to the user selecting a Home screen quick action.
- [static let sourceApplication: UIApplication.LaunchOptionsKey](./sourceapplication.md)
  A key indicating that another app requested the launch of your app.
- [static let url: UIApplication.LaunchOptionsKey](./url.md)
  A key indicating that the app was launched so that it could open the specified URL.
- [static let userActivityDictionary: UIApplication.LaunchOptionsKey](./useractivitydictionary.md)
  A key indicating a dictionary associated with an activity that the user wants to continue.
- [static let userActivityType: UIApplication.LaunchOptionsKey](./useractivitytype.md)
  A key indicating the type of user activity that the user wants to continue.
- [static let annotation: UIApplication.LaunchOptionsKey](./annotation.md)
  A key indicating that the URL passed to your app contained custom annotation data from the source app.
- [static let localNotification: UIApplication.LaunchOptionsKey](./localnotification.md)
  A key indicating that the app was launched to handle a local notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/bluetoothperipherals)*