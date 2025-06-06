# userActivityDictionary

**Framework**: UIKit  
**Kind**: property

A key indicating a dictionary associated with an activity that the user wants to continue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let userActivityDictionary: UIApplication.LaunchOptionsKey
```

#### Discussion

The value of this key is an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object containing the key [`userActivityType`](uiapplication/launchoptionskey/useractivitytype.md), whose value is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object identifying the activity type.

## See Also

- [class NSUserActivity](../Foundation/NSUserActivity.md)
  A representation of the state of your app at a moment in time.
- [static let bluetoothCentrals: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/bluetoothcentrals.md)
  A key indicating that the app was relaunched to handle Bluetooth-related events.
- [static let bluetoothPeripherals: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/bluetoothperipherals.md)
  A key indicating that the app should continue actions associated with its Bluetooth peripheral objects.
- [static let cloudKitShareMetadata: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/cloudkitsharemetadata.md)
  A key indicating that the app received a CloudKit share invitation.
- [static let eventAttribution: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/eventattribution.md)
- [static let location: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/location.md)
  A key indicating that the app was launched to handle an incoming location event.
- [static let newsstandDownloads: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/newsstanddownloads.md)
  A key indicating that the app was launched to process newly downloaded Newsstand assets.
- [static let remoteNotification: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/remotenotification.md)
  A key indicating that a remote notification is available for the app to process.
- [static let shortcutItem: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/shortcutitem.md)
  A key indicating that the app was launched in response to the user selecting a Home screen quick action.
- [static let sourceApplication: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/sourceapplication.md)
  A key indicating that another app requested the launch of your app.
- [static let url: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/url.md)
  A key indicating that the app was launched so that it could open the specified URL.
- [static let userActivityType: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/useractivitytype.md)
  A key indicating the type of user activity that the user wants to continue.
- [static let annotation: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/annotation.md)
  A key indicating that the URL passed to your app contained custom annotation data from the source app.
- [static let localNotification: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/localnotification.md)
  A key indicating that the app was launched to handle a local notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/useractivitydictionary)*