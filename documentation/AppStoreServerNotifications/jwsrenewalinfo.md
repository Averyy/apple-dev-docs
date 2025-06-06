# JWSRenewalInfo

**Framework**: App Store Server Notifications  
**Kind**: typealias

Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string JWSRenewalInfo
```

#### Discussion

The [`JWSRenewalInfo`](jwsrenewalinfo.md) type is a string of three Base64 URL-encoded components, separated by a period. The string contains the JWS representation of the subscription renewal information, signed by the App Store according to the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components in the string are a header, a payload, and a signature, in that order.

To read the subscription renewal information, Base64 URL-decode the payload. Use a [`JWSRenewalInfoDecodedPayload`](jwsrenewalinfodecodedpayload.md) object to read the payload information.

To read the header, Base64 URL-decode it and use a [`JWSDecodedHeader`](jwsdecodedheader.md) object to access the information. Use the information in the header to verify the signature.

## See Also

- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/jwsrenewalinfo)*