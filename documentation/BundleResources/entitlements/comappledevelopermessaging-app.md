# Default Messaging App

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app can be the default messaging app on someone’s device.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

#### Discussion

Add the Default Messaging App entitlement to your app by following these steps:

1. In the Xcode project navigator, select your app’s target, and then the Signing & Capabilities tab
2. Add a new capability by clicking the + Capability button and then type “Default Messaging””” in the search field.
3. Double-click the Default Messaging App entry to add the entitlement to your app.

Xcode displays the Default Messaging App entitlement, along with any other entitlements, in the capabilities list under your app’s signing information. For more information on preparing your app to become the default messaging app, see [`Preparing your app to be the default messaging app`](https://developer.apple.com/documentation/Messages/Preparing-your-app-to-be-the-default-messaging-app).

## See Also

- [Critical Messaging](entitlements/com.apple.developer.messages.critical-messaging.md)
  A Boolean value that indicates whether an app can use the Critical Messaging API to send SMS messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.messaging-app)*