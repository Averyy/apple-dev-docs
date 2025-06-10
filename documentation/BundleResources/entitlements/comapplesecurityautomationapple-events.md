# Apple Events Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app may prompt the user for permission to send Apple events to other apps.

**Availability**:
- macOS 10.7+

#### Discussion

Your app doesn’t need the Apple Events entitlement if it only sends Apple events to itself or to other processes signed with the same team ID.

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Resource Access, select Apple Events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.automation.apple-events)*