# revocationDate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The date that the App Store refunded or revoked the transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let revocationDate: Date?
```

## Mentions

- [Managing the life cycle of monthly subscriptions with a 12-month commitment](../managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment.md)
- [Testing refund requests](../testing-refund-requests.md)
- [Supporting monthly subscriptions with a 12-month commitment](../supporting-monthly-subscriptions-with-a-12-month-commitment.md)
- [Testing Family Sharing](../testing-family-sharing.md)

## Discussion

The App Store revokes a transaction when it refunds the transaction, when it revokes the transaction from Family Sharing, or when the customer loses access through an organization or group. Read [`revocationType`](./revocationtype-swift.property.md) to learn where the revocation originated.

## See Also

### Getting revocation status
- [let revocationReason: Transaction.RevocationReason?](./revocationreason-swift.property.md)
  The reason that the App Store refunded or revoked the transaction.
- [Transaction.RevocationReason](./revocationreason-swift.struct.md)
  Reasons that describe why the App Store may refund or revoke a transaction.
- [let revocationType: Transaction.RevocationType?](./revocationtype-swift.property.md)
  The type of refund or revocation that applies to the transaction.
- [Transaction.RevocationType](./revocationtype-swift.struct.md)
  The types of refunds and revocations that apply to transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationdate)*