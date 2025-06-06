# PushKit

**Framework**: PushKit  
**Kind**: module

Respond to push notifications related to your app’s complications, file providers, and VoIP services.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

#### Overview

The PushKit framework supports specialized notifications for updating your watchOS complications, responding to file provider changes, and receiving incoming Voice-over-IP (VoIP) calls. PushKit notifications differ from the ones you handle with the [`User Notifications`](https://developer.apple.com/documentation/UserNotifications) framework. Instead of displaying an alert, badging your app’s icon, or playing a sound, PushKit notifications wake up or launch your app and give it time to respond. Both PushKit and User Notifications use the Apple Push Notification service (APNs) to deliver push notifications to user devices.

To receive PushKit notifications, your app creates a [`PKPushRegistry`](pkpushregistry.md) object and uses it to configure the notification types it supports. When registration is successful, PushKit delivers a unique data token to your app that contains the identity of the current device and the push type. Forward that token along to the server, and include it in any notifications you send to the user. APNs uses the token to deliver the correct type of notification to the user’s device.

For information about how to configure your server to work with APNs, see [`Setting up a remote notification server`](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server).

> **Note**: PushKit doesn’t support some special use cases in which access to Apple Push Notification service (APNs) isn’t possible. For information about when you might need to support these cases, see [`iOS 10 and the Legacy VoIP Architecture`](https://developer.apple.comhttps://developer.apple.com/library/archive/qa/qa1938/_index.html#//apple_ref/doc/uid/DTS40017564).

PushKit doesn’t support some special use cases in which access to Apple Push Notification service (APNs) isn’t possible. For information about when you might need to support these cases, see [`iOS 10 and the Legacy VoIP Architecture`](https://developer.apple.comhttps://developer.apple.com/library/archive/qa/qa1938/_index.html#//apple_ref/doc/uid/DTS40017564).

## Topics

### Registration
- [Supporting PushKit Notifications in Your App](supporting-pushkit-notifications-in-your-app.md)
  Declare the types of PushKit notifications your app supports and configure objects to respond to them.
- [class PKPushRegistry](pkpushregistry.md)
  An object that requests the delivery and handles the receipt of PushKit notifications.
- [protocol PKPushRegistryDelegate](pkpushregistrydelegate.md)
  The methods that you use to handle incoming PushKit notifications and registration events.
- [class PKPushCredentials](pkpushcredentials.md)
  An object that encapsulates the device token you use to deliver push notifications to your app.
### Push Types
- [Responding to VoIP Notifications from PushKit](responding-to-voip-notifications-from-pushkit.md)
  Receive incoming Voice-over-IP (VoIP) push notifications and use them to display the system call interface to the user.
- [struct PKPushType](pkpushtype.md)
  Constants reflecting the push types you want to support.
### Payload
- [class PKPushPayload](pkpushpayload.md)
  An object that contains information about a received PushKit notification.
### Data export
- [Exporting delivery metrics logs](exporting-delivery-metrics-logs.md)
  Download and analyze push-notification metrics.
- [Exporting broadcast push notification metrics](exporting-broadcast-push-notification-metrics.md)
  Discover how many people subscribe to your broadcast channels, and how many messages they receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PushKit)*