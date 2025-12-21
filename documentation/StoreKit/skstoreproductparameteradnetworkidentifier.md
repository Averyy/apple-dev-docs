# SKStoreProductParameterAdNetworkIdentifier

**Framework**: StoreKit  
**Kind**: var

The key that represents the advertising network’s unique identifier.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- tvOS 11.3+

## Declaration

```swift
let SKStoreProductParameterAdNetworkIdentifier: String
```

## Mentions

- [Combining parameters to generate a signature for SKAdNetwork 1](combining-parameters-to-generate-a-signature-for-skadnetwork-1.md)
- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)

#### Discussion

The value for this key is an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString).

Ad networks obtain an ad network identifier during registration. Ad networks are responsible for sharing their ad network IDs with participating app developers. Apps that display ads and need to initiate the app install validation process must include the ad network ID in their `Info.plist`. For more information see [`Registering an ad network`](registering-an-ad-network.md) and `Configuring Apps`.

## See Also

- [let SKStoreProductParameterAdNetworkCampaignIdentifier: String](skstoreproductparameteradnetworkcampaignidentifier.md)
  The key that represents the advertising network’s campaign.
- [let SKStoreProductParameterAdNetworkTimestamp: String](skstoreproductparameteradnetworktimestamp.md)
  The key that represents the UNIX time, in milliseconds, of the ad impression.
- [let SKStoreProductParameterAdNetworkNonce: String](skstoreproductparameteradnetworknonce.md)
  The key that represents a random value to use for added security.
- [let SKStoreProductParameterAdNetworkAttributionSignature: String](skstoreproductparameteradnetworkattributionsignature.md)
  The key that represents the advertising network’s cryptographic signature to use for install validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkidentifier)*