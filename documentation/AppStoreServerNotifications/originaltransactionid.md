# originalTransactionId

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The original transaction identifier of a purchase.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```
string originalTransactionId
```

## Discussion

This value is identical to the transaction identifier ([`transactionId`](./transactionid.md)) except when the user restores or renews a subscription.

## See Also

### Transaction identifiers
- [type transactionId](./transactionid.md)
  The unique identifier for a transaction, such as an In-App Purchase, restored purchase, or subscription renewal.
- [type webOrderLineItemId](./weborderlineitemid.md)
  The unique identifier of subscription purchase events across devices, including subscription renewals.
- [type previousOriginalTransactionId](./previousoriginaltransactionid.md)
  The original transaction identifier of a subscription before migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/originaltransactionid)*