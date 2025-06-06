# AdImpressionRequest

**Framework**: SKAdNetwork for Web Ads  
**Kind**: dictionary

The request body that devices send to fetch the web ad impression from the ad network’s server.

**Availability**:
- SKAdNetwork for Web Ads 1.0+

## Declaration

```swift
object AdImpressionRequest
```

## Mentions

- [Creating an attributable ad link](creating-an-attributable-ad-link.md)

#### Discussion

The device generates the [`AdImpressionRequest`](adimpressionrequest.md) and sends it in the body of a [`Get a Signed Web Ad Impression Payload`](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md) request. The device uses the value from the `attributionSourceNonce` in a web ad link for the `source_nonce` value in this request. The ad network looks up the fully signed web ad impression using the `source_nonce` value, which it creates when it serves the attributable ad link.

> ❗ **Important**:  The `attributionSourceNonce` in a web ad, the `source_nonce` in this request, and the `nonce` in a corresponding [`AdImpressionResponse`](adimpressionresponse.md) all represent the same UUID, but the encoding varies.

 The `attributionSourceNonce` in a web ad, the `source_nonce` in this request, and the `nonce` in a corresponding [`AdImpressionResponse`](adimpressionresponse.md) all represent the same UUID, but the encoding varies.

## See Also

- [Get a Signed Web Ad Impression Payload](get-a-signed-skadnetwork-ad-payload-for-a-web-ad..md)
  An endpoint you provide to receive requests from devices to serve signed ad interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/skadnetworkforwebads/adimpressionrequest)*