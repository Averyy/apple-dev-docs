# JWSTransaction

**Framework**: App Store Server API  
**Kind**: typealias

Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
string JWSTransaction
```

#### Discussion

The `JWSTransaction` type is a string of three Base64URL-encoded components separated by a period. The string contains the JWS Compact Serialization of the transaction information, signed by the App Store according to the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

- To read the transaction information, Base64URL-decode the payload. Use a [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) object to read the payload information.
- To read the header, decode it and use a [`JWSDecodedHeader`](jwsdecodedheader.md) object to access the information. Use the information in the header to verify the signature.

##### Use App Store Server Library Functions

To verify a `JWSTransaction` on your server, consider implementing the verification using the App Store Server Library function `verifyAndDecodeTransaction`. The library provides this function in each language the library supports. For more information, see [`Simplifying your implementation by using the App Store Server Library`](simplifying-your-implementation-by-using-the-app-store-server-library.md).

## See Also

- [object JWSDecodedHeader](jwsdecodedheader.md)
  A decoded JSON Web Signature (JWS) header containing transaction or renewal information.
- [type JWSAppTransaction](jwsapptransaction.md)
  App transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSAppTransactionDecodedPayload](jwsapptransactiondecodedpayload.md)
  A decoded payload that contains app transaction information.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information, signed by the App Store, in JSON Web Signature (JWS) format.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [Data types](data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/jwstransaction)*