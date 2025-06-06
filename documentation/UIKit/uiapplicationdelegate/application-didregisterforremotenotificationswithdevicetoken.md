# application(_:didRegisterForRemoteNotificationsWithDeviceToken:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data)
```

#### Discussion

UIKit calls this method after it successfully registers your app with APNs.  In your implementation of this method, send the contents of the `deviceToken` parameter to the server that you use to generate remote notifications. Never cache the device token locally on the user’s device. Device tokens can change periodically, so caching the value risks sending an invalid token to your server. If the device token hasn’t changed, registering with APNs and returning the token happens quickly.

Typically, this method is called only after you call the [`registerForRemoteNotifications()`](uiapplication/registerforremotenotifications().md) method of [`UIApplication`](uiapplication.md), but UIKit might call it in other rare circumstances. For example, UIKit calls the method when the user launches an app after having restored a device from data that is not the device’s backup data. In this exceptional case, the app won’t know the new device’s token until the user launches it.

## Parameters

- `application`: The app object that initiated the remote-notification registration process.
- `deviceToken`: APNs device tokens are of variable length. Do not hard-code their size.

## See Also

- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any])](uiapplicationdelegate/application(_:didreceiveremotenotification:).md)
  Called when your app has received a remote notification.
- [func registerForRemoteNotifications()](uiapplication/registerforremotenotifications.md)
  Registers to receive remote notifications through Apple Push Notification service.
- [func application(UIApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md)
  Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any], fetchCompletionHandler: (UIBackgroundFetchResult) -> Void)](uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:).md)
  Tells the app that a remote notification arrived that indicates there is data to be fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:))*