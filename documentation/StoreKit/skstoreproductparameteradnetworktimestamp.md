# SKStoreProductParameterAdNetworkTimestamp

**Framework**: StoreKit  
**Kind**: var

The key that represents the UNIX time, in milliseconds, of the ad impression.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- tvOS 11.3+

## Declaration

```swift
let SKStoreProductParameterAdNetworkTimestamp: String
```

## Mentions

- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md)

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber). Ad networks generate the timestamp, represented as UNIX time in milliseconds, at the time you’re preparing to serve the ad.

## See Also

- [let SKStoreProductParameterAdNetworkIdentifier: String](skstoreproductparameteradnetworkidentifier.md)
  The key that represents the advertising network’s unique identifier.
- [let SKStoreProductParameterAdNetworkCampaignIdentifier: String](skstoreproductparameteradnetworkcampaignidentifier.md)
  The key that represents the advertising network’s campaign.
- [let SKStoreProductParameterAdNetworkNonce: String](skstoreproductparameteradnetworknonce.md)
  The key that represents a random value to use for added security.
- [let SKStoreProductParameterAdNetworkAttributionSignature: String](skstoreproductparameteradnetworkattributionsignature.md)
  The key that represents the advertising network’s cryptographic signature to use for install validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworktimestamp)*