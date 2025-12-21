# HistoryResponse

**Framework**: App Store Server API  
**Kind**: dictionary

A response that contains the customer’s transaction history for an app.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object HistoryResponse
```

#### Discussion

The [`Get Transaction History`](get-transaction-history.md) endpoint returns the [`HistoryResponse`](historyresponse.md). This response contains results for all in-app purchase product types: auto-renewable subscriptions, non-renewing subscriptions, non-consumables, and consumables. The result includes transactions in any state, including transactions that are refunded or revoked, and transactions that the app has or hasn’t marked as finished.

The history response returns a maximum of 20 transactions per response. If your customer has more than 20 in-app transactions, the [`hasMore`](historyresponse/hasmore.md) value is `true`. Each response includes a [`revision`](historyresponse/revision.md) value. Call [`Get Transaction History`](get-transaction-history.md) again with the `revision` token in the query to receive the next set of transactions; use the same query parameters for each subsequent call that includes `revision`. When the App Store has no more transactions to send, the `hasMore` value is `false`.

If a customer upgrades a subscription or the App Store revokes an in-app purchase while you’re receiving transaction history, the App Store updates the relevant transaction. If the response is sorted in `ASCENDING` order, you receive the transaction again, with updated data.

> **Note**:  The [`Get Transaction History V1`](get-transaction-history-v1.md) endpoint also returns the [`HistoryResponse`](historyresponse.md), however, it doesn’t include consumable in-app purchases that the app has marked as finished. Use [`Get Transaction History`](get-transaction-history.md) instead.

## Topics

### Response data types
- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type environment](environment.md)
  The server environment, either sandbox or production.
- [type hasMore](hasmore.md)
  A Boolean value indicating whether the App Store has more transaction data.
- [type revision](revision.md)
  A token you use in a query to request the next set of transactions for the customer.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

## See Also

- [Get Transaction History](get-transaction-history.md)
  Get a customer’s in-app purchase transaction history for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/historyresponse)*