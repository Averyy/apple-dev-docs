# transactionId

**Framework**: App Store Server API  
**Kind**: typealias

The unique identifier for a transaction, such as an In-App Purchase, restored In-App Purchase, or subscription renewal.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
string transactionId
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

In a purchase transaction, the `transactionId` matches the original transaction identifier, [`originalTransactionId`](originaltransactionid.md). When a customer restores a purchase or renews a subscription, the `transactionId` differs.

## See Also

- [type originalTransactionId](originaltransactionid.md)
  The original transaction identifier of a purchase.
- [type webOrderLineItemId](weborderlineitemid.md)
  The unique identifier of subscription-purchase events across devices, including renewals.
- [type anyTransactionId](anytransactionid.md)
  A type that represents an original transaction ID, transaction ID, or app transaction ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/transactionid)*