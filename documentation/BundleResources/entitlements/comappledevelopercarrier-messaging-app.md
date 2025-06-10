# Default Carrier Messaging App

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app can use the TelephonyMessagingKit framework to serve as the default carrier messaging app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

#### Discussion

Add the Default Carrier Messaging App entitlement to your app by following these steps:

1. In the Xcode project navigator, select your app’s target, and then the Signing & Capabilities tab.
2. Add a new capability by clicking the + Capability button and then type “Default Carrier Messaging” in the search field.
3. Double-click the Default Carrier Messaging App entry to add the entitlement to your app.

> ❗ **Important**: You may develop and test TelephonyMessagingKit apps on devices in all regions by using an Apple-provided provisioning profile. People using your app must have an account registered in the European Union (EU), and their device must be located within the EU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.carrier-messaging-app)*