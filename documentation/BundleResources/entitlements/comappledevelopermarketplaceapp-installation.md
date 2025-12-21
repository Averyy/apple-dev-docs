# com.apple.developer.marketplace.app-installation

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that enables an app to vend other apps as an alternative app marketplace.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

#### Discussion

The system requires that your app have this entitlement to implement an app marketplace and install other apps using [`MarketplaceKit`](https://developer.apple.com/documentation/MarketplaceKit). Apple approves your use of this entitlement based on a set of criteria. To request the entitlement, see [`Participating in alternative distribution for specific regions`](https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions). For more information, see [`Creating an alternative app marketplace`](https://developer.apple.com/documentation/appdistribution/creating-an-alternative-app-marketplace).

If your account receives this entitlement, provision your app with the entitlement according to: [`Provisioning with managed capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/).

> **Note**:  This entitlement isn’t available for Enterprise or Developer ID distributed apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.marketplace.app-installation)*