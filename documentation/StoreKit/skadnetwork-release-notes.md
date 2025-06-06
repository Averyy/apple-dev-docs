# SKAdNetwork release notes

**Framework**: StoreKit

Learn about the features in each SKAdNetwork version.

#### Overview

Use the most recent version of SKAdNetwork available.

In version 2.0 and later, ad networks use a version number when signing ads. For StoreKit-rendered ads, you set the version number in the [`SKStoreProductParameterAdNetworkVersion`](skstoreproductparameteradnetworkversion.md) parameter. For view-through ads, you set the version number in the [`version`](skadimpression/version.md) property.

When you receive an install-validation postback, it contains the version number. Each version of SKAdNetwork has specific instructions for signing ads and validating the postback.

Developers of advertised apps are eligible to receive copies of winning postbacks, versions 2 and later, if the participants meet the following conditions:

- The developer of the advertised app opts-in to receive postbacks. For instructions on opting-in, see [`Configuring an advertised app`](configuring-an-advertised-app.md).
- The device is running iOS 15 or later.

## Topics

### SKAdNetwork versions
- [SKAdNetwork 4 release notes](skadnetwork-4-release-notes.md)
  A version of SKAdNetwork available in iOS 16.1 and later.
- [SKAdNetwork 3 release notes](skadnetwork-3-release-notes.md)
  A version of SKAdNetwork available in iOS 14.6 and later.
- [SKAdNetwork 2.2 release notes](skadnetwork-2-2-release-notes.md)
  A version of SKAdNetwork available in iOS 14.5 and later.
- [SKAdNetwork 2.1 release notes](skadnetwork-2-1-release-notes.md)
  A version of SKAdNetwork available in iOS 14 and later.
- [SKAdNetwork 2 release notes](skadnetwork-2-release-notes.md)
  A version of SKAdNetwork available in iOS 14 and later.
- [SKAdNetwork 1 release notes](skadnetwork-1-release-notes.md)
  A version of SKAdNetwork available in iOS 11.3 and later.

## See Also

- [Signing and providing ads](signing-and-providing-ads.md)
  Advertise apps by signing and providing StoreKit-rendered ads, view-through ads, or attributable web ads.
- [Receiving ad attributions and postbacks](receiving-ad-attributions-and-postbacks.md)
  Learn about timeframes and priorities for ad impressions that result in ad attributions, and how additional impressions qualify for postbacks.
- [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md)
  Learn about the data that postbacks may contain in each conversion window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadnetwork-release-notes)*