# JWSTransaction

**Framework**: App Store Server Notifications  
**Kind**: typealias

Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string JWSTransaction
```

#### Discussion

The [`JWSTransaction`](jwstransaction.md) type is a string of three Base64URL-encoded components separated by a period. The string contains the JWS Compact Serialization of the transaction information, signed by the App Store according to the JSON Web Signature (JWS) [`IETF RFC 7515`](https://developer.apple.comhttps://datatracker.ietf.org/doc/html/rfc7515) specification.

The three components of the string are a header, a payload, and a signature, in that order.

- To read the transaction information, Base64URL-decode the payload. Use a [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) object to read the payload information.
- To read the header, decode it and use a [`JWSDecodedHeader`](jwsdecodedheader.md) object to access the information. Use the information in the header to verify the signature.

##### Use App Store Server Library Functions

To verify a [`JWSTransaction`](jwstransaction.md) on your server, consider implementing the verification using the App Store Server Library function `verifyAndDecodeTransaction`. The library provides this function in each language the library supports. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).

## See Also

- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- [object JWSRenewalInfoDecodedPayload](jwsrenewalinfodecodedpayload.md)
  A decoded payload containing subscription renewal information for an auto-renewable subscription.
- [object JWSTransactionDecodedPayload](jwstransactiondecodedpayload.md)
  A decoded payload that contains transaction information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/jwstransaction)*