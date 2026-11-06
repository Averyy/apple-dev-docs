# revocationType

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The type of refund or revocation that applies to the transaction.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
let revocationType: Transaction.RevocationType?
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)

## Discussion

This property indicates whether the transaction has a full refund or a prorated refund, the App Store revoked it from Family Sharing, or the customer no longer has access through an organization or group. The value is `nil` for transactions that aren’t revoked. For more information about removals from an organization or group, see [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md).

This property isn’t present for Advanced Commerce transactions, which use [`refunds`](./advancedcommerceinfo-swift.struct/item/refunds.md) instead.

## See Also

### Getting revocation status
- [let revocationDate: Date?](./revocationdate.md)
  The date that the App Store refunded or revoked the transaction.
- [let revocationReason: Transaction.RevocationReason?](./revocationreason-swift.property.md)
  The reason that the App Store refunded or revoked the transaction.
- [Transaction.RevocationReason](./revocationreason-swift.struct.md)
  Reasons that describe why the App Store may refund or revoke a transaction.
- [Transaction.RevocationType](./revocationtype-swift.struct.md)
  The types of refunds and revocations that apply to transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property)*