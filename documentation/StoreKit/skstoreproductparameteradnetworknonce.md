# SKStoreProductParameterAdNetworkNonce

**Framework**: StoreKit  
**Kind**: var

The key that represents a random value to use for added security.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- tvOS 11.3+

## Declaration

```swift
let SKStoreProductParameterAdNetworkNonce: String
```

## Mentions

- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md)
- [Combining parameters to generate a signature for SKAdNetwork 2](combining-parameters-to-generate-a-signature-for-skadnetwork-2.md)
- [Combining parameters to generate signatures for SKAdNetwork 2.2 and 3](combining-parameters-to-generate-signatures-for-skadnetwork-2-2-and-3.md)

#### Discussion

The value for this key is an [`NSUUID`](https://developer.apple.com/documentation/Foundation/NSUUID). Ad networks generate a random value for this key at the time of the ad impression.

> ❗ **Important**:  When you generate the signature value ([`SKStoreProductParameterAdNetworkAttributionSignature`](skstoreproductparameteradnetworkattributionsignature.md)), you must sign the nonce as an all-lowercase UUID string representation.

## See Also

- [let SKStoreProductParameterAdNetworkIdentifier: String](skstoreproductparameteradnetworkidentifier.md)
  The key that represents the advertising network’s unique identifier.
- [let SKStoreProductParameterAdNetworkCampaignIdentifier: String](skstoreproductparameteradnetworkcampaignidentifier.md)
  The key that represents the advertising network’s campaign.
- [let SKStoreProductParameterAdNetworkTimestamp: String](skstoreproductparameteradnetworktimestamp.md)
  The key that represents the UNIX time, in milliseconds, of the ad impression.
- [let SKStoreProductParameterAdNetworkAttributionSignature: String](skstoreproductparameteradnetworkattributionsignature.md)
  The key that represents the advertising network’s cryptographic signature to use for install validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworknonce)*