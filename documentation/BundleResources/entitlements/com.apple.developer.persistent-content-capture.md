# Persistent Content Capture

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.

**Availability**:
- macOS 14.4+

## Details

- **Name**: `com.apple.developer.persistent-content-capture`
- **Type**: boolean



**Default**: `NO`

#### Discussion

The Persistent Content Capture entitlement enables VNC apps to view and record the screen.

Before your app can use this entitlement, request permission to use it by submitting the [Persistent Content Capture Entitlement Request](https://developer.apple.com/contact/request/persistent-content-capture/) form. After receiving permission from Apple to use this entitlement, add it to your app’s profile in Xcode following the instrucitons Apple provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.persistent-content-capture)*