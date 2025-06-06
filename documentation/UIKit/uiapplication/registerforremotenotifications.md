# registerForRemoteNotifications()

**Framework**: UIKit  
**Kind**: method

Registers to receive remote notifications through Apple Push Notification service.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func registerForRemoteNotifications()
```

#### Discussion

Call this method to initiate the registration process with Apple Push Notification service. If registration succeeds, the app calls your app delegate object’s  [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md) method and passes it a device token. You should pass this token along to the server you use to generate remote notifications for the device. If registration fails, the app calls its app delegate’s [`application(_:didFailToRegisterForRemoteNotificationsWithError:)`](uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md) method instead.

If you want your app’s remote notifications to display alerts, play sounds, or perform other user-facing actions, you must request authorization to do so using the [`requestAuthorization(options:completionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter/requestAuthorization(options:completionHandler:)) method of [`UNUserNotificationCenter`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter). If you do not request and receive authorization for your app’s interactions, the system delivers all remote notifications to your app silently.

## See Also

- [func unregisterForRemoteNotifications()](uiapplication/unregisterforremotenotifications.md)
  Unregisters for all remote notifications received through Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](uiapplication/isregisteredforremotenotifications.md)
  A Boolean value that indicates whether the app is currently registered for remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/registerforremotenotifications())*