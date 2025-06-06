# JWSRenewalInfo

**Framework**: App Store Server API  
**Kind**: typealias

Subscription renewal information, signed by the App Store, in JSON Web Signature (JWS) format.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
string JWSRenewalInfo
```

#### Discussion

The `JWSRenewalInfo` type is a string of three Base64 URL-encoded components, separated by a period, containing subscription renewal information signed by the App Store. The App Store signs the string according to the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components in the string are a header, a payload, and a signature.

- To read the subscription renewal information, decode the payload. Use a [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) object to read the payload information.
- To read the header, decode it and use a [`JWSDecodedHeader`](jwsdecodedheader.md) object to access the information. Use the information in the header to verify the signature.

## See Also

- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature (JWS) header containing transaction or renewal information.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [Data types](data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/jwsrenewalinfo)*