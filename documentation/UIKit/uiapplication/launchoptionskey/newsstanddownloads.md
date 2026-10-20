# newsstandDownloads

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key indicating that the app was launched to process newly downloaded Newsstand assets.

**Availability**:
- iOS 5.0+ - Deprecated in 26.0
- iPadOS 5.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: This dictionary key is no longer used.

## Declaration

```swift
static let newsstandDownloads: UIApplication.LaunchOptionsKey
```

```c
extern UIApplicationLaunchOptionsKey const UIApplicationLaunchOptionsNewsstandDownloadsKey;
```

#### Discussion

The value of this key is an array of string identifiers that identify the `NKAssetDownload` objects corresponding to the assets. Although you can use the identifiers for cross-checking purposes, you should obtain the definitive array of `NKAssetDownload` objects (representing asset downloads in progress or in error) through the `downloadingAssets` property of the `NKLibrary` object representing the Newsstand app’s library.

## See Also

### Deprecated constants
- [static let bluetoothCentrals: UIApplication.LaunchOptionsKey](./bluetoothcentrals.md)
  A key indicating that the app was relaunched to handle Bluetooth-related events.
- [static let bluetoothPeripherals: UIApplication.LaunchOptionsKey](./bluetoothperipherals.md)
  A key indicating that the app should continue actions associated with its Bluetooth peripheral objects.
- [static let cloudKitShareMetadata: UIApplication.LaunchOptionsKey](./cloudkitsharemetadata.md)
  A key indicating that the app received a CloudKit share invitation.
- [static let eventAttribution: UIApplication.LaunchOptionsKey](./eventattribution.md)
  UserInfo contains a [`UIEventAttribution`](../../uieventattribution.md) to go along with a URL open on launch
- [static let location: UIApplication.LaunchOptionsKey](./location.md)
  A key indicating that the app was launched to handle an incoming location event.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/newsstanddownloads)*