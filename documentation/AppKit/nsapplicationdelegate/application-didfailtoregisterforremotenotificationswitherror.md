# application(_:didFailToRegisterForRemoteNotificationsWithError:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app was unable to register for Apple Push Services.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, didFailToRegisterForRemoteNotificationsWithError error: any Error)
```

#### Discussion

The delegate receives this message after the [`registerForRemoteNotifications(matching:)`](nsapplication/registerforremotenotifications(matching:).md) method of [`NSApplication`](nsapplication.md) is invoked and there is an error in the registration process.

For more information about how to implement push notifications in your application, see [`Local and Remote Notification Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## Parameters

- `application`: The application that initiated the remote-notification registration process.
- `error`: An NSError object that encapsulates information why registration did not succeed. The application can display this information to the user.

## See Also

- [func application(NSApplication, didRegisterForRemoteNotificationsWithDeviceToken: Data)](nsapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md)
  Tells the delegate that the app registered for Apple Push Services.
- [func application(NSApplication, didReceiveRemoteNotification: [String : Any])](nsapplicationdelegate/application(_:didreceiveremotenotification:).md)
  Tells the delegate when the app receives a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:))*