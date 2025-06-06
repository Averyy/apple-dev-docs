# transactionId

**Framework**: App Store Server Notifications  
**Kind**: typealias

The unique identifier for a transaction, such as an In-App Purchase, restored purchase, or subscription renewal.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
string transactionId
```

#### Discussion

The App Store generates a new value for transaction identifier every time the subscription automatically renews or the user restores it on a new device.

When a user first purchases a subscription, the transaction identifier always matches the original transaction identifier ([`originalTransactionId`](originaltransactionid.md)). For a restore or renewal, the transaction identifier doesn’t match the original transaction identifier. If a user restores or renews the same subscription multiple times, each restore or renewal has a unique transaction identifier.

## See Also

- [type originalTransactionId](originaltransactionid.md)
  The original transaction identifier of a purchase.
- [type webOrderLineItemId](weborderlineitemid.md)
  The unique identifier of subscription purchase events across devices, including subscription renewals.
- [type previousOriginalTransactionId](previousoriginaltransactionid.md)
  The original transaction identifer of a subscription before migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/transactionid)*