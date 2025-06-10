# Default Calling App

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app can be the default calling app on someone’s device.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- watchOS 11.2+

#### Discussion

Add the Default Calling App entitlement to your app by following these steps:

1. In the Xcode project navigator, select your app’s target, and then the Signing & Capabilities tab.
2. Add a new capability by clicking the + Capability button and then type “Default Calling” in the search field.
3. Double-click the Default Calling App entry to add the entitlement to your app.

Xcode displays the Default Calling App entitlement, along with any other entitlements, in the capabilities list under your app’s signing information. For more information, see [`Preparing your app to be the default calling app`](https://developer.apple.com/documentation/CallKit/Preparing-your-app-to-be-the-default-calling-app).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.calling-app)*