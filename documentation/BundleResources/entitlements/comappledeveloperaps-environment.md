# APS Environment (macOS) Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

The environment for push notifications in macOS apps.

**Availability**:
- macOS 10.14+

#### Discussion

This key specifies whether to use the development or production Apple Push Notification service (APNs) environment when registering for push notifications with [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/AppKit/NSApplication/registerForRemoteNotifications()).

Xcode sets the value of the entitlement based on your app’s current provisioning profile. For example, if you’re using a development provisioning profile, Xcode sets the value to `development`.

To add this entitlement to your app, enable the Push Notifications capability in Xcode.

## See Also

- [Registering your app with APNs](../UserNotifications/registering-your-app-with-apns.md)
  Communicate with Apple Push Notification service (APNs) and receive a unique device token that identifies your app.
- [APS Environment Entitlement](entitlements/aps-environment.md)
  The environment for push notifications.
- [Critical Alerts](entitlements/com.apple.developer.usernotifications.critical-alerts.md)
  An entitlement that permits an app to receive critical alert notifications.
- [com.apple.developer.usernotifications.filtering](entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.aps-environment)*