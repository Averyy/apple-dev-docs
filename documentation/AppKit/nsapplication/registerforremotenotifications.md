# registerForRemoteNotifications()

**Framework**: AppKit  
**Kind**: method

Register for notifications sent by Apple Push Notification service (APNs).

**Availability**:
- macOS 10.14+

## Declaration

```swift
@MainActor
func registerForRemoteNotifications()
```

#### Discussion

Call this method to register your app with APNs. When a valid connection is established, APNs sends a device token to your app delegate. Forward that token to your company’s provider server.

For more information about how to register with APNs, see [`Registering your app with APNs`](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns).

## See Also

- [func unregisterForRemoteNotifications()](nsapplication/unregisterforremotenotifications.md)
  Unregister for notifications received from Apple Push Notification service.
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](nsapplication/enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](nsapplication/registerforremotenotifications(matching:).md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](nsapplication/isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/registerforremotenotifications())*