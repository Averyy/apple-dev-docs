# registerForRemoteNotifications(matching:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Register to receive notifications of the specified types from a provider through the Apple Push Notification service.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func registerForRemoteNotifications(matching types: NSApplication.RemoteNotificationType)
```

```objc
- (void) registerForRemoteNotificationTypes:(NSRemoteNotificationType) types;
```

#### Discussion

> **Deprecated**: Use [`registerForRemoteNotifications()`](./registerforremotenotifications%28%29.md) instead.

When you send this message, the device initiates the registration process with Apple Push Notification Service. If it succeeds, the app delegate receives a device token in the [`application(_:didRegisterForRemoteNotificationsWithDeviceToken:)`](../nsapplicationdelegate/application%28_,didregisterforremotenotificationswithdevicetoken%29.md) method; if registration doesn’t succeed, the delegate is informed via the [`application(_:didFailToRegisterForRemoteNotificationsWithError:)`](../nsapplicationdelegate/application%28_,didfailtoregisterforremotenotificationswitherror%29.md) method. If the app delegate receives a device token, it should connect with its provider and pass it the token.

> **Note**:  Currently the only notification type supported in macOS for non-running apps is icon badging. However, the JSON payload, which may contain information related to sounds and alerts, is passed to a running app in [`application(_:didReceiveRemoteNotification:)`](../nsapplicationdelegate/application%28_,didreceiveremotenotification%29.md). The app can do whatever it wants to with that information (for example, display an alert or play a sound).

## Parameters

- `types`: A bit mask specifying the types of notifications the app accepts. See [`NSApplication.RemoteNotificationType`](./remotenotificationtype.md) for valid bit-mask values.

## See Also

### Managing remote notifications
- [func registerForRemoteNotifications()](./registerforremotenotifications%28%29.md)
  Register for notifications sent by Apple Push Notification service (APNs).
- [func unregisterForRemoteNotifications()](./unregisterforremotenotifications%28%29.md)
  Unregister for notifications received from Apple Push Notification service.
- [var enabledRemoteNotificationTypes: NSApplication.RemoteNotificationType](./enabledremotenotificationtypes.md)
  The types of push notifications that the app accepts.
- [var isRegisteredForRemoteNotifications: Bool](./isregisteredforremotenotifications.md)
  A Boolean value indicating whether the app is registered with Apple Push Notification service (APNs).
- [NSApplication.RemoteNotificationType](./remotenotificationtype.md)
  These constants determine whether apps launched by remote notifications display a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/registerforremotenotifications(matching:))*