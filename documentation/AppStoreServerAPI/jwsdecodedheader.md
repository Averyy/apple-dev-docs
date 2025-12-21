# JWSDecodedHeader

**Framework**: App Store Server API  
**Kind**: dictionary

A decoded JSON Web Signature (JWS) header containing transaction or renewal information.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object JWSDecodedHeader
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The types [`JWSTransaction`](jwstransaction.md) and [`JWSRenewalInfo`](jwsrenewalinfo.md) contain headers that are [`JWSDecodedHeader`](jwsdecodedheader.md) objects when decoded. Use the information in the [`JWSDecodedHeader`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSDecodedHeader) to validate the JWS signature. For more information about validating signatures, see the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The App Store signs transaction and renewal information that you receive in [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) and in the [`App Store Server API`](AppStoreServerAPI.md). It uses the following `x5c` certificate chain, in the following order:

1. A certificate that contains the public key that corresponds to the key the App Store uses to digitally sign the JWS. Section 4.11.10 Mac App Store Receipt Signing Certificates of the [`Apple Inc. Certificate Practice Statement Worldwide Developer Relations`](https://developer.apple.comhttps://images.apple.com/certificateauthority/pdf/Apple_WWDR_CPS_v1.26.pdf) document defines the custom extensions this certificate uses.
2. An Apple intermediate certificate that contains an extension with the extension ID for `Apple Worldwide Developer Relations (1.2.840.113635.100.6.2.1)`.
3. An Apple root certificate.

For more information, or to download Apple’s root certificate, see [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/).

## Topics

### Data types
- [type alg](alg.md)
  An algorithm used to sign a JSON Web Signature.
- [type x5c](x5c.md)
  The JSON Web Signature (JWS) header parameter that contains the certificate chain that corresponds to the key used to digitally sign the JWS.

## See Also

- [type JWSAppTransaction](jwsapptransaction.md)
  App transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSAppTransactionDecodedPayload](jwsapptransactiondecodedpayload.md)
  A decoded payload that contains app transaction information.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.
- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information, signed by the App Store, in JSON Web Signature (JWS) format.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [Data types](data-types.md)
  Refer to these data types for decoded transaction and renewal information payloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/jwsdecodedheader)*