# originalTransactionId

**Framework**: App Store Server Notifications  
**Kind**: typealias

The original transaction identifier of a purchase.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string originalTransactionId
```

#### Discussion

This value is identical to the transaction identifier ([`transactionId`](transactionid.md)) except when the user restores or renews a subscription.

## See Also

- [type transactionId](transactionid.md)
  The unique identifier for a transaction, such as an In-App Purchase, restored purchase, or subscription renewal.
- [type webOrderLineItemId](weborderlineitemid.md)
  The unique identifier of subscription purchase events across devices, including subscription renewals.
- [type previousOriginalTransactionId](previousoriginaltransactionid.md)
  The original transaction identifer of a subscription before migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/originaltransactionid)*