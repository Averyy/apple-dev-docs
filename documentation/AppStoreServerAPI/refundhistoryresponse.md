# RefundHistoryResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains an array of signed JSON Web Signature (JWS) refunded transactions, and paging information.

**Availability**:
- App Store Server API 1.6+

## Declaration

```swift
object RefundHistoryResponse
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The [`Get Refund History`](get-refund-history.md) endpoint returns this response.

This response returns a maximum of 20 refunded transactions. If your customer has more than 20 refunded transactions, the `hasMore` value is `true`. Each response includes a [`revision`](refundhistoryresponse/revision.md) token. Call [`Get Refund History`](get-refund-history.md) again with the [`revision`](refundhistoryresponse/revision.md) token in the query to receive the next set of transactions. When the App Store has no more transactions to send, the `hasMore` value is `false`.

Consider storing the `revision` token from the last page of results with other customer account information. Use it at a later date when you call [`Get Refund History`](get-refund-history.md) to request any new refunded transactions since the last time you called the endpoint for the customer. By using the stored `revision` token, you can avoid fetching transactions you’ve already received.

## Topics

### Response data types
- [type hasMore](hasmore.md)
  A Boolean value indicating whether the App Store has more transaction data.
- [type revision](revision.md)
  A token you use in a query to request the next set of transactions for the customer.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

## See Also

- [Get Refund History](get-refund-history.md)
  Get a paginated list of all of a customer’s refunded in-app purchases for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/refundhistoryresponse)*