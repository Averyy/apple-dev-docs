# Persistent Content Capture

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.

**Availability**:
- macOS 14.4+

#### Discussion

The Persistent Content Capture entitlement enables VNC apps to view and record the screen.

Before your app can use this entitlement, request permission to use it by submitting the [`Persistent Content Capture Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/persistent-content-capture/) form. After receiving permission from Apple to use this entitlement, add it to your app’s profile in Xcode following the instrucitons Apple provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.persistent-content-capture)*