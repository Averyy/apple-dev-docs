# Location Push Service Extension

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+

#### Discussion

This entitlement enables your app to monitor for Apple Push Notification service (APNs) pushes with the `location` push type, and receive pushes in your Location Push Service Extension. For more information about the `location` push type, see [`Sending notification requests to APNs`](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns).

> **Note**: Without this entitlement, your code receives an error when it calls [`startMonitoringLocationPushes(completion:)`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/startMonitoringLocationPushes(completion:)).

Add the entitlement to your app by following these steps:

1. Open your app’s Xcode project and select your app from the target list.
2. Select the Signing & Capabilities panel.
3. Click “+ Capabilities” and enter “push” in the search field; then double-click Location Push Service Extension to add the entitlement to your app’s entitlements file.

For more information about implementing your Location Push Service Extension, see [`Creating a location push service extension`](https://developer.apple.com/documentation/CoreLocation/creating-a-location-push-service-extension).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.location.push)*