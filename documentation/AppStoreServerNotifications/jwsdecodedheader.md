# JWSDecodedHeader

**Framework**: App Store Server Notifications  
**Kind**: dictionary

A decoded JSON Web Signature header containing transaction or renewal information.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
object JWSDecodedHeader
```

#### Discussion

All JWS representations, including the [`signedPayload`](signedpayload.md), contain a JWS header. When you Base64 URL-decode the header, use the [`JWSDecodedHeader`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSDecodedHeader) object to read its contents. Use the information in the [`JWSDecodedHeader`](jwsdecodedheader.md) to validate the JWS signature. For more information about validating signatures, see the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The App Store signs transaction and renewal information that you receive in [`App Store Server Notifications V2`](app-store-server-notifications-v2.md) and in the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI). It uses the following `x5c` certificate chain, in order:

1. A certificate that contains the public key that corresponds to the key the App Store uses to digitally sign the JWS. Section 4.11.10 Mac App Store Receipt Signing Certificates of the [`Apple Inc. Certificate Practice Statement Worldwide Developer Relations`](https://developer.apple.comhttps://images.apple.com/certificateauthority/pdf/Apple_WWDR_CPS_v1.26.pdf) document defines the policy for this certificate.
2. An Apple intermediate certificate from the [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/) site that starts with `Worldwide Developer Relations`.
3. An Apple root certificate.

For more information, or to download Apple’s root and intermediate certificates, see [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/).

## Topics

### JWS header types
- [type alg](alg.md)
  The JSON Web Signature (JWS) header parameter that identifies the cryptographic algorithm used to secure the JWS.
- [type x5c](x5c.md)
  The JSON Web Signature (JWS) header parameter that contains the certificate chain that corresponds to the key used to digitally sign the JWS.

## See Also

- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [Transaction data types](transaction-data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/jwsdecodedheader)*