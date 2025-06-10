# UIApplication.LaunchOptionsKey

**Framework**: UIKit  
**Kind**: struct

The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct LaunchOptionsKey
```

#### Overview

These keys are passed to the options dictionary that’s passed to the [`application(_:willFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md) and [`application(_:didFinishLaunchingWithOptions:)`](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md) methods of the app delegate.

## Topics

### Accessing launch options
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
- [static let userActivityDictionary: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/useractivitydictionary.md)
  A key indicating a dictionary associated with an activity that the user wants to continue.
- [static let userActivityType: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/useractivitytype.md)
  A key indicating the type of user activity that the user wants to continue.
- [static let annotation: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/annotation.md)
  A key indicating that the URL passed to your app contained custom annotation data from the source app.
- [static let localNotification: UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey/localnotification.md)
  A key indicating that the app was launched to handle a local notification.
### Creating a launch options key
- [init(rawValue: String)](uiapplication/launchoptionskey/init(rawvalue:).md)
  Creates a launch options key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process has begun.
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [class let didFinishLaunchingNotification: NSNotification.Name](uiapplication/didfinishlaunchingnotification.md)
  A notification that posts immediately after the app finishes launching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey)*