# sourceIdentifier

**Framework**: Storekit  
**Kind**: property

A four-digit integer that ad networks define to represent the ad campaign.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
var sourceIdentifier: NSNumber { get set }
```

## Mentions

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)
- [Identifying the parameters in install-validation postbacks](identifying-the-parameters-in-install-validation-postbacks.md)
- [SKAdNetwork 4 release notes](skadnetwork-4-release-notes.md)

#### Discussion

The [`sourceIdentifier`](skadimpression/sourceidentifier.md) key is available for ad impressions that use SKAdNetwork 4 and later. The [`sourceIdentifier`](skadimpression/sourceidentifier.md), also known as the , replaces and extends the campaign identifier value, [`adCampaignIdentifier`](skadimpression/adcampaignidentifier.md).

Ad networks and developers define the meaning of the hierarchical source identifier. This integer can have up to four digits. You can encode information about your advertisement in each set of digits; you may receive two, three, or all four digits of the [`sourceIdentifier`](skadimpression/sourceidentifier.md) in the first winning postback, depending on the ad impression’s postback data tier. For more information about the value you may get in the postback, see [`Receiving postbacks in multiple conversion windows`](receiving-postbacks-in-multiple-conversion-windows.md).

> **Note**:  An install-validation postback represents this integer as a string in its `source-identifier` parameter. For more details about the parameters of an install-validation postback, see [`Identifying the parameters in install-validation postbacks`](identifying-the-parameters-in-install-validation-postbacks.md).

## See Also

- [init(sourceAppStoreItemIdentifier: NSNumber, advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String, adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp: NSNumber, signature: String, version: String)](skadimpression/init(sourceappstoreitemidentifier:advertisedappstoreitemidentifier:adnetworkidentifier:adcampaignidentifier:adimpressionidentifier:timestamp:signature:version:).md)
  Creates an ad impression object using the supplied values.
- [var version: String](skadimpression/version.md)
  The version of the SKAdNetwork API.
- [var adNetworkIdentifier: String](skadimpression/adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var adCampaignIdentifier: NSNumber](skadimpression/adcampaignidentifier.md)
  A number that represents the advertising network’s campaign.
- [var advertisedAppStoreItemIdentifier: NSNumber](skadimpression/advertisedappstoreitemidentifier.md)
  The App Store ID of the app that the ad impression advertises.
- [var adImpressionIdentifier: String](skadimpression/adimpressionidentifier.md)
  A random value to use for added security.
- [var sourceAppStoreItemIdentifier: NSNumber](skadimpression/sourceappstoreitemidentifier.md)
  The App Store ID of the app that displays the ad.
- [var timestamp: NSNumber](skadimpression/timestamp.md)
  A number that represents the UNIX time, in milliseconds, of the ad impression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/sourceidentifier)*