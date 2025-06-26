# APS Environment Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

The environment for push notifications.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

#### Discussion

This key specifies whether to use the development or production Apple Push Notification service (APNs) environment when registering for push notifications.

Xcode sets the value of the entitlement based on your app’s current provisioning profile. For example, if you’re using a development provisioning profile, Xcode sets the value to `development`. Production provisioning profile and [`Prerelease Versions and Beta Testers`](https://developer.apple.com/documentation/AppStoreConnectAPI/prerelease-versions-and-beta-testers) use `production`. These default settings can be modified. The `development` environment is also referred to as the `sandbox` environment.

Use this entitlement for both the UserNotifications and PushKit frameworks.

To add this entitlement to your app, enable the Push Notifications capability in Xcode.

## See Also

- [Registering your app with APNs](../UserNotifications/registering-your-app-with-apns.md)
  Communicate with Apple Push Notification service (APNs) and receive a unique device token that identifies your app.
- [PushKit](../PushKit/PushKit.md)
  Respond to push notifications related to your app’s complications, file providers, and VoIP services.
- [APS Environment (macOS) Entitlement](entitlements/com.apple.developer.aps-environment.md)
  The environment for push notifications in macOS apps.
- [Critical Alerts](entitlements/com.apple.developer.usernotifications.critical-alerts.md)
  An entitlement that permits an app to receive critical alert notifications.
- [com.apple.developer.usernotifications.filtering](entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment)*