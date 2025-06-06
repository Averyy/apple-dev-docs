# AdImpressionResponse

**Framework**: SKAdNetwork for Web Ads  
**Kind**: dictionary

The response you provide that contains a signed payload for a clicked web ad.

**Availability**:
- SKAdNetwork for Web Ads 1.0+

## Declaration

```swift
object AdImpressionResponse
```

## Mentions

- [Creating an attributable ad link](creating-an-attributable-ad-link.md)
- [Generating a signature for attributable web ads](generating-a-signature-for-attributable-web-ads.md)

#### Discussion

This is a response that you provide to the [`Get a Signed Web Ad Impression Payload`](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md) endpoint. When you create an [`AdImpressionResponse`](adimpressionresponse.md), use the dash-separated string representation of the UUID, which you decode from the `source_nonce` in the [`AdImpressionRequest`](adimpressionrequest.md) that you receive.

> ❗ **Important**:  The `attributionSourceNonce` in a web ad link, the `source_nonce` in an [`AdImpressionRequest`](adimpressionrequest.md), and the `nonce` in this response all represent the same UUID, but the encoding varies.

 The `attributionSourceNonce` in a web ad link, the `source_nonce` in an [`AdImpressionRequest`](adimpressionrequest.md), and the `nonce` in this response all represent the same UUID, but the encoding varies.

## See Also

- [Generating a signature for attributable web ads](generating-a-signature-for-attributable-web-ads.md)
  Initiate install-validation by providing the signed parameters for an attributable web ad.
- [object signature](signature.md)
  The key-value pairs that ad networks use to cryptographically sign a web ad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/skadnetworkforwebads/adimpressionresponse)*