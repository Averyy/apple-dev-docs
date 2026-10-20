# application(_:didFailToRegisterForRemoteNotificationsWithError:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app was unable to register for Apple Push Services.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, didFailToRegisterForRemoteNotificationsWithError error: any Error)
```

```objc
- (void) application:(NSApplication *) application didFailToRegisterForRemoteNotificationsWithError:(NSError *) error;
```

#### Discussion

The delegate receives this message after the [`registerForRemoteNotifications(matching:)`](../nsapplication/registerforremotenotifications%28matching%29.md) method of [`NSApplication`](../nsapplication.md) is invoked and there is an error in the registration process.

For more information about how to register with APNs, see [Registering your app with APNs](../../UserNotifications/registering-your-app-with-apns.md).

## Parameters

- `application`: The application that initiated the remote-notification registration process.
- `error`: An NSError object that encapsulates information why registration did not succeed. The application can display this information to the user.

## See Also

### Handling Push Notifications
- [func application(NSApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](./application%28_,didregisterforremotenotificationswithdevicetoken%29.md)
  Tells the delegate that the app registered for Apple Push Services.
- [func application(NSApplication, didReceiveRemoteNotification: [String : Any])](./application%28_,didreceiveremotenotification%29.md)
  Tells the delegate when the app receives a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:))*