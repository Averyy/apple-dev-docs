# signature

**Framework**: SKAdNetwork for Web Ads  
**Kind**: dictionary

The key-value pairs that ad networks use to cryptographically sign a web ad.

**Availability**:
- SKAdNetwork for Web Ads 1.0+

## Declaration

```swift
object signature
```

## Mentions

- [Generating a signature for attributable web ads](generating-a-signature-for-attributable-web-ads.md)

#### Discussion

Use the required parameters in the [`signature`](signature.md) object to generate a cryptographic signature for the [`AdImpressionResponse`](adimpressionresponse.md). For more information, see [`Generating a signature for attributable web ads`](generating-a-signature-for-attributable-web-ads.md).

## Properties

- `version` (string) *(required)*: The SKAdNetwork version. Use version `“4.0”` or later. For version information, see [`SKAdNetwork release notes`](https://developer.apple.com/documentation/StoreKit/skadnetwork-release-notes).
- `ad_network_id` (string) *(required)*: The ad network ID. You receive an ad network ID when you register to use SKAdNetwork. For more information, see [`Registering an ad network`](https://developer.apple.com/documentation/StoreKit/registering-an-ad-network).
- `source_identifier` (integer) *(required)*: A four-digit value you use to measure the aspects of an advertising effort or campaign.
- `itunes_item_id` (integer) *(required)*: The App Store ID of the app that the ad impression advertises. This is the same value the ad network provides in the attributable ad link. For more information, see [`Creating an attributable ad link`](creating-an-attributable-ad-link.md).
- `nonce` (string) *(required)*: A UUID you generate to include in the signature. This value needs to match the value of `attributionSourceNonce` in the original ad link. This value needs to be in the `UUID` string format. Provide the dash-separated representation of the `attributionSourceNonce`.
- `source_domain` (string) *(required)*: The effective top-level domain and one more preceding path component (eTLD+1) representation of the ad network that seeks ad attribution.
- `fidelity_type` (integer) *(required)*: The fidelity type value for web ads is `1`.
- `timestamp` (integer) *(required)*: An integer that represents the UNIX time, in milliseconds, of the ad impression.

## See Also

- [Generating a signature for attributable web ads](generating-a-signature-for-attributable-web-ads.md)
  Initiate install-validation by providing the signed parameters for an attributable web ad.
- [object AdImpressionResponse](adimpressionresponse.md)
  The response you provide that contains a signed payload for a clicked web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/skadnetworkforwebads/signature)*