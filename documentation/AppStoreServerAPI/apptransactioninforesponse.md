# AppTransactionInfoResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains signed app transaction information for a customer.

**Availability**:
- App Store Server API 1.17+

## Declaration

```swift
object AppTransactionInfoResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

This response contains information that you request by calling the [`Get App Transaction Info`](get-app-transaction-info.md) endpoint. For information on decoding and reading the app transaction, see [`JWSAppTransaction`](jwsapptransaction.md) and [`JWSAppTransactionDecodedPayload`](jwsapptransactiondecodedpayload.md).

## Topics

### Response data types
- [type JWSAppTransaction](jwsapptransaction.md)
  App transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.
- [object JWSAppTransactionDecodedPayload](jwsapptransactiondecodedpayload.md)
  A decoded payload that contains app transaction information.

## See Also

- [Get App Transaction Info](get-app-transaction-info.md)
  Get a customer’s app transaction information for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/apptransactioninforesponse)*