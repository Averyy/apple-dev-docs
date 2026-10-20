# registerForRemoteNotifications()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Register for notifications sent by Apple Push Notification service (APNs).

**Availability**:
- macOS 10.14+

## Declaration

```swift
func registerForRemoteNotifications()
```

```objc
- (void) registerForRemoteNotifications;
```

#### Discussion

Call this method to register your app with APNs. When a valid connection is established, APNs sends a device token to your app delegate. Forward that token to your company’s provider server.

For more information about how to register with APNs, see [Registering your app with APNs](../../UserNotifications/registering-your-app-with-apns.md).

## See Also

### Managing remote notifications
- [func unregisterForRemoteNotifications()](./unregisterforremotenotifications%28%29.md)
  Unregister for notifications received from Apple Push Notification service.
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](./enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [func registerForRemoteNotifications(matching: NSApplication.RemoteNotificationType)](./registerforremotenotifications%28matching%29.md)
  Register to receive notifications of the specified types from a provider through the Apple Push Notification service.
- [var isRegisteredForRemoteNotifications: Bool](./isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](./remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/registerforremotenotifications())*