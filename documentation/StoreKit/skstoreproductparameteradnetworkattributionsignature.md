# SKStoreProductParameterAdNetworkAttributionSignature

**Framework**: StoreKit  
**Kind**: var

The key that represents the advertising network’s cryptographic signature to use for install validation.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- tvOS 11.3+

## Declaration

```swift
let SKStoreProductParameterAdNetworkAttributionSignature: String
```

## Mentions

- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Signing and providing ads](signing-and-providing-ads.md)

#### Discussion

The value for this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString). The ad network creates the cryptographic signature, used to sign ads. For instructions on generating this value, see [`Generating the signature to validate StoreKit-rendered ads`](generating-the-signature-to-validate-storekit-rendered-ads.md).

## See Also

- [let SKStoreProductParameterAdNetworkIdentifier: String](skstoreproductparameteradnetworkidentifier.md)
  The key that represents the advertising network’s unique identifier.
- [let SKStoreProductParameterAdNetworkCampaignIdentifier: String](skstoreproductparameteradnetworkcampaignidentifier.md)
  The key that represents the advertising network’s campaign.
- [let SKStoreProductParameterAdNetworkTimestamp: String](skstoreproductparameteradnetworktimestamp.md)
  The key that represents the UNIX time, in milliseconds, of the ad impression.
- [let SKStoreProductParameterAdNetworkNonce: String](skstoreproductparameteradnetworknonce.md)
  The key that represents a random value to use for added security.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkattributionsignature)*