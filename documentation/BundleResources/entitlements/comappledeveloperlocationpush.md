# com.apple.developer.location.push

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

#### Discussion

This entitlement enables your app to monitor for Apple Push Notification service (APNs) pushes with the `location` push type, and receive pushes in your Location Push Service Extension. For more information about the `location` push type, see [`Sending notification requests to APNs`](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns).

Before submitting an app with this entitlement to the App Store, you must get permission to use the entitlement. To apply for the entitlement, log in to your Apple Developer Account with an Account Holder role and fill out the [`request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/location-push-service-extension/).

After you have the permission, add the entitlement to your app by opening the project’s entitlements file in Xcode. Add the key [`com.apple.developer.location.push`](entitlements/com.apple.developer.location.push.md) and set the corresponding value to `YES`. Without this entitlement, your code gets an error when it calls [`startMonitoringLocationPushes(completion:)`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/startMonitoringLocationPushes(completion:)).

For more information about implementing your Location Push Service Extension, see [`Creating a location push service extension`](https://developer.apple.com/documentation/CoreLocation/creating-a-location-push-service-extension).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.location.push)*