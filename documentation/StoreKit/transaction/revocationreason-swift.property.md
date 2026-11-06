# revocationReason

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The reason that the App Store refunded or revoked the transaction.

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
let revocationReason: Transaction.RevocationReason?
```

## Mentions

- [Testing refund requests](../testing-refund-requests.md)
- [Testing Family Sharing](../testing-family-sharing.md)

## Discussion

Read [`revocationType`](./revocationtype-swift.property.md) to learn where the revocation originated.

## See Also

### Getting revocation status
- [let revocationDate: Date?](./revocationdate.md)
  The date that the App Store refunded or revoked the transaction.
- [Transaction.RevocationReason](./revocationreason-swift.struct.md)
  Reasons that describe why the App Store may refund or revoke a transaction.
- [let revocationType: Transaction.RevocationType?](./revocationtype-swift.property.md)
  The type of refund or revocation that applies to the transaction.
- [Transaction.RevocationType](./revocationtype-swift.struct.md)
  The types of refunds and revocations that apply to transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationreason-swift.property)*