# revision

**Framework**: App Store Server API  
**Kind**: typealias

A token you use in a query to request the next set of transactions for the customer.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
string revision
```

#### Discussion

The App Store server returns a `revision` value in each response to certain endpoints, such as [`Get Transaction History`](get-transaction-history.md) and [`Get Refund History`](get-refund-history.md). Use the `revision` value to get a set of paginated transactions.

The first time you call an endpoint, you don’t include a `revision` query parameter, and the API returns the customer’s first set of up to 20 transactions. If there are more transactions, the [`hasMore`](hasmore.md) value in the response is `true`. To get the next set of transactions, use the [`revision`](revision.md) value from the response in your subsequent call to the endpoint.

Consider storing the `revision` value from the last page of transactions, when the [`hasMore`](hasmore.md) value is `false`, with other customer account information.  Use it the next time you call the endpoint for the same customer, to avoid fetching transactions you’ve already received. For the [`Get Transaction History`](get-transaction-history.md) endpoint, store the `revision` value only if you request the transaction history in `ASCENDING` sort order.

## See Also

- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type environment](environment.md)
  The server environment, either sandbox or production.
- [type hasMore](hasmore.md)
  A Boolean value indicating whether the App Store has more transaction data.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/revision)*