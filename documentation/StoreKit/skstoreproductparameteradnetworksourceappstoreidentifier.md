# SKStoreProductParameterAdNetworkSourceAppStoreIdentifier

**Framework**: StoreKit  
**Kind**: var

The key that represents the App Store ID of the app that displays the ad.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+

## Declaration

```swift
let SKStoreProductParameterAdNetworkSourceAppStoreIdentifier: String
```

## Mentions

- [Verifying an install-validation postback](verifying-an-install-validation-postback.md)
- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber). Provide the App Store item identifier of the app that’s displaying the ad.

During testing, if you’re using a development-signed build to display the ads and not an app from App Store, use `0` as the item identifier.

## See Also

- [let SKStoreProductParameterAdNetworkVersion: String](skstoreproductparameteradnetworkversion.md)
  The key that represents the version of the ad network API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworksourceappstoreidentifier)*