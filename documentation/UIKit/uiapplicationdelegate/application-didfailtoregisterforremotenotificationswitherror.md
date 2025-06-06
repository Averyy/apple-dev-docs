# application(_:didFailToRegisterForRemoteNotificationsWithError:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: any Error)
```

#### Discussion

UIKit calls this method if it was unable to register your app with APNs or if your app is not properly configured for remote notifications. During development, make sure your app has the proper entitlements and that its App ID is configured to support push notifications. You might use your implementation of this method to make a note of the failed registration so that you can try again later.

For more information about how to set up and send remote notifications in your app, see [`Setting up a remote notification server`](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server).

## Parameters

- `application`: The app object that initiated the remote-notification registration process.
- `error`: An   object that encapsulates information why registration did not succeed. The app can choose to display this information to the user.

## See Also

- [func application(UIApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](uiapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any], fetchCompletionHandler: (UIBackgroundFetchResult) -> Void)](uiapplicationdelegate/application(_:didreceiveremotenotification:fetchcompletionhandler:).md)
  Tells the app that a remote notification arrived that indicates there is data to be fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:))*