# JWSDecodedHeader

**Framework**: Retention Messaging API  
**Kind**: dictionary

A decoded JSON Web Signature (JWS) header.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object JWSDecodedHeader
```

## Mentions

- [Responding to real-time retention messaging requests](responding-to-realtime-retention-messaging-requests.md)

#### Discussion

The type [`RealtimeRequestBody`](realtimerequestbody.md) contains a header that’s a `JWSDecodedHeader` object when decoded. Use the information in the `JWSDecodedHeader` to validate the JWS signature of the request body. For more information about validating signatures, see the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The signature uses the `x5c` certificate chain, in the following order:

1. A certificate that contains the public key that corresponds to the key the App Store uses to digitally sign the JWS. Section 4.11.10 Mac App Store Receipt Signing Certificates of the [`Apple Inc. Certificate Practice Statement Worldwide Developer Relations`](https://developer.apple.comhttps://images.apple.com/certificateauthority/pdf/Apple_WWDR_CPS_v1.26.pdf) document defines the custom extensions this certificate uses.
2. An Apple intermediate certificate that contains an extension with the extension ID for `Apple Worldwide Developer Relations (1.2.840.113635.100.6.2.1)`.
3. An Apple root certificate.

For more information, or to download Apple’s root certificate, see [`Apple PKI`](https://developer.apple.comhttps://www.apple.com/certificateauthority/).

## See Also

- [type alg](alg.md)
  An algorithm you use to sign a JSON Web Signature (JWS).
- [type x5c](x5c.md)
  A JSON Web Signature (JWS) header parameter that contains the certificate chain that corresponds to the key you use to digitally sign the JWS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/jwsdecodedheader)*