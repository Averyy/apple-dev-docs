# revocationDate

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The date that the App Store refunded the transaction or revoked it from Family Sharing.

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

## See Also

### Getting revocation status
- [let revocationReason: Transaction.RevocationReason?](./revocationreason-swift.property.md)
  The reason that the App Store refunded the transaction or revoked it from Family Sharing.
- [Transaction.RevocationReason](./revocationreason-swift.struct.md)
  Reasons that describe why the App Store may refund a transaction or revoke it from Family Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationdate)*