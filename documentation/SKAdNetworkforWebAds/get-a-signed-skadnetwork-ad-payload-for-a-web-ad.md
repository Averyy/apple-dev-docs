# Get a Signed Web Ad Impression Payload

**Framework**: SKAdNetwork for Web Ads  
**Kind**: httpRequest

An endpoint you provide to receive requests from devices to serve signed ad interactions.

**Availability**:
- SKAdNetwork for Web Ads 1.0+

## Mentions

- [Creating an attributable ad link](creating-an-attributable-ad-link.md)
- [Generating a signature for attributable web ads](generating-a-signature-for-attributable-web-ads.md)

#### Discussion

You implement this endpoint on your server to provide signed SKAdNetwork ad payloads for web ads that users tap. The device calls this endpoint when a user taps an SKAdNetwork-attributable web ad.

To receive requests at this endpoint, your server needs to support the Transport Layer Security (TLS) 1.2 protocol or later.

The following is an example of an [`AdImpressionRequest`](adimpressionrequest.md) payload:

```json
{
    "source_domain": "example.com",
    "source_engagement_type": "click_to_App_Store",
    "source_nonce": "t8naKxXHTzuTJhNfljADPQ",
    "version": "4.0"
}
```

A corresponding [`AdImpressionResponse`](adimpressionresponse.md) to send in response to this payload is as follows:

```json
{
    "version": "4.0",
    "ad_network_id": "com.apple.test-1",
    "source_identifier": 3120,
    "itunes_item_id": 525463029,
    "nonce": "b7c9da2b-15c7-4f3b-9326-135f9630033d",
    "source_domain": "example.com",
    "timestamp": 1676057605705,
    "signature": "MEUCID/KZzaGxpa9jv9P1thWn8cHzcDq8ebDWEoarV1JrjNcAiEA6d9IqYErxFCrD96oR0rRftjVW6PRx37MC9QPS88OeE4="
}
```

> ❗ **Important**:  The `attributionSourceNonce` in a web ad, the `source_nonce` in an [`AdImpressionRequest`](adimpressionrequest.md), and the `nonce` in an [`AdImpressionResponse`](adimpressionresponse.md) all represent the same UUID, but the encoding varies.

 The `attributionSourceNonce` in a web ad, the `source_nonce` in an [`AdImpressionRequest`](adimpressionrequest.md), and the `nonce` in an [`AdImpressionResponse`](adimpressionresponse.md) all represent the same UUID, but the encoding varies.

The device uses the same encoding as `attributionSourceNonce` for the `source_nonce` value in the [`AdImpressionRequest`](adimpressionrequest.md). However, you use the dash-separated string representation of the UUID for the `nonce` value in an [`AdImpressionResponse`](adimpressionresponse.md).

## Request Body

The request that devices send to this endpoint, asking for the web ad impression from the ad network’s server.

## See Also

- [object AdImpressionRequest](adimpressionrequest.md)
  The request body that devices send to fetch the web ad impression from the ad network’s server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/skadnetworkforwebads/get-a-signed-skadnetwork-ad-payload-for-a-web-ad.)*