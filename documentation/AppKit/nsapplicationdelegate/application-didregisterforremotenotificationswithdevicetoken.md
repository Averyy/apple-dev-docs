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

For more information about how to register with APNs, see [`Registering your app with APNs`](https://developer.apple.com/documentation/usernotifications/registering-your-app-with-apns).

## Parameters

- `application`: The application that initiated the remote-notification registration process.
- `deviceToken`: A token that identifies the device to Apple Push Notification Service (APNS). The token is an opaque data type because that is the form that the provider needs to submit to the APNS servers when it sends a notification to a device. The APNS servers require a binary format for performance reasons. The size of a device token is 32 bytes.

## See Also

- [func application(NSApplication, didFailToRegisterForRemoteNotificationsWithError: any Error)](nsapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md)
  Tells the delegate that the app was unable to register for Apple Push Services.
- [func application(NSApplication, didReceiveRemoteNotification: [String : Any])](nsapplicationdelegate/application(_:didreceiveremotenotification:).md)
  Tells the delegate when the app receives a remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:))*