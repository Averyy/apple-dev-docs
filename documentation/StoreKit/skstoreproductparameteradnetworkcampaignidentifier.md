# SKStoreProductParameterAdNetworkCampaignIdentifier

**Framework**: StoreKit  
**Kind**: var

The key that represents the advertising network’s campaign.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- tvOS 11.3+

## Declaration

```swift
let SKStoreProductParameterAdNetworkCampaignIdentifier: String
```

## Mentions

- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)
- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md)
- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber). Ad networks determine their own campaign identifiers, which must be an integer `>=1` and `<=100`.

Use [`SKStoreProductParameterAdNetworkSourceIdentifier`](skstoreproductparameteradnetworksourceidentifier.md) instead of this value to generate version 4 and later signatures.

## See Also

- [let SKStoreProductParameterAdNetworkIdentifier: String](skstoreproductparameteradnetworkidentifier.md)
  The key that represents the advertising network’s unique identifier.
- [let SKStoreProductParameterAdNetworkTimestamp: String](skstoreproductparameteradnetworktimestamp.md)
  The key that represents the UNIX time, in milliseconds, of the ad impression.
- [let SKStoreProductParameterAdNetworkNonce: String](skstoreproductparameteradnetworknonce.md)
  The key that represents a random value to use for added security.
- [let SKStoreProductParameterAdNetworkAttributionSignature: String](skstoreproductparameteradnetworkattributionsignature.md)
  The key that represents the advertising network’s cryptographic signature to use for install validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkcampaignidentifier)*