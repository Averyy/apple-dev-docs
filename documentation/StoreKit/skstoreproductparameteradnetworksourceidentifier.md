# SKStoreProductParameterAdNetworkSourceIdentifier

**Framework**: StoreKit  
**Kind**: var

A four-digit integer that ad networks define to represent the ad campaign.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- tvOS 16.1+

## Declaration

```swift
let SKStoreProductParameterAdNetworkSourceIdentifier: String
```

## Mentions

- [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md)
- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)
- [SKAdNetwork 4 release notes](skadnetwork-4-release-notes.md)

#### Discussion

This key is available for ad impressions that use SKAdNetwork 4 and later. The [`SKStoreProductParameterAdNetworkSourceIdentifier`](skstoreproductparameteradnetworksourceidentifier.md), also known as the , replaces and extends the campaign identifier value, [`SKStoreProductParameterAdNetworkCampaignIdentifier`](skstoreproductparameteradnetworkcampaignidentifier.md).

Ad networks and developers define the meaning of the hierarchical source identifier. This string represents an integer of up to four digits. You can encode information about your advertisement in each set of digits; you may receive two, three, or all four digits of the [`sourceIdentifier`](skadimpression/sourceidentifier.md) in the first winning postback, depending on the ad impression’s postback data tier. For more information about the value you may get in the postback, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworksourceidentifier)*