# Generating JWS impressions

**Framework**: AdAttributionKit

Create a JSON Web Signature (JWS) for use with app impressions in AdAttributionKit.

#### Overview

A JSON Web Signature (JWS) is an open standard ([`RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515)) that defines a way to securely transmit information. AdAttributionKit requires a JWS to create an [`AppImpression`](appimpression.md). You create the JWS and sign it with your private key. For more information about creating keys, see [`Registering an ad network`](registering-an-ad-network.md)

To generate a signed compact JWS:

1. Create the JOSE (JSON Object Signing and Encryption) header.
2. Create the JWS payload.
3. Sign the JWS.

#### Create the Jose Header

To create a JWS impression to use with AdAttributionKit, use the following fields and values in the header:

| Header field | Value |
| --- | --- |
| alg - encryption algorithm | ES256 — All JWSs for AdAttributionKit require signing with ES256 encryption. |
| kid - your ad network ID | The ad network ID you receive during ad network registration (for example, a string similar to `example.adattributionkit`). You can also use your existing SKAdNetwork ad network ID, which ends with `.skadnetwork`. |

Here’s an example of a JOSE header:

```json
    {
        "alg": "ES256",
        "kid": "example.adattributionkit"
    }
```

#### Create the Jws Payload

The JWS payload contains information about the advertisement, such as the advertised app item ID, publisher app item ID, source identifier, and type of impression. Use the following fields to include these values in the JWS payload:

| Payload field | Value |
| --- | --- |
| impression-identifier | The [`id`](appimpression/id.md) |
| publisher-item-identifier | The [`publisherItemID`](appimpression/publisheritemid.md) |
| impression-type | The impression type, `"app-impression"` |
| ad-network-identifier | A string that defines the ad network, such as `example.adattributionkit` |
| source-identifier | The hierarchical source identifier, which may include two, three, or four digits |
| timestamp | The time the ad network created the impression, in milliseconds since 1970 |
| advertised-item-identifier | The [`advertisedItemID`](appimpression/advertiseditemid.md) |
| eligible-for-re-engagement | A Boolean value that indicates whether the impression is eligible for reengagement. (optional) |

Here’s an example of a JWS payload:

```json
{
 "impression-identifier": "7aa9f8cc-5689-4c02-b963-22ca22136015",
 "publisher-item-identifier": 0,
 "impression-type": "app-impression",
 "ad-network-identifier": "example.adattributionkit",
 "source-identifier": 5239,
 "timestamp": 1679790422446,
 "advertised-item-identifier": 1108187390
}
```

To create impressions eligible for reengagement conversions, add the following field and value to the JWS payload:

```json
{
    // Other payload properties.
    "eligible-for-re-engagement": true
}
```

#### Sign the Jws

Use the private key you generated during ad network registration to sign the JWS using ES256 encryption.

You need to sign the JWS in the compact format outlined in [`section 5.1 of RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515#section-5.1?) that describes the JWS signature process and format, and conforms to the following format as a UTF-8 string:

```None
ASCII(BASE64URL(UTF8(JWS Protected Header)) || '.' || BASE64URL(JWS Payload))
```

This renders a compact JWS impression like the example below that you can pass into the API:

```None
eyJraWQiOiJleGFtcGxlLmFkYXR0cmlidXRpb25raXQiLCJhbGciOiJFUzI1NiJ9.eyJhZHZlcnRpc2VkLWl0ZW0taWRlbnRpZmllciI6MTEwODE4NzM5MCwiYWQtbmV0d29yay1pZGVudGlmaWVyIjoiZXhhbXBsZS5hZGF0dHJpYnV0aW9ua2l0IiwiaW1wcmVzc2lvbi10eXBlIjoiYXBwLWltcHJlc3Npb24iLCJlbGlnaWJsZS1mb3ItcmUtZW5nYWdlbWVudCI6dHJ1ZSwidGltZXN0YW1wIjoxNzE5NTk5OTU3MjM5LCJwdWJsaXNoZXItaXRlbS1pZGVudGlmaWVyIjo1ODM4NDkyLCJpbXByZXNzaW9uLWlkZW50aWZpZXIiOiI1NDRCOEZBRC0wQUQ1LTQ0MzQtOThCMi0zMjcxMTNBRjg0REIiLCJzb3VyY2UtaWRlbnRpZmllciI6NTIzOX0.zxQ_HcpB7pK6lWOms4LZ8uK3sZu_0S-bPR0My7UY4QlEAYFP-wp5eN1WuHOmNwoPD5cgazpwA3o5xq-fhfpOEQ
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/generating-jws-impressions)*