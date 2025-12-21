# SKStoreProductParameterAdNetworkVersion

**Framework**: StoreKit  
**Kind**: var

The key that represents the version of the ad network API.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+

## Declaration

```swift
let SKStoreProductParameterAdNetworkVersion: String
```

## Mentions

- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)

#### Discussion

The value for this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString). Set this key to version number “`4.0`”, “`3.0`”, “`2.2"`, `“2.1"`, or `"2.0"`. Use the highest available version whenever possible. For version availability, see [`SKAdNetwork release notes`](skadnetwork-release-notes.md).

Ad networks use this key and the other [`Ad network install-validation keys`](ad-network-install-validation-keys.md) when signing ads. For more information, see [`Generating the signature to validate StoreKit-rendered ads`](generating-the-signature-to-validate-storekit-rendered-ads.md).

## See Also

- [let SKStoreProductParameterAdNetworkSourceAppStoreIdentifier: String](skstoreproductparameteradnetworksourceappstoreidentifier.md)
  The key that represents the App Store ID of the app that displays the ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkversion)*