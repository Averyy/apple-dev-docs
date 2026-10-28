# application(_:didFailToRegisterForRemoteNotificationsWithError:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func application(_ application: UIApplication, didFailToRegisterForRemoteNotificationsWithError error: any Error)
```

```objc
- (void) application:(UIApplication *) application didFailToRegisterForRemoteNotificationsWithError:(NSError *) error;
```

## Discussion

UIKit calls this method if it was unable to register your app with APNs or if your app is not properly configured for remote notifications. During development, make sure your app has the proper entitlements and that its App ID is configured to support push notifications. You might use your implementation of this method to make a note of the failed registration so that you can try again later.

For more information about how to set up and send remote notifications in your app, see [Setting up a remote notification server](../../UserNotifications/setting-up-a-remote-notification-server.md).

## Parameters

- `application`: The app object that initiated the remote-notification registration process.
- `error`: An [`NSError`](../../Foundation/nserror.md) object that encapsulates information why registration did not succeed. The app can choose to display this information to the user.

## See Also

### Handling remote notification registration
- [func application(UIApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](./application%28_,didregisterforremotenotificationswithdevicetoken%29.md)
  Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [func application(UIApplication, didReceiveRemoteNotification: [AnyHashable : Any], fetchCompletionHandler: (UIBackgroundFetchResult) -> Void)](./application%28_,didreceiveremotenotification,fetchcompletionhandler%29.md)
  Tells the app that a remote notification arrived that indicates there is data to be fetched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:))*