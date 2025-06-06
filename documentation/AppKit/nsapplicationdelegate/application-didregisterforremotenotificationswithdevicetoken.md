# application(_:didRegisterForRemoteNotificationsWithDeviceToken:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app registered for Apple Push Services.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data)
```

#### Discussion

The delegate receives this message after the [`registerForRemoteNotifications(matching:)`](nsapplication/registerforremotenotifications(matching:).md)method of [`NSApplication`](nsapplication.md) is invoked and there is no error in the registration process. After receiving the device token, the application should connect with its provider and give the token to it. APNS only pushes notifications to the application’s computer that are accompanied with this token.

For more information about how to implement push notifications in your application, see [`Local and Remote Notification Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## Parameters

- `application`: The application that initiated the remote-notification registration process.
- `deviceToken`: The size of a device token is 32 bytes.

## See Also

- [func application(NSApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](nsapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md)
  Tells the delegate that the app was unable to register for Apple Push Services.
- [func application(NSApplication, didReceiveRemoteNotification: [String : Any])](nsapplicationdelegate/application(_:didreceiveremotenotification:).md)
  Tells the delegate when the app receives a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:))*