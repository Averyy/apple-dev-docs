# RefundLookupResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains an array of signed JSON Web Signature (JWS) transactions.

**Availability**:
- App Store Server API 1.1+

## Declaration

```swift
object RefundLookupResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

If the customer hasn’t received any refunds for in-app purchases in your app, the `signedTransactions` array is empty. To read the transaction information, decode the payload for each [`JWSTransaction`](jwstransaction.md) object in the `signedTransactions` array. Use a [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) object to read the transaction information in the payload.

This response can contain a maximum of 50 transactions in the `signedTransactions` array.

## See Also

- [Get Refund History](get-refund-history.md)
  Get a paginated list of all of a customer’s refunded in-app purchases for your app.
- [object RefundHistoryResponse](refundhistoryresponse.md)
  A response that contains an array of signed JSON Web Signature (JWS) refunded transactions, and paging information.
- [Get Refund History V1](get-refund-history-v1.md)
  Get a list of up to 50 of a customer’s refunded in-app purchases for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/refundlookupresponse)*