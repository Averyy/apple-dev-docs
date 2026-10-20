# com.apple.developer.marketplace.app-installation

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that enables an app to vend other apps as an alternative app marketplace.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Details

- **Name**: `com.apple.developer.marketplace.app-installation`
- **Type**: boolean



**Default**: `NO`

#### Discussion

The system requires that your app have this entitlement to implement an app marketplace and install other apps using [MarketplaceKit](../../MarketplaceKit/MarketplaceKit.md). Apple approves your use of this entitlement based on a set of criteria. To request the entitlement, see [Participating in alternative distribution for specific regions](../../MarketplaceKit/participating-in-alternative-distribution-for-specific-regions.md). For more information, see [Creating an alternative app marketplace](../../MarketplaceKit/creating-an-alternative-app-marketplace.md).

If your account receives this entitlement, provision your app with the entitlement according to: [Provisioning with managed capabilities](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/).

> **Note**:  This entitlement isn’t available for Enterprise or Developer ID distributed apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.marketplace.app-installation)*