# SKAdImpression

**Framework**: StoreKit  
**Kind**: class

A class that defines an ad impression for a view-through ad.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
class SKAdImpression
```

## Mentions

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)
- [Signing and providing ads](signing-and-providing-ads.md)
- [SKAdNetwork 2.2 release notes](skadnetwork-2-2-release-notes.md)

#### Overview

Create a `SKAdImpression` instance when you’re preparing to present a view-through ad. In the instance, you set:

- Values known to you, including your ad network ID, the App Store IDs of the source app and the advertised app, and the version.
- A value you determine – the campaign ID.
- Values you generate, including the timestamp, a nonce (ad-impression identifier), and the cryptographic signature.

For information about generating the cryptographic signature, see [`Generating the signature to validate view-through ads`](generating-the-signature-to-validate-view-through-ads.md).

Use your `SKAdImpression` instance when you call [`startImpression(_:completionHandler:)`](skadnetwork/startimpression(_:completionhandler:).md) to begin presenting your view-through ad. Use the same instance when you call [`endImpression(_:completionHandler:)`](skadnetwork/endimpression(_:completionhandler:).md) to end the ad presentation.

## Topics

### Providing a signature
- [var signature: String](skadimpression/signature.md)
  The advertising network’s cryptographic signature for the ad impression.
### Creating a signature
- [init(sourceAppStoreItemIdentifier: NSNumber, advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String, adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp: NSNumber, signature: String, version: String)](skadimpression/init(sourceappstoreitemidentifier:advertisedappstoreitemidentifier:adnetworkidentifier:adcampaignidentifier:adimpressionidentifier:timestamp:signature:version:).md)
  Creates an ad impression object using the supplied values.
- [var version: String](skadimpression/version.md)
  The version of the SKAdNetwork API.
- [var adNetworkIdentifier: String](skadimpression/adnetworkidentifier.md)
  A string that represents the advertising network’s unique identifier.
- [var sourceIdentifier: NSNumber](skadimpression/sourceidentifier.md)
  A four-digit integer that ad networks define to represent the ad campaign.
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
### Describing ads
- [var adType: String?](skadimpression/adtype.md)
  The type of the ad.
- [var adDescription: String?](skadimpression/addescription.md)
  A human-readable description of the ad.
- [var adPurchaserName: String?](skadimpression/adpurchasername.md)
  The name of the entity that purchased the ad.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Understanding AdAttributionKit and SKAdNetwork interoperability](../AdAttributionKit/adattributionkit-skadnetwork-interoperability.md)
  Learn how attribution APIs interact to deliver ad impressions.
- [class SKAdNetwork](skadnetwork.md)
  A class that validates advertisement-driven app installations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression)*