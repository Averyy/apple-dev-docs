# TransactionInfoResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains signed transaction information for a single transaction.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
object TransactionInfoResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The `TransactionInfoResponse` contains information about the transaction that you request using the [`Get Transaction Info`](get-transaction-info.md) endpoint. The [`transactionId`](transactionid.md) in the `signedTransactionInfo` matches the `transactionId` you provide in the request path.

## Topics

### Response data types
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

## See Also

- [Get Transaction Info](get-transaction-info.md)
  Get information about a single transaction for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/transactioninforesponse)*