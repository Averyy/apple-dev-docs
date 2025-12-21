# Critical Alerts

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that permits an app to receive critical alert notifications.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

#### Discussion

If your app has this entitlement, then it can request [`criticalAlert`](https://developer.apple.com/documentation/UserNotifications/UNAuthorizationOptions/criticalAlert) authorization to receive push notifications that cause the system to play a sound even when the app is locked, muted, or a person uses Do Not Disturb focus. Your app can specify a custom sound and volume for critical alerts.

To request this entitlement for your app, [`fill out the request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).

## See Also

- [APS Environment Entitlement](entitlements/aps-environment.md)
  The environment for push notifications.
- [APS Environment (macOS) Entitlement](entitlements/com.apple.developer.aps-environment.md)
  The environment for push notifications in macOS apps.
- [com.apple.developer.usernotifications.filtering](entitlements/com.apple.developer.usernotifications.filtering.md)
  Enable receiving notifications without displaying the notification to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.usernotifications.critical-alerts)*