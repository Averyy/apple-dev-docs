# registerForRemoteNotifications(matching:)

**Framework**: AppKit  
**Kind**: method

Register to receive notifications of the specified types from a provider through the Apple Push Notification service.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func registerForRemoteNotifications(matching types: NSApplication.RemoteNotificationType)
```

#### Discussion

> **Note**: Use [`registerForRemoteNotifications()`](nsapplication/registerforremotenotifications().md) instead.

When you send this message, the device initiates the registration process with Apple Push Notification Service. If it succeeds, the app delegate receives a device token in the [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](nsapplicationdelegate/application(_:didregisterforremotenotificationswithdevicetoken:).md) method; if registration doesn’t succeed, the delegate is informed via the [`application(_:didFailToRegisterForRemoteNotificationsWithError:)`](nsapplicationdelegate/application(_:didfailtoregisterforremotenotificationswitherror:).md) method. If the app delegate receives a device token, it should connect with its provider and pass it the token.

> **Note**:  Currently the only notification type supported in macOS for non-running apps is icon badging. However, the JSON payload, which may contain information related to sounds and alerts, is passed to a running app in [`application(_:didReceiveRemoteNotification:)`](nsapplicationdelegate/application(_:didreceiveremotenotification:).md). The app can do whatever it wants to with that information (for example, display an alert or play a sound).

## Parameters

- `types`: A bit mask specifying the types of notifications the app accepts. See   for valid bit-mask values.

## See Also

- [func registerForRemoteNotifications()](nsapplication/registerforremotenotifications.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](nsapplication/unregisterforremotenotifications.md)
  Unregister for notifications received from Apple Push Notification service.
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](nsapplication/enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [var isRegisteredForRemoteNotifications: Bool](nsapplication/isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](nsapplication/remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/registerforremotenotifications(matching:))*